// functions/api/create-checkout.js - Cloudflare Pages Function

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
    const body = await context.request.json();
    const { plan, name, email, phone, successUrl, cancelUrl } = body;

    if (!plan || !name) {
      return new Response(
        JSON.stringify({ error: 'Missing required parameters: plan and name are required.' }),
        { status: 400, headers: corsHeaders }
      );
    }

    const customerEmail = email || `${name.toLowerCase().replace(/[^a-z0-9]/g, '') || 'customer'}@vantacin.com`;

    // Live Bachs API Secret Key from environment or fallback
    const secretKey = (context.env && context.env.BACHS_SECRET_KEY) || "sk_live_4c415f3e_z7Y3N6gTwBnESIYiMQMZmrdHjHffHcUov7cHqEcJMsg";
    const apiBaseUrl = 'https://api.bachs.io/v1';

    // Official pre-created Bachs products for Vantacin+
    const products = {
      '1bottle': { id: 'prod_c6f6822851774830b9a9', name: 'VANTACIN+ — 1 Bottle Starter (15% Off)', amount: '17000.00' },
      '2bottles': { id: 'prod_8f462debad5c416297aa', name: 'VANTACIN+ — 2 Bottles Recommended (15% Off)', amount: '28900.00' },
      '3bottles': { id: 'prod_89dfb019004541d7bc86', name: 'VANTACIN+ — 3 Bottles Eradication Bundle (15% Off)', amount: '34000.00' }
    };

    const cleanPlanKey = (plan || '2bottles').toLowerCase().replace(/[^a-z0-9]/g, '');
    let selectedPlan = products[cleanPlanKey];
    if (!selectedPlan) {
      if (cleanPlanKey.includes('1')) selectedPlan = products['1bottle'];
      else if (cleanPlanKey.includes('3')) selectedPlan = products['3bottles'];
      else selectedPlan = products['2bottles'];
    }

    const headers = {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${secretKey}`,
      'User-Agent': 'VantacinCloudflareApp/1.0'
    };

    // Create checkout session using the product ID
    const reference = `vantacin_${Date.now()}_${Math.floor(Math.random() * 1000)}`;
    const sessionPayload = {
      product_cart: [
        {
          product_id: selectedPlan.id,
          quantity: 1
        }
      ],
      customer: {
        email: customerEmail,
        name: name,
        phone_number: phone || ''
      },
      success_url: successUrl || 'https://vanticina.pages.dev/thank-you.html?status=success&paid=true',
      cancel_url: cancelUrl || 'https://vanticina.pages.dev/thank-you.html?status=cancelled',
      reference: reference,
      metadata: {
        plan: plan,
        customer_name: name,
        customer_phone: phone || ''
      }
    };

    const sessionResponse = await fetch(`${apiBaseUrl}/checkout-sessions`, {
      method: 'POST',
      headers,
      body: JSON.stringify(sessionPayload)
    });

    if (!sessionResponse.ok) {
      const errorText = await sessionResponse.text();
      throw new Error(`Bachs Session Creation Failed: ${sessionResponse.status} - ${errorText}`);
    }

    const sessionData = await sessionResponse.json();

    return new Response(
      JSON.stringify({
        checkoutUrl: sessionData.checkout_url,
        checkoutId: sessionData.checkout_id || null,
        reference: reference
      }),
      { status: 200, headers: corsHeaders }
    );

  } catch (error) {
    console.error('Error initiating Bachs payment:', error);
    return new Response(
      JSON.stringify({ error: error.message || 'Internal server error occurred.' }),
      { status: 500, headers: corsHeaders }
    );
  }
}
