---
summary: "Automated competitive intelligence for the Indian smartphone market focusing on the under ₹30k segment."
description: "Tracks Google Trends, performs anomaly detection, and generates daily competitive reports for Tecno/Pova against key competitors like Samsung, Vivo, Motorola, Infinix, Realme, and Redmi. Emphasizes products under ₹30,000."
requirements:
  - Brave Search API
  - Browser CLI for Google Trends
  - Telegram/Discord for alerts
configuration:
  keywords_tracked:
    tecno: ["tecno pova curve 2", "tecno pova 7", "tecno pova 7 pro", "tecno pova slim", "tecno spark go 3", "tecno spark go 5g", "tecno camon 30 series"]
    primary_competitors: ["samsung galaxy a35", "samsung galaxy a55", "samsung galaxy m series", "vivo t3", "vivo v series", "vivo y under-30k", "vivo v30e", "vivo v29e"]
    secondary_competitors: ["motorola edge 50", "motorola edge 70 fusion", "infinix gt 30", "infinix note 50s", "infinix note edge"]
    tracked_for_learning: ["realme 12 series", "realme 13 series", "redmi note 13 series", "poco x6", "poco m6", "oppo a79", "oppo a58"]
  geographic_focus: "India (geo=IN)"
  price_threshold: "under ₹30,000"
  windows: ["7-day", "12-month", "5-year"]
  anomaly_thresholds:
    spike_critical: 80
    critical_drop: -50
    notify_immediately: true
    silent_if_normal: true
usage:
  hourly_check: "Check 7-day trends for all keywords; alert if >50% spike or >30% drop on any under-30k product."
  daily_report: "Generate full analysis focusing on under-30k products."
  manual_deep_dive: "Analyze specific competitor patterns (e.g., Samsung A-series, M-series)."
outputs:
  hourly: "Anomaly alerts with cause, threat level, and suggested action."
  daily: "Comprehensive report with brand rankings, under-₹30k threats, tracked learnings, and recommended actions."
intelligence_priorities:
  primary: "Samsung (A-series, M-series), Vivo (T-series, V-series)"
  secondary: "Motorola (Edge 50/70 Fusion), Infinix (GT 30, Note 50s, Note Edge)"
  tracked: "Realme (12/13 series), Redmi (Note 13 series), Poco (X6/M6)"
  ignore: "OnePlus, iPhone, Pixel (unless dropping under ₹30k)"
file_management:
  input: ["MEMORY.md", "Google Trends data", "Web search results"]
  output: ["memory/2026-MM-DD-competitive-intel.md", "deliverables/competitive-intel-report-YYYYMMDD.md"]
corrections:
  products_status:
    pova_curve_2: {status: "LIVE", price: "₹27,999-29,999", priority: "PRIMARY (defend)"}
    pova_7_series: {status: "Live", price: "₹30k+", priority: "Secondary"}
    infinix_gt_30: {status: "IN MARKET", price: "₹24,999", priority: "PRIMARY (threat)"}
    samsung_a35_a55: {status: "Live", price: "₹27,999-30k+", priority: "PRIMARY (threat)"}
    vivo_t3: {status: "Launching", price: "₹29,999", priority: "PRIMARY (threat)"}
    motorola_edge_70: {status: "Launching Mar", price: "₹30k expected", priority: "Track if undercuts"}
  competitive_reality: "Curve 2 and GT 30 are active in the market. Real competition is Samsung + Vivo. Focus on defending/attacking under ₹30k, learning from all."
sub_agent_instructions:
  checking_trends:
    - "Flag immediately any Samsung/Vivo under-30k spike."
    - "Analyze why it moved (launch, price cut, campaign)."
    - "Compare how it threatens Tecno under-30k position."
    - "Learn what pricing/campaign tactics work."
  output_format: "🚨 THREAT: [Brand] [Product] @ ₹[Price] — [Why moving]; 📈 LEARNING: [Bigger brand] [Strategy] — applicable to Tecno?; 💡 ACTION: What N should do now"
created: "March 2, 2026"
owner: "N's Competitive Intelligence System"
focus: "Under ₹30k threats | Track all for learning"
---

# Competitive Intelligence Agent

## Summary
Automated competitive trend analysis for Tecno/Pova vs all brands (Vivo, Samsung, Motorola, Infinix, Realme, Redmi) in Indian smartphone market. **Primary focus: Under ₹30k segment where Tecno competes.** Tracks Google Trends across 7-day, 12-month, and 5-year windows.

## Description
This agent performs systematic competitive intelligence gathering:
- **Primary targets**: Samsung, Vivo (big players in under-₹30k)
- **Secondary threats**: Motorola, Infinix (under ₹30k)
- **Track all**: Realme, Redmi, Oppo (learning + pattern recognition)
- **Tecno products**: Pova Curve 2 (LIVE), Pova 7, Spark Go, future launches

## Requirements
- Brave Search API
- Browser CLI for Google Trends
- Telegram/Discord for alerts

## Configuration

### Keywords Tracked (Updated March 2, 2026)

**Tecno (LIVE Products):**
- tecno pova curve 2 (⚠️ **ALREADY LAUNCHED** under ₹30k)
- tecno pova 7 / pova 7 pro
- tecno pova slim
- tecno spark go 3 / spark go 5g
- tecno camon 30 series

**Primary Competitors (Under ₹30k FOCUS):**
- samsung galaxy a35 / a55 / m series
- vivo t3 / v series / y under-30k
- vivo v30e / v29e (if under 30k)

