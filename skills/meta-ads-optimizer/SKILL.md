---
name: meta-ads-optimizer
description: Meta Ads automation with Indian market optimization
author: Brand Marketing Team
version: 2.0.0
requires: brand-context, copywriting, analytics-dashboard
category: paid-ads
---

# 🎯 Meta Ads Optimizer

**Purpose:** Automate Meta Ads campaigns with Indian market optimizations, festival calendar targeting, and Tier-2/3 city focus.

---

## Quick Commands

```bash
@meta-ads-optimizer create campaign "Pova 6 Launch"
@meta-ads-optimizer optimize --roas-target 2.5
@meta-ads-optimizer creative-rotate --fatigue-threshold 1.5
@meta-ads-optimizer scale --budget-increase 20% --if-roas-above 2.0
```

---

## Indian Market Optimizations

### Audience Targeting
- **Tier-2/3 Cities:** Jaipur, Lucknow, Indore, Nagpur, Kochi
- **Age:** 18-34 (gaming focus)
- **Interests:** Mobile gaming, PUBG, Free Fire, esports
- **Languages:** English, Hindi, Hinglish

### Festival Calendar
```yaml
Campaigns:
  - Diwali: Oct-Nov (highest CPM, highest conversion)
  - Holi: Mar (colorful creative themes)
  - IPL: Apr-May (cricket + gaming overlap)
  - Raksha Bandhan: Aug (gift angle)
  - Independence Day: Aug (patriotic themes)
```

### Creative Best Practices
- **Format:** 9:16 vertical video (Stories/Reels)
- **Length:** 15-30 seconds
- **Hook:** First 3 seconds critical
- **Audio:** Trending music or gaming sounds
- **CTA:** "Shop Now" or "Learn More"

---

## Auto-Optimization Rules

```javascript
// Budget Scaling
if (ROAS > 2.5 && Spend > 1000) {
  IncreaseBudget(20%)
}

// Creative Fatigue
if (CTR < 1.0 && Frequency > 3) {
  PauseAd()
  Notify("Creative fatigue detected")
}

// Audience Overlap
if (Overlap > 30%) {
  MergeAdSets()
}
```

---

## Credits

Built for Indian mobile market optimization.
