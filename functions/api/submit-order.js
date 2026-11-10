// functions/api/submit-order.js - Cloudflare Pages Function
// Stores orders in Cloudflare D1 + forwards to Google Sheets + Telegram / Email alerts

export async function onRequestOptions() {
  return new Response(null, {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    }
  });
}

export async function onRequestPost(context) {
  const corsHeaders = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Content-Type': 'application/json'
  };

  try {
    const data = await context.request.json();
    const { name, phone, alt_phone, address, city, state, plan, amount } = data;

    if (!name || !phone || !address || !state) {
      return new Response(
        JSON.stringify({ error: 'Missing required order fields (name, phone, address, state).' }),
        { status: 400, headers: corsHeaders }
      );
    }

    const orderRef = 'VAN-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(100 + Math.random() * 900);
    const planLabels = {
      '1bottle': '1 Bottle Starter (₦20,000)',
      '2bottles': '2 Bottles Recommended (₦34,000)',
      '3bottles': '3 Bottles Eradication (₦40,000)'
    };
    const packageLabel = planLabels[plan] || `${plan} (₦${Number(amount || 0).toLocaleString()})`;
    const orderAmount = Number(amount) || (plan === '1bottle' ? 20000 : plan === '3bottles' ? 40000 : 34000);

    // 1. Save directly into Cloudflare D1 Database
    if (context.env && context.env.DB) {
      try {
        await context.env.DB.prepare(
          `INSERT INTO orders (order_ref, name, phone, alt_phone, address, city, state, package, amount, payment_method, payment_status)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'COD', 'pending')`
        ).bind(
          orderRef,
          name,
          phone,
          alt_phone || '',
          address,
          city || '',
          state,
          packageLabel,
          orderAmount
        ).run();
      } catch (dbErr) {
        console.error('D1 Database insertion error:', dbErr);
      }
    }

    // Prepare payload for external webhooks (Google Sheets / Email / Telegram)
    const webhookPayload = {
      orderRef,
      createdAt: new Date().toISOString(),
      name,
      phone,
      altPhone: alt_phone || 'None',
      address,
      city: city || 'N/A',
      state,
      plan,
      packageLabel,
      amount: orderAmount,
      paymentMethod: 'Cash on Delivery (COD)'
    };

    // 2. Forward to Google Sheets Webhook if configured
    const googleSheetWebhook = (context.env && context.env.GOOGLE_SHEET_WEBHOOK_URL) || null;
    if (googleSheetWebhook) {
      try {
        fetch(googleSheetWebhook, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(webhookPayload)
        }).catch(err => console.error('Google Sheet webhook error:', err));
      } catch (sheetErr) {
        console.error('Sheet fetch trigger error:', sheetErr);
      }
    }

    // 3. Telegram Instant Alert if configured
    const telegramToken = context.env && context.env.TELEGRAM_BOT_TOKEN;
    const telegramChatId = context.env && context.env.TELEGRAM_CHAT_ID;
    if (telegramToken && telegramChatId) {
      const msg = `🚨 *NEW VANTACIN+ ORDER!*\n\n` +
        `📦 *Package:* ${packageLabel}\n` +
        `💰 *Amount:* ₦${orderAmount.toLocaleString()}\n` +
        `👤 *Customer:* ${name}\n` +
        `📞 *Phone:* ${phone}\n` +
        `📱 *Alt Phone:* ${alt_phone || 'None'}\n` +
        `📍 *Address:* ${address}, ${city || ''}, ${state}\n` +
        `🆔 *Ref:* \`${orderRef}\`\n` +
        `🚚 *Payment:* Cash on Delivery`;

      try {
        fetch(`https://api.telegram.org/bot${telegramToken}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: telegramChatId,
            text: msg,
            parse_mode: 'Markdown'
          })
        }).catch(err => console.error('Telegram alert error:', err));
      } catch (tgErr) {
        console.error('Telegram dispatch error:', tgErr);
      }
    }

    return new Response(
      JSON.stringify({
        success: true,
        orderRef,
        message: 'Order recorded successfully.'
      }),
      { status: 200, headers: corsHeaders }
    );
  } catch (error) {
    console.error('submit-order error:', error);
    return new Response(
      JSON.stringify({ error: error.message || 'Internal Server Error' }),
      { status: 500, headers: corsHeaders }
    );
  }
}
