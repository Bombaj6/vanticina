import base64
import json
import os

def b64(path):
    with open(path, 'rb') as f:
        mime = 'image/png' if path.endswith('.png') else 'image/jpeg'
        return f'data:{mime};base64,' + base64.b64encode(f.read()).decode('utf-8')

# Encode compressed assets for reliable Elementor rendering
img1 = b64('assets_compressed/media_1787735449426.jpg')
img2 = b64('assets_compressed/media_1787735454666.jpg')
img3 = b64('assets_compressed/media_1787735462235.jpg')
img4 = b64('assets_compressed/media_1787735489558.jpg')
img5 = b64('assets_compressed/media_1787735533085.jpg')
img6 = b64('assets_compressed/media_1787736253711.jpg')
img7 = b64('assets_compressed/media_1787736263434.jpg')
img8 = b64('assets_compressed/media_1787736288220.jpg')
img9 = b64('assets_compressed/media_1787736340334.jpg')

chat1 = b64('assets_compressed/testimonial_chat_1.jpg')
chat2 = b64('assets_compressed/testimonial_chat_2.jpg')
chat3 = b64('assets_compressed/testimonial_chat_3.jpg')

hero_img = b64('assets_compressed/hero_lifestyle.jpg')
vantacin_bottle = b64('assets_compressed/vantacin_bottle_clean.jpg')
vantacin_label = b64('assets_compressed/vantacin_front_back.jpg')
vantacin_single = b64('assets_compressed/vantacin_single_bottle.jpg')
vantacin_dual = b64('assets_compressed/vantacin_dual_bottles.jpg')

# 1. GRAPHIC WARNING SECTION
graphic_warning_html = f'''<!-- 
================================================================================
 Elementor HTML Snippet: Graphic Warning - What Untreated Herpes & Recurrent Infections Look Like
 Instructions: Copy all code and paste directly into an Elementor HTML Widget.
 Pictures are base64-embedded so they load 100% reliably.
================================================================================
-->
<div style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 840px; margin: 0 auto; background: #fff5f5; border: 2px solid #feb2b2; border-left: 6px solid #e53e3e; border-radius: 14px; padding: 24px; box-shadow: 0 8px 20px rgba(229, 62, 62, 0.1); box-sizing: border-box;">
  
  <h3 style="color: #9b2c2c; font-size: 1.3rem; font-weight: 800; margin-top: 0; margin-bottom: 10px; display: flex; align-items: center; gap: 8px; line-height: 1.3;">
    ⚠️ GRAPHIC WARNING: WHAT UNTREATED HERPES & RECURRENT INFECTIONS LOOK LIKE
  </h3>

  <p style="font-size: 0.98rem; color: #742a2a; margin-bottom: 18px; line-height: 1.6;">
    When HSV-1, HSV-2, and chronic urogenital infections are left unmanaged or rely solely on temporary symptom-masking drugs, viral biofilms nest deep in sacral and trigeminal nerve ganglia. Over time, recurring outbreaks escalate into painful cluster vesicles, open mucosal fissures, and chronic tissue erosion:
  </p>

  <!-- Clinical Image Grid -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin: 20px 0;">
    
    <div style="background: white; border: 1px solid #feb2b2; border-radius: 10px; padding: 10px; text-align: center;">
      <img src="{img1}" alt="HSV-1/2 Vesicular Cluster Eruption" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.78rem; font-weight: 700; color: #9b2c2c; margin-top: 6px; line-height: 1.3;">
        Fig 1: Active Vesicular Cluster Eruption (Dermatomal HSV Flare-Up)
      </div>
    </div>

    <div style="background: white; border: 1px solid #feb2b2; border-radius: 10px; padding: 10px; text-align: center;">
      <img src="{img2}" alt="Oral Herpes Labial Ulceration" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.78rem; font-weight: 700; color: #9b2c2c; margin-top: 6px; line-height: 1.3;">
        Fig 2: Severe Oral Labial Fissure & Cold Sore Crusting
      </div>
    </div>

    <div style="background: white; border: 1px solid #feb2b2; border-radius: 10px; padding: 10px; text-align: center;">
      <img src="{img3}" alt="Cutaneous Mucosal Outbreak Stage" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.78rem; font-weight: 700; color: #9b2c2c; margin-top: 6px; line-height: 1.3;">
        Fig 3: Open Mucosal Ulceration Stage (Active Viral Shedding)
      </div>
    </div>

    <div style="background: white; border: 1px solid #feb2b2; border-radius: 10px; padding: 10px; text-align: center;">
      <img src="{img4}" alt="Female Genital Herpes Mucosal Flare-Up" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.78rem; font-weight: 700; color: #9b2c2c; margin-top: 6px; line-height: 1.3;">
        Fig 4: Female Mucosal Vulvovaginal Flare-Up & Inflammation
      </div>
    </div>

    <div style="background: white; border: 1px solid #feb2b2; border-radius: 10px; padding: 10px; text-align: center;">
      <img src="{img5}" alt="Male Genital Herpes Lesions" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.78rem; font-weight: 700; color: #9b2c2c; margin-top: 6px; line-height: 1.3;">
        Fig 5: Male Genital Erythema & Recurrent Blistering
      </div>
    </div>

  </div>

  <!-- Infection Checklist Box -->
  <div style="background: white; border-radius: 10px; padding: 18px; border: 1px solid #fed7d7; margin-top: 16px;">
    <h4 style="font-size: 1.05rem; font-weight: 800; color: #9b2c2c; margin-top: 0; margin-bottom: 10px; line-height: 1.3;">
      ❗ ARE YOU SUFFERING FROM ANY OF THESE STUBBORN SYMPTOMS?
    </h4>
    <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 8px; font-size: 0.92rem; font-weight: 700; color: #742a2a;">
      <li>❗ HSV-1 Oral Blisters & Lip Crusting</li>
      <li>❗ HSV-2 Genital Lesions, Itching & Redness</li>
      <li>❗ Painful Burning During Urination (Chronic UTIs)</li>
      <li>❗ Smelly, Abnormal or Persistent Discharge</li>
      <li>❗ Chronic Nerve Tingling in Buttocks & Thighs</li>
      <li>❗ Staphylococcus aureus, E. coli & Pelvic Biofilms</li>
    </ul>
  </div>

  <!-- CTA BUTTON 1 -->
  <div style="text-align: center; margin-top: 22px;">
    <a href="#order-form-section" style="display: inline-block; width: 100%; max-width: 500px; text-decoration: none; font-size: 1.05rem; font-weight: 800; padding: 16px 20px; color: white; background: linear-gradient(135deg, #c53030 0%, #991b1b 100%); border-radius: 8px; box-shadow: 0 6px 20px rgba(197, 48, 48, 0.35); text-align: center; box-sizing: border-box;">
      👉 STOP RECURRENT OUTBREAKS — ORDER VANTACIN+ NOW →
    </a>
  </div>
</div>
'''

