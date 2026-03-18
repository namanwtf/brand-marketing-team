---
name: copywriting
description: Brand-voice copywriting with psychology frameworks
author: Brand Marketing Team
version: 2.0.0
requires: brand-context, marketing-psychology
category: content
---

# 📝 Copywriting Agent

**Purpose:** Create conversion-optimized copy that matches your brand voice and applies proven psychology frameworks. Never write bland copy again.

**Improvements over v1.0:**
- ✅ Brand voice training from brand-context.md
- ✅ Psychology frameworks auto-applied
- ✅ Hinglish support for Indian market
- ₹X,999 pricing psychology
- ✅ Battery/charging focus for mobile brands

---

## When to Use

```bash
# Create homepage copy
@copywriting create homepage

# Write landing page for product launch
@copywriting create landing-page "Pova 7 Launch"

# Optimize existing copy
@copywriting optimize meta-ads --variant B

# Write email sequence
@copywriting email-sequence welcome

# Create social media content
@copywriting social --platform instagram --campaign "Holi Sale"
```

---

## Capabilities

### 1. Brand Voice Training
Automatically reads your `brand-context.md` and adapts:

```yaml
Brand Voice: Bold & Energetic
→ Headlines: Action verbs, power words
→ Tone: Confident, youthful, exciting
→ CTAs: "Claim", "Grab", "Dominate" (not "Buy", "Submit")
```

### 2. Psychology Frameworks Auto-Applied

Every piece of copy includes:

```markdown
## SPECIFICITY PRINCIPLE
❌ "Long battery life"
✅ "7,000mAh battery — 2 days heavy use"

## SOCIAL PROOF
❌ "Trusted by many"
✅ "Join 2M+ gamers who never run out of charge"

## SCARCITY
❌ "Limited time offer"
✅ "Only 500 units at launch price"

## PRICE ANCHORING
❌ "₹15,999"
✅ "Was ₹18,999 | Now ₹15,999 | You save ₹3,000"

## AUTHORITY
❌ "Good camera"
✅ "64MP AI camera with Sony IMX sensor"
```

### 3. Hinglish Support
For Indian Tier-2/3 markets:

```
English: "Game all day without charging"
Hinglish: "Poora din khelo, tension mat lo — battery chalti rahegi!"

English: "Most powerful processor"
Hinglish: "Sabse powerful processor — lag khatam!"
```

### 4. Mobile-Specific Copy
Auto-detects mobile context and emphasizes:
- Battery life (mAh, hours of use)
- Charging speed (Watts, "0-100 in X minutes")
- Display specs (Hz, AMOLED, brightness)
- Gaming performance (FPS, thermal management)
- Camera specs (MP, AI features, night mode)

---

## Configuration

Add to your `brand-context.md`:

```yaml
copywriting:
  voice: "bold-energetic"  # Options: professional, friendly, luxury, tech-savvy
  languages: ["english", "hinglish"]
  
  messaging-pillars:
    - "Battery life"
    - "Gaming performance"
    - "Value for money"
  
  psychology-frameworks:
    - "specificity"
    - "social-proof"
    - "scarcity"
    - "price-anchoring"
    - "authority"
  
  forbidden-words:
    - "cheap"
    - "budget"
    - "entry-level"
  
  preferred-words:
    - "value" (instead of cheap)
    - "premium features" (instead of budget)
    - "smart choice" (instead of entry-level)
```

---

## Usage Examples

### Example 1: Homepage Hero Section
```
User: @copywriting create homepage-hero

Agent: 📝 HOMEPAGE COPY OPTIONS

OPTION 1: Bold & Direct
────────────────────────
**Headline:** Game All Day. Win Every Night.
**Subheadline:** 7,000mAh battery. 120Hz display. Under ₹20,000.
The phone that keeps up with your ambition.
**CTA:** Claim Your Gaming Edge →

Psychology applied:
✅ Action verbs ("Game", "Win", "Claim")
✅ Specifics (7,000mAh, 120Hz, ₹20k)
✅ Outcome-focused ("Win Every Night")

OPTION 2: Challenge-Based
────────────────────────
**Headline:** Your Current Phone Can't Handle This.
**Subheadline:** 7,000mAh. 120Hz. Built for gamers who refuse to lose.
**CTA:** Upgrade to Pova 6 →

OPTION 3: Social Proof
────────────────────────
**Headline:** 2 Million Gamers Made the Switch.
**Subheadline:** Here's why: 7,000mAh battery. 120Hz smoothness. 
Price that makes sense: under ₹20,000.
**CTA:** Join the Movement →

RECOMMENDATION: Option 1 (A/B test with Option 2)
```

