---
name: pricing-optimizer
description: Dynamic pricing based on competitor moves and market conditions
author: Brand Marketing Team
version: 2.0.0
requires: brand-context, competitive-intel
category: strategy
---

# 💰 Pricing Optimizer Agent

**Purpose:** Automatically optimize pricing based on competitor moves, demand signals, and margin protection rules. Never leave money on the table.

**Improvements over v1.0:**
- ✅ Real-time competitor price integration
- ✅ Dynamic pricing recommendations
- ✅ Margin protection guardrails
- ✅ A/B test pricing strategies
- ✅ Festival/promotion calendar integration

---

## When to Use

```bash
# Analyze current pricing vs competitors
@pricing-optimizer analyze

# Get pricing recommendation for specific product
@pricing-optimizer recommend pova-6

# Set up auto-adjustment with thresholds
@pricing-optimizer auto-adjust --threshold 5%

# Simulate price change impact
@pricing-optimizer simulate --product pova-6 --price 14999

# Generate pricing strategy report
@pricing-optimizer report --weekly
```

---

## Capabilities

### 1. Competitor-Based Pricing
- Monitors competitor prices in real-time
- Calculates price gaps and positioning
- Suggests optimal price points
- Tracks price elasticity

### 2. Margin Protection
- Never recommends below minimum margin
- Accounts for COGS, shipping, taxes
- Cash flow aware pricing
- Promotional budget integration

### 3. Smart Recommendations
```
SCENARIO: Realme P4 Lite drops to ₹14,999

ANALYSIS:
• Your Pova 6: ₹15,999
• Price gap: ₹1,000 (6.7% higher)
• Competitor: 7,000mAh battery
• Your advantage: 120Hz vs 90Hz display

RECOMMENDATIONS:
1. MATCH: ₹14,999 (aggressive, -6.7% margin)
   → Risk: Price war
   → Reward: Maintain market share

2. BUNDLE: ₹15,999 + free gaming accessories
   → Maintain price, add value
   → Perceived value increase: ₹1,500

3. DIFFERENTIATE: ₹15,499 (match halfway)
   → Highlight 120Hz advantage
   → Target spec-conscious buyers

OPTIMAL CHOICE: Option 2 (Bundle Strategy)
Confidence: 78%
Expected impact: +12% conversions, -3% margin
```

### 4. Festival Calendar Integration
```
UPCOMING: Holi Sale (March 25)

PRICING STRATEGY:
• Pre-sale (Now-Mar 24): Maintain ₹15,999
• Sale (Mar 25-28): Flash price ₹13,999
• Post-sale (Mar 29+): ₹15,499 (new normal)

MARGIN IMPACT:
• Pre-sale: 22% margin
• Sale: 8% margin (volume play)
• Post-sale: 18% margin (new baseline)
```

### 5. A/B Test Pricing
```bash
@pricing-optimizer ab-test --product pova-6

SETUP:
• Variant A: ₹15,999 (current)
• Variant B: ₹15,499 (test)
• Duration: 14 days
• Traffic split: 50/50

SUCCESS METRICS:
• Primary: Revenue per visitor
• Secondary: Conversion rate, margin

AUTO-ROLLBACK if:
• Revenue drops >15%
• Margin drops below 12%
```

---

## Configuration

Add to your `brand-context.md`:

```yaml
pricing-optimizer:
  products:
    - name: "Pova 6"
      current-price: 15999
      min-margin: 15%
      cogs: 8500
      competitors: ["realme-p4-lite", "samsung-m17e"]
    
  strategy:
    type: "value-based"  # Options: penetration, skimming, value-based
    aggression: "medium"  # Options: conservative, medium, aggressive
    
  guardrails:
    min-margin: 12%
    max-discount: 20%
    price-match: true
    bundle-preference: true
    
  calendar:
    festivals:
      - name: "Holi Sale"
        date: "2025-03-25"
        discount: 15%
      - name: "Amazon Prime Day"
        date: "2025-07-15"
        discount: 20%
```

---

## Usage Examples