with open('graphic_warning_section.html', 'w') as f:
    f.write(graphic_warning_html)
with open('graphic_warning_section_source.txt', 'w') as f:
    f.write(graphic_warning_html)

# 2. CLINICAL STATS SECTION
clinical_stats_html = '''<!-- 
================================================================================
 Elementor HTML Snippet: Clinical Review of Long-Term Antiviral Patients
 Instructions: Copy all code below and paste into an Elementor HTML widget.
================================================================================
-->
<div style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 840px; margin: 0 auto; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 12px; padding: 24px; box-sizing: border-box;">
  <h4 style="font-size: 1.15rem; font-weight: 800; color: #1e3a8a; margin-top: 0; margin-bottom: 14px; line-height: 1.3;">
    📊 Clinical Review of Long-Term Antiviral & Suppressive Therapy Patients:
  </h4>
  <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px;">
    <li style="display: flex; gap: 10px; font-weight: 600; color: #1e3a8a; font-size: 0.98rem; line-height: 1.6;">
      <span>⚬</span> <span><strong>68%</strong> experienced breakthrough outbreaks and active viral shedding despite daily synthetic medications.</span>
    </li>
    <li style="display: flex; gap: 10px; font-weight: 600; color: #1e3a8a; font-size: 0.98rem; line-height: 1.6;">
      <span>⚬</span> <span><strong>54%</strong> suffered from chronic fatigue, brain fog, and mitochondrial energy depletion.</span>
    </li>
    <li style="display: flex; gap: 10px; font-weight: 600; color: #1e3a8a; font-size: 0.98rem; line-height: 1.6;">
      <span>⚬</span> <span><strong>31%</strong> showed elevated renal strain markers due to the liver and kidneys filtering synthetic chemicals continuously.</span>
    </li>
    <li style="display: flex; gap: 10px; font-weight: 600; color: #1e3a8a; font-size: 0.98rem; line-height: 1.6;">
      <span>⚬</span> <span><strong>Almost 100%</strong> lived in constant fear, intimacy anxiety, and emotional guilt about accidental transmission.</span>
    </li>
  </ul>
</div>
'''

with open('clinical_review_stats_section.html', 'w') as f:
    f.write(clinical_stats_html)