### Example 2: Product Page
```
User: @copywriting create product-page pova-6

Agent: 📝 POVA 6 PRODUCT PAGE

HERO SECTION:
**Headline:** Power That Lasts. Performance That Dominates.
**Subheadline:** 
• 7,000mAh battery — 2 days non-stop gaming
• 120Hz AMOLED display — butter-smooth visuals
• Dimensity 7300 — flagship performance under ₹20k

**Price:** ₹15,999
**Launch Offer:** ₹14,999 + Free Gaming Headphones

KEY FEATURES:
🔋 **Battery That Won't Quit**
    7,000mAh capacity. 45W fast charging (0-50% in 25 mins).
    Stream 18 hours. Game 12 hours. No power bank needed.

🎮 **Display Built for Gaming**
    120Hz refresh rate. 360Hz touch sampling. 
    Spot enemies faster. React quicker. Win more.

⚡ **Speed Without Compromise**
    MediaTek Dimensity 7300. 5G ready. 
    Lag-free gaming. Fast downloads. Smooth multitasking.

📸 **Capture Every Moment**
    64MP AI triple camera. Night mode. Portrait mode.
    Your victories deserve to be remembered.

SOCIAL PROOF:
"Best gaming phone under ₹20,000" — TechRadar India
★★★★★ 4.8/5 from 12,847 gamers

CTA: **Grab Yours Now →** (₹14,999 limited offer)
```

### Example 3: Meta Ad Copy
```
User: @copywriting create meta-ad "pova-6-launch"

Agent: 📝 META AD OPTIONS

AD 1: Problem-Solution
──────────────────────
**Primary Text:**
Tired of your phone dying mid-game? 😤

Meet Pova 6 — 7,000mAh battery that lasts 2 days.
120Hz display. Under ₹20,000.

Gamers are switching. Here's why 👇

**Headline:** Game All Day Without Charging
**Description:** 7,000mAh battery | 120Hz display | ₹15,999
**CTA:** Shop Now

AD 2: Social Proof
──────────────────────
**Primary Text:**
2 million gamers made the switch this year.

The reason? Pova 6 delivers:
✅ 7,000mAh battery (2 days use)
✅ 120Hz AMOLED display
✅ Flagship performance under ₹20k

Join them. Limited launch offer live now 🔥

**Headline:** India's Favorite Gaming Phone
**Description:** From ₹15,999 | Free gaming headphones
**CTA:** Claim Offer

AD 3: Urgency
──────────────────────
**Primary Text:**
⚠️ Launch offer ends in 48 hours

Pova 6 at ₹14,999 (₹1,000 off) + Free Gaming Headphones

7,000mAh battery. 120Hz display. Built for gamers.

Don't miss out →

**Headline:** ₹1,000 Off Ends Soon
**Description:** Launch offer + free headphones
**CTA:** Shop Now

RECOMMENDATION: Run all 3. Budget split: 40/40/20
```

### Example 4: Hinglish Copy
```
User: @copywriting create hinglish social-post

Agent: 📝 HINGLISH CONTENT

POST 1: Battery Focus
────────────────────
Battery ka tension? 🤔
POVA 6 le lo — 7,000mAh battery!

✅ Poora din gaming
✅ 2 din tak charge nahi karna padega
✅ Price sirf ₹15,999

Ab bas khelo, charging ki fikar chhodo! 🔥

#POVA6 #GamingPhone #BatteryKing

POST 2: Gaming Performance
────────────────────
Lag se pareshan? 😤

POVA 6 mein hai:
🎮 120Hz display — smooth like butter
⚡ Dimensity 7300 — no lag, only wins
🔋 7,000mAh — game all day

Price: ₹15,999 (₹18,999 se kam!)

Link in bio 👆

POST 3: Value Proposition
────────────────────
₹20,000 ke andar best gaming phone? 🎮

Haan, POVA 6! 💪
• 7,000mAh battery
• 120Hz AMOLED display  
• 64MP camera
• Flagship processor

Sab kuch hai, price bhi kam! 😍
Sirf ₹15,999

Abhi order karo 👇
```

---

## Copywriting Frameworks Applied

### PAS (Problem-Agitate-Solution)
```
**Problem:** Your phone dies mid-game
**Agitate:** You lose the match. Your team hates you. 
           You miss clutch moments.
**Solution:** Pova 6 — 7,000mAh battery. Game all day.
```

### AIDA (Attention-Interest-Desire-Action)
```
**Attention:** Game All Day. Win Every Night.
**Interest:** 7,000mAh battery. 120Hz display. Under ₹20k.
**Desire:** Never miss a clutch moment. Dominate every match.
**Action:** Claim Your Gaming Edge →
```

### FAB (Features-Advantages-Benefits)
```
**Feature:** 7,000mAh battery
**Advantage:** 2 days of heavy use
**Benefit:** Game all weekend without charging
```

---

## Credits

Built upon copywriting framework by Corey Haines (MIT License).
Enhanced with:
- Brand voice auto-training
- Hinglish language support
- Mobile-specific copy patterns
- Indian market psychology
- Automated framework application

---

*Part of the Brand Marketing Team framework.*