### Scenario 1: Competitor Price Drop
```
User: @pricing-optimizer alert "realme dropped p4 lite price"

Agent: 🚨 PRICING ALERT

COMPETITOR MOVE:
• Realme P4 Lite: ₹14,999 (was ₹16,999)
• Drop: ₹2,000 (-11.8%)
• Your position: ₹2,000 premium

OPTIONS ANALYSIS:
┌─────────────┬────────────┬───────────┬──────────┐
│ Strategy    │ New Price  │ Margin    │ Impact   │
├─────────────┼────────────┼───────────┼──────────┤
│ Match       │ ₹14,999    │ 12%       │ High vol │
│ Undercut    │ ₹14,499    │ 8%        │ Max vol  │
│ Bundle      │ ₹15,999    │ 20%       │ Brand    │
│ Ignore      │ ₹15,999    │ 22%       │ Risky    │
└─────────────┴────────────┴───────────┴──────────┘

RECOMMENDATION: Bundle Strategy
• Price: ₹15,999
• Add: Gaming headphone (₹999 value)
• Effective discount: 6.3%
• Margin: 18%

Execute? [Yes/No/Adjust]
```

### Scenario 2: New Product Launch
```
User: @pricing-optimizer launch pova-7

Agent: 📊 LAUNCH PRICING ANALYSIS

MARKET RESEARCH:
• Samsung M17e: ₹13,999 (4GB+128GB)
• Realme P4 Lite: ₹14,999 (6GB+128GB)
• Vivo T5x: ₹18,999 (6GB+128GB)

POSITIONING OPTIONS:
1. AGGRESSIVE: ₹13,999 (undercut Samsung)
   → Market share focus
   → Margin: 10%
   
2. VALUE: ₹15,499 (between Realme & Vivo)
   → Balanced approach
   → Margin: 18%
   → Highlight: 7,500mAh battery
   
3. PREMIUM: ₹16,999 (Vivo alternative)
   → Feature superiority
   → Margin: 24%
   → Requires: 120Hz AMOLED

RECOMMENDATION: Option 2 (₹15,499)
• Sweet spot in market
• Defensible with specs
• 18% margin sustainable

Launch price: ₹15,499
Intro offer: ₹14,999 (first week)
```

### Scenario 3: Dynamic Adjustment
```
User: @pricing-optimizer auto-adjust --enable

Agent: ⚙️ AUTO-ADJUSTMENT ENABLED

RULES CONFIGURED:
• Monitor: Realme, Samsung, Vivo prices (every 30 min)
• Trigger: Competitor drops >10%
• Action: Recommend response within 1 hour
• Limits: Never below 12% margin

NOTIFICATIONS:
• WhatsApp: Price alerts
• Email: Daily pricing summary
• Dashboard: Real-time price positioning

GUARDRAILS ACTIVE:
✅ Minimum margin: 12%
✅ Maximum discount: 20%
✅ Price match: Enabled
✅ Bundle preference: Enabled

Your pricing is now on autopilot (with approval gates).
```

---

## Integration with Other Skills

**Inputs from:**
- `competitive-intel`: Real-time competitor prices
- `analytics-dashboard`: Conversion data, demand signals
- `marketing-psychology`: Pricing psychology frameworks

**Outputs to:**
- `meta-ads-optimizer`: Adjust ad bids based on pricing
- `copywriting`: Price messaging in ads
- `launch-strategy`: Launch pricing recommendations

---

## Safety Guardrails

- ✅ **Margin protection**: Never below configured minimum
- ✅ **Approval gates**: Major changes require human approval
- ✅ **A/B testing**: Validate before full rollout
- ✅ **Rollback**: One-click revert to previous pricing
- ✅ **Audit trail**: All price changes logged with rationale

---

## Credits

Built upon pricing-strategy framework by Corey Haines (MIT License).
Enhanced with:
- Real-time competitor integration
- Dynamic auto-adjustment
- Margin protection system
- Festival calendar integration
- A/B testing framework

---

*Part of the Brand Marketing Team framework.*