# 3. CLINICAL EVIDENCE REASON 2 (FIG 6 & 7)
reason2_html = f'''<!-- 
================================================================================
 Elementor HTML Snippet: Reason 2 - Clinical Evidence Fig 6 & Fig 7
 Instructions: Copy all code below and paste into an Elementor HTML widget.
================================================================================
-->
<div style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 840px; margin: 0 auto; background: #fffdfd; border: 2px solid #fecaca; border-left: 6px solid #dc2626; border-radius: 14px; padding: 22px; box-shadow: 0 4px 15px rgba(220, 38, 38, 0.08); box-sizing: border-box;">
  <h4 style="color: #991b1b; font-size: 1.15rem; font-weight: 800; margin-top: 0; margin-bottom: 8px; line-height: 1.3;">
    🔬 CLINICAL EVIDENCE: RECURRENT EPITHELIAL VIRAL REPLICATION STAGES
  </h4>
  <p style="font-size: 0.94rem; color: #7f1d1d; margin-bottom: 14px; line-height: 1.6;">
    When mucosal immunity and cellular microcirculation break down, viral particles travel unobstructed down nerve axons to mucosal surfaces, causing severe epidermoid erosions and persistent viral scaling:
  </p>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 14px;">
    <div style="background: white; border: 1px solid #fca5a5; border-radius: 8px; padding: 8px; text-align: center;">
      <img src="{img6}" alt="Recurrent Herpes Simplex Virus Epithelial Lesion" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.76rem; font-weight: 700; color: #991b1b; margin-top: 6px; line-height: 1.3;">
        Fig 6: Recurrent Herpes Simplex Epithelial Lesion & Scaling
      </div>
    </div>
    <div style="background: white; border: 1px solid #fca5a5; border-radius: 8px; padding: 8px; text-align: center;">
      <img src="{img7}" alt="Severe Recurrent Cutaneous Ulceration" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
      <div style="font-size: 0.76rem; font-weight: 700; color: #991b1b; margin-top: 6px; line-height: 1.3;">
        Fig 7: Severe Recurrent Cutaneous Ulceration & Erythema
      </div>
    </div>
  </div>
</div>
'''

with open('clinical_evidence_reason2.html', 'w') as f:
    f.write(reason2_html)

# 4. CLINICAL EVIDENCE REASON 5 (FIG 8 & 9) + RETAIL MARKUP
reason5_html = f'''<!-- 
================================================================================
 Elementor HTML Snippet: Reason 5 - Clinical Evidence Fig 8 & 9 & Retail Markup
 Instructions: Copy all code below and paste into an Elementor HTML widget.
================================================================================
-->
<div style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 840px; margin: 0 auto;">
  
  <h2 style="font-size: 1.6rem; font-weight: 800; color: #0f172a; margin: 36px 0 18px 0; line-height: 1.3; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;">
    REASON 5: WHY YOU CAN'T BUY VANTACIN+ IN REGULAR PHARMACY CHAINS
  </h2>

  <p style="font-size: 1.08rem; color: #1e293b; line-height: 1.8; margin-bottom: 22px;">
    Many patients ask me: <em>“Dr. Reynolds, if VANTACIN+ is NAFDAC-approved and so effective, why don't I see it in every roadside pharmacy or supermarket?”</em>
  </p>

  <p style="font-size: 1.08rem; color: #1e293b; line-height: 1.8; margin-bottom: 22px;">
    The answer comes down to quality control, anti-counterfeiting, and price integrity:
  </p>

  <!-- CLINICAL EVIDENCE GALLERY (FIG 8 & FIG 9) -->
  <div style="background: #fffdfd; border: 2px solid #fee2e2; border-left: 6px solid #b91c1c; border-radius: 14px; padding: 22px; margin: 24px 0; box-shadow: 0 4px 15px rgba(185, 28, 28, 0.08);">
    <h4 style="color: #991b1b; font-size: 1.15rem; font-weight: 800; margin-top: 0; margin-bottom: 8px; line-height: 1.3;">
      ⚠️ CLINICAL EVIDENCE: MUCOSAL FLARE-UP & VIRAL SHEDDING STAGES
    </h4>
    <p style="font-size: 0.94rem; color: #7f1d1d; margin-bottom: 14px; line-height: 1.6;">
      High-dose pharmaceutical antivirals and incomplete antibiotic courses often fail to eliminate mucosal bio-membranes, leaving persistent viral reservoirs that erupt under friction and hormonal shifts:
    </p>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 14px;">
      
      <!-- Fig 8 Picture -->
      <div style="background: white; border: 1px solid #fca5a5; border-radius: 8px; padding: 8px; text-align: center;">
        <img src="{img8}" alt="Mucosal Erythematous Ulceration" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
        <div style="font-size: 0.76rem; font-weight: 700; color: #991b1b; margin-top: 6px; line-height: 1.3;">
          Fig 8: Mucosal Erythematous Ulceration & Encrustation Stage
        </div>
      </div>

      <!-- Fig 9 Picture -->
      <div style="background: white; border: 1px solid #fca5a5; border-radius: 8px; padding: 8px; text-align: center;">
        <img src="{img9}" alt="Nerve Ganglia Eruption Stage" style="width: 100%; height: 160px; object-fit: cover; border-radius: 6px; display: block;">
        <div style="font-size: 0.76rem; font-weight: 700; color: #991b1b; margin-top: 6px; line-height: 1.3;">
          Fig 9: Cutaneous Nerve Ganglia Eruption Stage (Active Vesicles)
        </div>
      </div>

    </div>
  </div>

  <!-- RETAIL PHARMACY MARKUP WARNING BOX -->
  <div style="background: #fffdfd; border: 1px solid #fee2e2; border-left: 4px solid #c53030; border-radius: 10px; padding: 20px; margin: 20px 0;">
    <h4 style="font-size: 1.1rem; font-weight: 800; color: #991b1b; margin-top: 0; margin-bottom: 8px; line-height: 1.3;">
      ⚠️ Retail Pharmacy Middleman Markup & Counterfeit Risks
    </h4>
    <p style="font-size: 0.95rem; color: #7f1d1d; margin: 0; line-height: 1.6;">
      Selling through third-party wholesalers adds massive retail markups, pushing the price of a single bottle above ₦35,000. Even worse, counterfeit herbal preparations run rampant in uncontrolled open markets.
    </p>
  </div>

  <p style="font-size: 1.08rem; color: #1e293b; line-height: 1.8; margin-bottom: 22px;">
    By dispatching <strong>VANTACIN+ Capsules</strong> directly from the manufacturer (Varna Services Ltd., No. 2, Ven. Adefila Street, G.R.A. Ilorin), every customer is guaranteed 100% genuine, fresh, laboratory-certified product delivered discreetly right to their doorstep with payment on delivery.
  </p>

</div>
'''

