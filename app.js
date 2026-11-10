// Vantacin+ Interactive Logic & Order Management

// 1. Countdown Timer (15:00 Urgency)
function startCountdown() {
  const timerEl = document.getElementById('countdown-timer');
  if (!timerEl) return;

  let totalSeconds = 14 * 60 + 59;
  setInterval(() => {
    if (totalSeconds <= 0) {
      totalSeconds = 15 * 60; // reset
    }
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    timerEl.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    totalSeconds--;
  }, 1000);
}

// 2. Package Selector & Form Auto-scroll
function selectPackageForForm(packageKey, name, price) {
  const radio = document.querySelector(`input[name="order_package"][value="${packageKey}"]`);
  if (radio) {
    radio.checked = true;
    updateRadioCardSelection(packageKey);
  }
  const formSection = document.getElementById('order-form-section');
  if (formSection) {
    formSection.scrollIntoView({ behavior: 'smooth' });
  }
}

function updateRadioCardSelection(packageKey) {
  ['1bottle', '2bottles', '3bottles'].forEach((key) => {
    const card = document.getElementById(`card-${key}`);
    const input = card ? card.querySelector('input') : null;
    if (card && input) {
      if (input.checked) {
        card.classList.add('selected');
      } else {
        card.classList.remove('selected');
      }
    }
  });
}

// 3. Direct Order Form Submission Handler
async function handleDirectOrderSubmit(e) {
  e.preventDefault();
  
  const submitBtn = document.getElementById('btn-submit-order');
  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.textContent = 'Processing Order... ⏳';
  }

  const name = document.getElementById('order-name').value.trim();
  const phone = document.getElementById('order-phone').value.trim();
  const altPhone = document.getElementById('order-alt-phone').value.trim();
  const address = document.getElementById('order-address').value.trim();
  const city = document.getElementById('order-city').value.trim();
  const state = document.getElementById('order-state').value;
  
  const selectedRadio = document.querySelector('input[name="order_package"]:checked');
  const plan = selectedRadio ? selectedRadio.value : '2bottles';

  const amounts = {
    '1bottle': 20000,
    '2bottles': 34000,
    '3bottles': 40000
  };

  const amount = amounts[plan] || 34000;

  const orderPayload = {
    name: name,
    phone: phone,
    alt_phone: altPhone,
    address: address,
    city: city,
    state: state,
    plan: plan,
    amount: amount
  };

  let orderRef = '';

  // Submit to backend API (/api/submit-order) with fallback timeout
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 2000);

    const response = await fetch('/api/submit-order', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(orderPayload),
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    if (response.ok) {
      const result = await response.json();
      if (result.orderRef) orderRef = result.orderRef;
    }
  } catch (err) {
    console.warn('Order background sync logged or timed out:', err);
  }

  // Determine package number (1, 2, or 3)
  const pkgMap = { '1bottle': '1', '2bottles': '2', '3bottles': '3' };
  const pkg = pkgMap[plan] || '2';
  const uniqueOrder = orderRef || ('VAN-' + Date.now().toString(36).toUpperCase() + '-' + Math.floor(100 + Math.random() * 900));

  // Store order details in sessionStorage so /thank-you can display details without putting PII in the URL
  try {
    sessionStorage.setItem('vantacin_last_order', JSON.stringify({
      name: name,
      phone: phone,
      alt_phone: altPhone,
      address: address,
      city: city,
      state: state,
      pkg: pkg,
      order: uniqueOrder,
      plan: plan,
      amount: amount
    }));
  } catch (err) {
    console.warn('sessionStorage save error:', err);
  }

  // Redirect to /thank-you with only pkg and order (NO personal or health information in URL)
  window.location.href = `thank-you?pkg=${encodeURIComponent(pkg)}&order=${encodeURIComponent(uniqueOrder)}`;
}

// 4. Testimonial Lightbox
function openLightbox(src) {
  const modal = document.getElementById('lightbox-modal');
  const img = document.getElementById('lightbox-img');
  if (modal && img) {
    img.src = src;
    modal.classList.add('active');
  }
}

function closeLightbox() {
  const modal = document.getElementById('lightbox-modal');
  if (modal) {
    modal.classList.remove('active');
  }
}

// 5. Sticky Floating Bar on Scroll
window.addEventListener('scroll', () => {
  const floatingBar = document.getElementById('floating-bar');
  if (!floatingBar) return;
  
  if (window.scrollY > 600) {
    floatingBar.classList.add('visible');
  } else {
    floatingBar.classList.remove('visible');
  }
});

// Close modals on ESC key
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    closeLightbox();
  }
});

// 6. Meta Pixel Tracking Logic
function setupMetaPixelTracking() {
  // Fire ViewContent on landing page load (without any sensitive or health parameters)
  if (typeof fbq === 'function') {
    fbq('track', 'ViewContent');
  }

  // Fire InitiateCheckout once when the visitor first starts filling in the order form (first focus on any form field)
  // Not on the "order now" buttons that only scroll to the form
  let initiateCheckoutFired = false;
  const orderForm = document.getElementById('direct-order-form');
  if (orderForm) {
    const formFields = orderForm.querySelectorAll('input, select, textarea');
    formFields.forEach((field) => {
      field.addEventListener('focus', () => {
        if (!initiateCheckoutFired) {
          initiateCheckoutFired = true;
          if (typeof fbq === 'function') {
            fbq('track', 'InitiateCheckout');
          }
        }
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
  startCountdown();
  setupMetaPixelTracking();
});