**Secondary Competitors (Under ₹30k threats):**
- motorola edge 50 / edge 70 fusion
- infinix gt 30 (⚠️ **IN MARKET**)
- infinix note 50s
- infinix note edge

**Tracked for Learning:**
- realme 12 series / 13 series
- redmi note 13 series
- poco x6 / m6
- oppo a79 / a58

### Geographic Focus
India only (geo=IN)

### Price Threshold
**Primary**: Products & launches under **₹30,000**
(Track above-30k only for learning, flag threats only when under-30k)

### Windows
- **7-day**: Hourly anomaly detection
- **12-month**: Daily trend analysis  
- **5-year**: Weekly strategic context

### Anomaly Thresholds
```yaml
spike_critical: 80
critical_drop: -50
notify_immediately: true
silent_if_normal: true
```

## Usage

### Hourly Check (Automated)
```
Check: 7-day trends for all keywords
Alert if: >50% spike, >30% drop on any under-30k product
```

### Daily Report
```
Session message: "Daily competitive intel report"
Agent responds with full analysis focusing under-30k
```

### Manual Deep Dive
```
Session message: "Deep dive into Samsung under-30k trends"
Agent analyzes Samsung A-series, M-series patterns
```

## Outputs

### Hourly (Anomaly Only)
```
🚨 ANOMALY: Samsung A35 searches spiked +60%
Cause: Price drop to ₹27,999 on Flipkart
Threat Level: 🔴 HIGH (direct Curve 2 competitor)
Action: Monitor if sustained, prep comparison content
```

### Daily (Comprehensive)
```
# Competitive Intelligence Report — Under ₹30k Focus
## Brand Rankings (7-day)
1. Samsung: 89 (+12%) ← A-series price cuts
2. Vivo: 67 (+5%) ← T3 buzz
3. Motorola: 74 (stable)
4. Infinix: 50 (+8%) ← GT 30 marketing
5. Tecno: 30 (+3%) ← Curve 2 sustaining

## Under-₹30k Threats This Week
- Samsung A35 @ ₹27,999 (was ₹30k+) — curve 2 competitor
- Vivo T3 launch @ ₹29,999 — gaming focus
- Infinix GT 30 @ ₹24,999 — gaming undercuts

## Tracked for Learning
- iPhone SE (above 30k, pattern only)
- OnePlus Nord (above 30k, but pricing strategy learnable)
- Realme 13 series (under 30k, secondary threat)

## Recommended Actions
1. Push Curve 2 "8000mAh vs 5000mAh" vs Samsung A35
2. Watch Vivo T3 gaming reviews — capture GT 30 comparison angle
3. Monitor if A35 price cut is sustained or flash sale
```

## Intelligence Priorities

### 🔴 PRIMARY (Immediate Threats Under ₹30k)
| Brand | Focus | Why |
|-------|-------|-----|
| **Samsung** | A-series (A35, A55), M-series | Biggest volume player |
| **Vivo** | T-series (T3), V-series (V29e, V30e) | Strong offline + youth |

### 🟡 SECONDARY (Direct Competitors)
| Brand | Focus | Why |
|-------|-------|-----|
| **Motorola** | Edge 50/70 Fusion | Growing under-30k presence |
| **Infinix** | GT 30, Note 50s, Note Edge | Aggressive pricing |

### 🟢 TRACKED (Pattern Learning)
| Brand | Focus | Why |
|-------|-------|-----|
| **Realme** | 12 series, 13 series | Pricing strategies |
| **Redmi** | Note 13 series | Market share shifts |
| **Poco** | X6, M6 | Performance positioning |

### ⚪ IGNORE (Unless Dropping Under 30k)
- OnePlus (Nord series if above 30k)
- iPhone (pattern learning only)
- Pixel (niche)

## File Management

### Input
- MEMORY.md (corrected competitor hierarchy)
- Google Trends data
- Web search results

### Output
- `memory/2026-MM-DD-competitive-intel.md`
- `deliverables/competitive-intel-report-YYYYMMDD.md`

## Key Corrections (March 2, 2026)

### Products Status (UPDATED)
| Product | Status | Price | Intelligence Priority |
|---------|--------|-------|----------------------|
| Pova Curve 2 | **LIVE** | ₹27,999-29,999 | **PRIMARY** (defend) |
| Pova 7 series | Live | ₹30k+ | Secondary |
| Infinix GT 30 | **IN MARKET** | ₹24,999 | **PRIMARY** (threat) |
| Samsung A35/A55 | Live | ₹27,999-30k+ | **PRIMARY** (threat) |
| Vivo T3 | Launching | ₹29,999 | **PRIMARY** (threat) |
| Motorola Edge 70 | Launching Mar | ₹30k expected | Track if undercuts |

### Competitive Reality
- **Curve 2**: Already competing in market (not pre-launch)
- **GT 30**: Active in market, marketing now
- **Real competition**: Samsung + Vivo (volume + brand power)
- **Focus**: Defend/attack under ₹30k, learn from all

## Sub-Agent Instructions

### When Checking Trends:
1. **Flag immediately**: Any Samsung/Vivo under-30k spike
2. **Analyze**: Why it moved (launch, price cut, campaign)
3. **Compare**: How it threatens Tecno under-30k position
4. **Learn**: What pricing/campaign tactics work (even above 30k)

### Output Format:
```
🚨 THREAT: [Brand] [Product] @ ₹[Price] — [Why moving]
📈 LEARNING: [Bigger brand] [Strategy] — applicable to Tecno?
💡 ACTION: What N should do now
```

---

**Created:** March 2, 2026
**Owner:** N's Competitive Intelligence System
**Focus:** Under ₹30k threats | Track all for learning