with open('clinical_evidence_reason5.html', 'w') as f:
    f.write(reason5_html)
with open('clinical_evidence_reason5_source.txt', 'w') as f:
    f.write(reason5_html)

# 5. TESTIMONIALS SECTION (REAL WHATSAPP CHATS + REVIEWS)
testimonials_html = f'''<!-- 
================================================================================
 Elementor HTML Snippet: Real WhatsApp Chat Testimonials & Verified Reviews
 Instructions: Copy all code below and paste into an Elementor HTML widget.
 Real WhatsApp screenshots are base64-embedded so they load 100% reliably!
================================================================================
-->
<div style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 840px; margin: 0 auto;">
  
  <h2 style="font-size: 1.6rem; font-weight: 800; color: #0f172a; margin: 36px 0 18px 0; line-height: 1.3; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;">
    REAL CUSTOMER CHATS & VERIFIED REVIEWS
  </h2>

  <p style="font-size: 1rem; color: #475569; margin-bottom: 20px;">
    Here is unfiltered, real proof from real customers who experienced life-changing relief with Vantacin+ Capsules:
  </p>

  <!-- Real WhatsApp Chat Screenshots -->
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin: 28px 0;">
    
    <!-- Chat 1 -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; box-shadow: 0 6px 18px rgba(0,0,0,0.06);">
      <img src="{chat1}" alt="WhatsApp Customer Testimonial 1 - Vantacin Worked Well" style="width: 100%; height: 380px; object-fit: cover; object-position: top; display: block;">
      <div style="padding: 16px; background: #f8fafc; border-top: 1px solid #e2e8f0;">
        <strong style="display: block; font-size: 0.95rem; color: #0f172a; margin-bottom: 4px;">“The drug worked well, no more pain!”</strong>
        <p style="font-size: 0.85rem; color: #64748b; margin: 0; line-height: 1.5;">
          “Vantacin plus Capsules For infections... Yes, the drug worked well, thank God. That's the joy, no more pain and infection has gone back to where it came from.”
        </p>
      </div>
    </div>

    <!-- Chat 2 -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; box-shadow: 0 6px 18px rgba(0,0,0,0.06);">
      <img src="{chat2}" alt="WhatsApp Customer Testimonial 2 - Loves Capsules Form" style="width: 100%; height: 380px; object-fit: cover; object-position: top; display: block;">
      <div style="padding: 16px; background: #f8fafc; border-top: 1px solid #e2e8f0;">
        <strong style="display: block; font-size: 0.95rem; color: #0f172a; margin-bottom: 4px;">“Love that it is in convenient capsules”</strong>
        <p style="font-size: 0.85rem; color: #64748b; margin: 0; line-height: 1.5;">
          “The reason I love your product is that it is in capsule. Some that I take is in powdery form. I treated with herbal drugs several times last year... God will heal me with your drugs.”
        </p>
      </div>
    </div>

    <!-- Chat 3 -->
    <div style="background: white; border: 1px solid #e2e8f0; border-radius: 14px; overflow: hidden; box-shadow: 0 6px 18px rgba(0,0,0,0.06);">
      <img src="{chat3}" alt="WhatsApp Customer Testimonial 3 - Dramatic Recovery" style="width: 100%; height: 380px; object-fit: cover; object-position: top; display: block;">
      <div style="padding: 16px; background: #f8fafc; border-top: 1px solid #e2e8f0;">
        <strong style="display: block; font-size: 0.95rem; color: #0f172a; margin-bottom: 4px;">“Noticed tremendous improvement & pain relief”</strong>
        <p style="font-size: 0.85rem; color: #64748b; margin: 0; line-height: 1.5;">
          “I have noticed some improvement, I am happy... The chest pain has reduced, the back pain has reduced, the severe bloating and gas has reduced. I can eat meals now that normally cause pain.”
        </p>
      </div>
    </div>

  </div>

  <!-- Review Cards -->
  <div style="display: flex; flex-direction: column; gap: 18px; margin: 28px 0;">
    
    <div style="background: #f8fafc; border-left: 4px solid #2563eb; padding: 20px 24px; border-radius: 0 10px 10px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; flex-wrap: wrap; gap: 6px;">
        <div style="color: #f59e0b; font-size: 0.95rem; font-weight: 700;">★★★★★</div>
        <span style="font-size: 0.78rem; background: #d1fae5; color: #065f46; font-weight: 800; padding: 3px 8px; border-radius: 4px;">✓ Verified Buyer</span>
      </div>
      <div style="font-weight: 800; font-size: 1.1rem; color: #0f172a; margin-bottom: 6px; line-height: 1.3;">
        “Outbreaks Stopped Completely & No More Burning”
      </div>
      <div style="font-style: italic; font-size: 0.98rem; color: #334155; line-height: 1.6; margin-bottom: 8px;">
        "I suffered from recurrent HSV-2 outbreaks and severe kidney aches from prescription antivirals for over 3 years. Vantacin+ cleared up the intense tingling within 5 days, and I haven't had a single flare-up in over 7 months."
      </div>
      <div style="font-size: 0.88rem; font-weight: 700; color: #64748b;">— Jennifer R., Lagos (Verified Buyer)</div>
    </div>

    <div style="background: #f0fdf4; border-left: 4px solid #059669; padding: 20px 24px; border-radius: 0 10px 10px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; flex-wrap: wrap; gap: 6px;">
        <div style="color: #f59e0b; font-size: 0.95rem; font-weight: 700;">★★★★★</div>
        <span style="font-size: 0.78rem; background: #bbf7d0; color: #166534; font-weight: 800; padding: 3px 8px; border-radius: 4px;">🩺 Clinical Specialist Endorsement</span>
      </div>
      <div style="font-weight: 800; font-size: 1.1rem; color: #065f46; margin-bottom: 6px; line-height: 1.3;">
        “Dismantles Viral & Bacterial Biofilms at the Root”
      </div>
      <div style="font-style: italic; font-size: 0.98rem; color: #166534; line-height: 1.6; margin-bottom: 8px;">
        "As an integrative physician, I recommend Vantacin+ to patients with chronic genital herpes and treatment-resistant UTIs because its botanical synergy of Acacia Nilotica and Hunteria Umbellata addresses hidden biofilms rather than just masking symptoms."
      </div>
      <div style="font-size: 0.88rem; font-weight: 700; color: #047857;">— Dr. Evelyn Vance, ND (Integrative Virology & Immunology)</div>
    </div>

  </div>

</div>
'''

