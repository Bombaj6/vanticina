// api/create-checkout.js - Bachs.io Payment Gateway Integration

export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Credentials', true);
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const { plan, name, email, phone, successUrl, cancelUrl } = req.body;

    if (!plan || !name) {
      return res.status(400).json({ error: 'Missing required parameters: plan and name are required.' });
    }

    const customerEmail = email || `${name.toLowerCase().replace(/[^a-z0-9]/g, '') || 'customer'}@vantacin.com`;

    // Live Bachs API Secret Key
    const secretKey = process.env.BACHS_SECRET_KEY || "sk_live_4c415f3e_z7Y3N6gTwBnESIYiMQMZmrdHjHffHcUov7cHqEcJMsg";
    const apiBaseUrl = 'https://api.bachs.io/v1';

    // Official pre-created Bachs products for Vantacin+
    const products = {
      '1bottle': { id: 'prod_c6f6822851774830b9a9', name: 'VANTACIN+ — 1 Bottle Starter (15% Off)', amount: '17000.00' },
      '2bottles': { id: 'prod_8f462debad5c416297aa', name: 'VANTACIN+ — 2 Bottles Recommended (15% Off)', amount: '28900.00' },
      '3bottles': { id: 'prod_89dfb019004541d7bc86', name: 'VANTACIN+ — 3 Bottles Eradication Bundle (15% Off)', amount: '34000.00' }
    };

    const cleanPlanKey = plan.toLowerCase().replace(/[^a-z0-9]/g, '');
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
      'User-Agent': 'VantacinApp/1.0'
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
      success_url: successUrl || 'https://vanticina.vercel.app/thank-you.html?status=success&paid=true',
      cancel_url: cancelUrl || 'https://vanticina.vercel.app/thank-you.html?status=cancelled',
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

    return res.status(200).json({
      checkoutUrl: sessionData.checkout_url,
      checkoutId: sessionData.checkout_id || null,
      reference: reference
    });

  } catch (error) {
    console.error('Error initiating Bachs payment:', error);
    return res.status(500).json({ error: error.message || 'Internal server error occurred.' });
  }
}