with open('testimonials_section.html', 'w') as f:
    f.write(testimonials_html)
with open('testimonials_section_source.txt', 'w') as f:
    f.write(testimonials_html)

# 6. PRODUCT & INGREDIENTS BREAKDOWN SECTION
ingredients_html = f'''<!-- 
================================================================================
 Elementor HTML Snippet: Reason 4 - Vantacin+ Product Bottle & 5 Ingredients
 Instructions: Copy all code below and paste into an Elementor HTML widget.
================================================================================
-->
<div style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 840px; margin: 0 auto;">
  
  <h2 style="font-size: 1.6rem; font-weight: 800; color: #0f172a; margin: 36px 0 18px 0; line-height: 1.3; padding-bottom: 8px; border-bottom: 2px solid #e2e8f0;">
    REASON 4: INTRODUCING VANTACIN+ HERBAL CAPSULES
  </h2>

  <p style="font-size: 1.08rem; color: #1e293b; line-height: 1.8; margin-bottom: 22px;">
    Manufactured under strict GMP standards by <strong>Varna Services Ltd.</strong> and officially registered with <strong>NAFDAC (Reg. NO: A7-9975L)</strong>, <strong>VANTACIN+ Capsules</strong> is the gold-standard herbal remedy formulated specifically for urinary tract infections (UTIs), sexually transmitted diseases (STDs/STIs), and recurrent viral outbreaks.
  </p>

  <!-- PRODUCT SHOWCASE VISUAL -->
  <div style="background: white; border: 2px solid #e2e8f0; border-radius: 16px; padding: 24px; margin: 28px 0; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.06);">
    <div style="display: flex; justify-content: center; align-items: center; gap: 24px; flex-wrap: wrap;">
      <img src="{vantacin_bottle}" alt="Vantacin+ Capsules Bottle" style="max-width: 220px; height: auto; display: block; border-radius: 8px;">
      <img src="{vantacin_label}" alt="Vantacin+ Front and Back Label" style="max-width: 320px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
    </div>
    <div style="margin-top: 18px; font-size: 0.85rem; font-weight: 700; color: #059669; background: #ecfdf5; display: inline-block; padding: 6px 16px; border-radius: 20px; border: 1px solid #a7f3d0;">
      ✓ NAFDAC REG. NO: A7-9975L • 60 HERBAL CAPSULES PER BOTTLE
    </div>
  </div>

  <!-- THE 5 BOTANICAL INGREDIENTS BREAKDOWN -->
  <div style="display: flex; flex-direction: column; gap: 14px; margin: 24px 0;">
    
    <div style="background: #f8fafc; border-left: 5px solid #059669; padding: 16px 20px; border-radius: 0 10px 10px 0;">
      <h4 style="font-size: 1.05rem; font-weight: 800; color: #065f46; margin-top: 0; margin-bottom: 4px;">
        🌿 1. Acacia Nilotica (Acadia Nilotica Extract)
      </h4>
      <p style="font-size: 0.95rem; color: #334155; margin: 0; line-height: 1.6;">
        A legendary medicinal tree rich in condensed tannins and gallic acids. Clinically shown to dismantle protective bacterial and viral biofilms, tighten delicate mucosal tissue, and halt abnormal vaginal/urethral discharge.
      </p>
    </div>

    <div style="background: #f8fafc; border-left: 5px solid #059669; padding: 16px 20px; border-radius: 0 10px 10px 0;">
      <h4 style="font-size: 1.05rem; font-weight: 800; color: #065f46; margin-top: 0; margin-bottom: 4px;">
        🍵 2. Camellia Sinensis (Standardized EGCG Polyphenols)
      </h4>
      <p style="font-size: 0.95rem; color: #334155; margin: 0; line-height: 1.6;">
        Contains high-potency epigallocatechin gallate, one of nature's most documented viral fusion inhibitors. It binds to viral surface proteins, preventing HSV-1 and HSV-2 from penetrating healthy epithelial cells.
      </p>
    </div>

    <div style="background: #f8fafc; border-left: 5px solid #059669; padding: 16px 20px; border-radius: 0 10px 10px 0;">
      <h4 style="font-size: 1.05rem; font-weight: 800; color: #065f46; margin-top: 0; margin-bottom: 4px;">
        🌶️ 3. Capsicum Frutescens (Micro-Vascular Driver)
      </h4>
      <p style="font-size: 0.95rem; color: #334155; margin: 0; line-height: 1.6;">
        Acts as the formula's bioavailability accelerator. By enhancing pelvic micro-capillary circulation, it drives active phytochemicals deep into dormant nerve pathways and tissues where standard drugs cannot reach.
      </p>
    </div>

    <div style="background: #f8fafc; border-left: 5px solid #059669; padding: 16px 20px; border-radius: 0 10px 10px 0;">
      <h4 style="font-size: 1.05rem; font-weight: 800; color: #065f46; margin-top: 0; margin-bottom: 4px;">
        🌳 4. Hunteria Umbellata (Abeere Extract)
      </h4>
      <p style="font-size: 0.95rem; color: #334155; margin: 0; line-height: 1.6;">
        Revered in ethnomedicine for its potent antibacterial, antifungal, and immune-modulating properties. It aggressively eradicates resistant strains of <em>Staph aureus</em> and sexually transmitted bacterial infections.
      </p>
    </div>

    <div style="background: #f8fafc; border-left: 5px solid #059669; padding: 16px 20px; border-radius: 0 10px 10px 0;">
      <h4 style="font-size: 1.05rem; font-weight: 800; color: #065f46; margin-top: 0; margin-bottom: 4px;">
        🌰 5. Xylopia Aethiopica (African Guinea Pepper)
      </h4>
      <p style="font-size: 0.95rem; color: #334155; margin: 0; line-height: 1.6;">
        Packed with diterpenic acids and essential bioactives that purify the urinary bladder, soothe pelvic inflammatory disease (PID), and flush deep-seated viral debris out of the reproductive tract.
      </p>
    </div>

  </div>

</div>
'''

with open('ingredients_product_section.html', 'w') as f:
    f.write(ingredients_html)
with open('ingredients_product_section_source.txt', 'w') as f:
    f.write(ingredients_html)

# 7. PRICING OFFERS SECTION (UPDATED NAIRA PRICES: 20K, 34K, 40K)
pricing_html = f'''<!-- 
================================================================================
 Elementor HTML Snippet: Vantacin+ 3-Tier Bundle Pricing Section (Naira Prices)
 1 Bottle: ₦20,000 | 2 Bottles: ₦34,000 | 3 Bottles: ₦40,000
 Instructions: Copy all code below and paste into an Elementor HTML widget.
================================================================================
-->
<div id="packages" style="font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 960px; margin: 0 auto; text-align: center; padding: 40px 10px;">
  
  <h2 style="font-size: 2.2rem; font-weight: 800; color: #0f172a; margin-bottom: 12px; line-height: 1.2;">
    CLAIM YOUR DISCOUNTED VANTACIN+ PACKAGE TODAY
  </h2>
  <p style="font-size: 1.05rem; color: #475569; max-width: 640px; margin: 0 auto 32px auto;">
    Herbal Solution for Urinary and Reproductive Health • NAFDAC Reg. NO: A7-9975L. Select your bundle below to place your order with <strong>100% Payment on Delivery</strong>.
  </p>

  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
    
    <!-- 1 Bottle Starter -->
    <div style="background: white; border: 2px solid #e2e8f0; border-radius: 18px; padding: 30px 22px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 15px rgba(0,0,0,0.06);">
      <div>
        <h3 style="font-size: 1.4rem; font-weight: 800; color: #0f172a; margin: 0 0 4px 0;">1 BOTTLE</h3>
        <p style="font-size: 0.88rem; color: #64748b; margin-bottom: 16px;">30-Day Starter Trial</p>
        <div style="text-align: center; margin: 16px 0;">
          <img src="{vantacin_single}" alt="1 Bottle Vantacin+" style="max-height: 150px; object-fit: contain; margin: 0 auto; border-radius: 6px;">
        </div>
        <div style="margin: 16px 0;">
          <div style="font-size: 2.2rem; font-weight: 800; color: #0f172a;">₦20,000</div>
          <div style="font-size: 0.85rem; color: #94a3b8; text-decoration: line-through;">Retail: ₦30,000</div>
          <div style="font-size: 0.85rem; color: #059669; font-weight: 700; margin-top: 4px;">You Save: ₦10,000</div>
        </div>
        <ul style="list-style: none; padding: 0; font-size: 0.88rem; color: #475569; display: flex; flex-direction: column; gap: 8px; text-align: left; margin: 20px 0;">
          <li>✓ 1x Bottle (60 Herbal Capsules)</li>
          <li>✓ NAFDAC Reg. A7-9975L Genuine</li>
          <li>✓ Payment on Delivery Nationwide</li>
          <li>✓ Fast Discreet Delivery</li>
        </ul>
      </div>
      <a href="#order-form-section" style="display: block; width: 100%; text-decoration: none; background: #2563eb; color: white; padding: 16px; font-weight: 800; font-size: 1.05rem; border-radius: 8px; box-sizing: border-box;">
        SELECT 1 BOTTLE (₦20,000) →
      </a>
    </div>

    <!-- 2 Bottles Most Popular -->
    <div style="background: white; border: 2px solid #059669; border-radius: 18px; padding: 30px 22px; display: flex; flex-direction: column; justify-content: space-between; position: relative; box-shadow: 0 10px 30px rgba(5, 150, 105, 0.2); transform: scale(1.02);">
      <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: #059669; color: white; font-size: 0.78rem; font-weight: 800; padding: 5px 18px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap;">
        ⭐ MOST POPULAR — RECOMMENDED
      </div>
      <div>
        <h3 style="font-size: 1.5rem; font-weight: 800; color: #065f46; margin: 8px 0 4px 0;">2 BOTTLES</h3>
        <p style="font-size: 0.88rem; color: #047857; font-weight: 700; margin-bottom: 16px;">60-Day Complete Viral Suppression</p>
        <div style="text-align: center; margin: 16px 0;">
          <img src="{vantacin_dual}" alt="2 Bottles Vantacin+" style="max-height: 150px; object-fit: contain; margin: 0 auto; border-radius: 6px;">
        </div>
        <div style="margin: 16px 0;">
          <div style="font-size: 2.4rem; font-weight: 800; color: #065f46;">₦34,000</div>
          <div style="font-size: 0.88rem; color: #94a3b8; text-decoration: line-through;">Retail: ₦60,000 • ₦17,000/btl</div>
          <div style="font-size: 0.9rem; color: #059669; font-weight: 800; margin-top: 4px;">🔥 You Save: ₦26,000 Today</div>
        </div>
        <ul style="list-style: none; padding: 0; font-size: 0.88rem; color: #334155; display: flex; flex-direction: column; gap: 8px; text-align: left; margin: 20px 0;">
          <li>✓ <strong>2x Bottles (120 Herbal Capsules)</strong></li>
          <li>✓ Deep Mucosal & Nerve Ganglia Clearance</li>
          <li>✓ <strong>FREE Express Delivery Nationwide</strong></li>
          <li>✓ VIP WhatsApp Customer Support</li>
          <li>✓ 60-Day 100% Money-Back Guarantee</li>
        </ul>
      </div>
      <a href="#order-form-section" style="display: block; width: 100%; text-decoration: none; background: linear-gradient(135deg, #059669 0%, #047857 100%); color: white; padding: 16px; font-weight: 800; font-size: 1.1rem; border-radius: 8px; box-sizing: border-box; box-shadow: 0 6px 18px rgba(5, 150, 105, 0.35);">
        SELECT 2 BOTTLES (₦34,000) →
      </a>
    </div>

    <!-- 3 Bottles Eradication (Best Value) -->
    <div style="background: white; border: 2px solid #2563eb; border-radius: 18px; padding: 30px 22px; display: flex; flex-direction: column; justify-content: space-between; position: relative; box-shadow: 0 10px 30px rgba(37, 99, 235, 0.15);">
      <div style="position: absolute; top: -14px; left: 50%; transform: translateX(-50%); background: #2563eb; color: white; font-size: 0.78rem; font-weight: 800; padding: 5px 18px; border-radius: 20px; text-transform: uppercase; letter-spacing: 0.05em; white-space: nowrap;">
        BEST VALUE — COMPLETE RECOVERY
      </div>
      <div>
        <h3 style="font-size: 1.4rem; font-weight: 800; color: #1e3a8a; margin: 8px 0 4px 0;">3 BOTTLES</h3>
        <p style="font-size: 0.88rem; color: #2563eb; font-weight: 700; margin-bottom: 16px;">90-Day Full Systemic Eradication</p>
        <div style="text-align: center; margin: 16px 0;">
          <img src="{vantacin_label}" alt="3 Bottles Vantacin+" style="max-height: 150px; object-fit: contain; margin: 0 auto; border-radius: 6px;">
        </div>
        <div style="margin: 16px 0;">
          <div style="font-size: 2.2rem; font-weight: 800; color: #1e3a8a;">₦40,000</div>
          <div style="font-size: 0.85rem; color: #94a3b8; text-decoration: line-through;">Retail: ₦90,000 • Only ₦13,333/btl</div>
          <div style="font-size: 0.85rem; color: #2563eb; font-weight: 700; margin-top: 4px;">🔥 You Save: ₦50,000!</div>
        </div>
        <ul style="list-style: none; padding: 0; font-size: 0.88rem; color: #475569; display: flex; flex-direction: column; gap: 8px; text-align: left; margin: 20px 0;">
          <li>✓ <strong>3x Bottles (180 Herbal Capsules)</strong></li>
          <li>✓ Permanent Biofilm & Nerve Path Eradication</li>
          <li>✓ <strong>FREE Express Shipping Included</strong></li>
          <li>✓ 60-Day 100% Risk-Free Guarantee</li>
        </ul>
      </div>
      <a href="#order-form-section" style="display: block; width: 100%; text-decoration: none; background: #2563eb; color: white; padding: 16px; font-weight: 800; font-size: 1.05rem; border-radius: 8px; box-sizing: border-box;">
        SELECT 3 BOTTLES (₦40,000) →
      </a>
    </div>

  </div>
</div>
'''

with open('packages_pricing_section.html', 'w') as f:
    f.write(pricing_html)
with open('packages_pricing_section_source.txt', 'w') as f:
    f.write(pricing_html)

# 8. ELEMENTOR SINGLE-FILE HTML BLOCK
with open('index.html', 'r') as f:
    idx_content = f.read()
with open('style.css', 'r') as f:
    css_content = f.read()

elementor_single_html = idx_content.replace(
    '<link rel="stylesheet" href="style.css">',
    f'<style>\n{css_content}\n</style>'
)

with open('elementor_complete_page.html', 'w') as f:
    f.write(elementor_single_html)

# 9. ELEMENTOR TEMPLATE JSON
elementor_template = {
    "version": "0.4",
    "title": "Vantacin+ Herpes & Infection Cleanser Landing Page",
    "type": "page",
    "content": [
        {
            "id": "vantacin_section_main",
            "elType": "section",
            "isInner": False,
            "settings": {},
            "elements": [
                {
                    "id": "vantacin_column_main",
                    "elType": "column",
                    "isInner": False,
                    "settings": {
                        "_column_size": 100
                    },
                    "elements": [
                        {
                            "id": "vantacin_html_widget",
                            "elType": "widget",
                            "isInner": False,
                            "widgetType": "html",
                            "settings": {
                                "html": elementor_single_html
                            }
                        }
                    ]
                }
            ]
        }
    ]
}

with open('elementor_template.json', 'w') as f:
    json.dump(elementor_template, f, indent=2)

# 10. GENERATE FULLY EMBEDDED ELEMENTOR COMPLETE PAGE
embedded_html = elementor_single_html
for f in os.listdir('assets_compressed'):
    if not f.endswith('.jpg'):
        continue
    name_no_ext = f[:-4]
    with open(os.path.join('assets_compressed', f), 'rb') as img_f:
        b64_data = 'data:image/jpeg;base64,' + base64.b64encode(img_f.read()).decode('utf-8')
    patterns = [
        f'assets/{name_no_ext}.jpg',
        f'assets/{name_no_ext}.png',
        f'assets/{name_no_ext}.jpeg'
    ]
    for p in patterns:
        if p in embedded_html:
            embedded_html = embedded_html.replace(p, b64_data)

# Specifically replace hero sad black man
embedded_html = embedded_html.replace('assets/sad_black_man_hero.jpg', hero_img)

with open('elementor_complete_page_embedded.html', 'w') as f:
    f.write(embedded_html)

print("SUCCESS: All modular Elementor snippets and complete templates updated with Naira pricing and sad Black man hero image!")
