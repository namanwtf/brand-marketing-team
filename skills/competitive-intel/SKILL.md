---
name: competitive-intel
description: 24/7 competitor monitoring with real-time alerts
author: Brand Marketing Team
version: 2.0.0
requires: brand-context
category: intelligence
---

# 🕵️ Competitive Intelligence Agent

**Purpose:** Monitor competitors 24/7, detect price changes, new launches, and marketing moves. Send instant alerts via WhatsApp/Telegram.

**Improvements over v1.0:**
- ✅ Real-time web scraping (not just manual research)
- ✅ Automatic price history tracking
- ✅ WhatsApp/Telegram integration
- ✅ Smart alerts (only significant changes)
- ✅ Historical trend analysis

---

## When to Use

```bash
# Start 24/7 monitoring
@competitive-intel watch realme samsung vivo

# Check specific competitor
@competitive-intel check realme

# Get daily briefing
@competitive-intel daily-brief

# Set up price alerts
@competitive-intel alert when "samsung m17e" < 13000

# Generate competitor report
@competitive-intel report --weekly
```

---

## Capabilities

### 1. Real-Time Price Monitoring
- Scrapes Flipkart, Amazon, and retailer sites
- Tracks price changes every 30 minutes
- Detects stock availability changes
- Monitors promotional offers

### 2. Launch Detection
- Watches for new product announcements
- Monitors BIS certifications (India)
- Tracks press releases and news
- Detects social media teases

### 3. Smart Alerting
- WhatsApp notifications for major changes
- Telegram alerts for daily summaries
- Email reports for weekly analysis
- Only alerts on significant changes (>5% price drop, new launches)

### 4. Historical Analysis
- Price trend charts
- Seasonal pattern detection
- Competitor response tracking
- Market share estimation

---

## Usage Examples

### Monitor All Competitors
```
User: @competitive-intel watch all
Agent: Starting 24/7 monitoring for:
       • Realme (P4 Lite, Narzo series)
       • Samsung (M-series, A-series)
       • Vivo (T-series, Y-series)
       • Poco (X-series)
       
       Alert settings:
       • Price drop > 10%: Immediate WhatsApp
       • New launch: Immediate WhatsApp
       • Daily summary: Telegram at 7 AM
       • Weekly report: Email every Monday
```

### Check Specific Product
```
User: @competitive-intel check "realme p4 lite"
Agent: 📊 REALME P4 LITE STATUS
       
       Current Price: ₹14,999 (Flipkart)
       Launch Date: March 19, 2025
       Key Specs: 7000mAh, Dimensity 6300
       
       Price History:
       • Mar 19: ₹16,999 (launch)
       • Mar 22: ₹14,999 (current, -12%)
       
       ⚠️ THREAT ANALYSIS:
       • Direct competitor to our Pova 6
       • 7000mAh battery matches our spec
       • ₹1000 cheaper than our current pricing
       
       RECOMMENDED ACTION:
       Consider price match or bundle offer.
```

### Daily Briefing
```
User: @competitive-intel daily-brief
Agent: 🌅 DAILY COMPETITIVE BRIEF - March 23, 2025

       🔴 HIGH PRIORITY:
       • Samsung dropped M17e price to ₹12,999 (-₹1000)
       • Vivo T5x stock running low on Flipkart
       
       🟡 MEDIUM PRIORITY:
       • Realme P4 Lite maintaining ₹14,999
       • Poco X8 Pro launch buzz building
       
       🟢 OPPORTUNITIES:
       • Samsung out of stock on Amazon
       • Realme shipping delays reported
       
       YOUR POSITION:
       • Pova 6: Price competitive, stock available
       • Recommendation: Maintain pricing, push availability messaging
```

---

## Configuration

Add to your `brand-context.md`:

```yaml
competitive-intel:
  competitors:
    - name: "Realme"
      products: ["P4 Lite", "Narzo 70", "12 Pro"]
      priority: "high"
    - name: "Samsung"
      products: ["M17e", "A16", "F06"]
      priority: "high"
    - name: "Vivo"
      products: ["T5x", "Y51", "V40"]
      priority: "medium"
  
  alert-channels:
    whatsapp: true
    telegram: true
    email: false
  
  thresholds:
    price-drop: 10%      # Alert on >10% price drop
    price-increase: 5%   # Alert on >5% price increase
    stock-out: true      # Alert when competitor goes OOS
    new-launch: true     # Alert on new product launches
```

---

## Integration with Other Skills

This skill feeds data to:
- **pricing-optimizer**: Real-time competitor pricing
- **copywriting**: Competitor messaging analysis
- **meta-ads-optimizer**: Competitor ad creative tracking
- **analytics-dashboard**: Competitive benchmarking

---

## Data Sources

- Flipkart.com (price, stock, reviews)
- Amazon.in (price, stock, reviews)
- GSMArena.com (specifications)
- 91mobiles.com (news, launches)
- Smartprix.com (comparisons)
- BIS certification database (new launches)

---

## Architecture

```
┌─────────────────────────────────────────┐
│  Competitive Intelligence Agent          │
├─────────────────────────────────────────┤
│  Scheduler (node-cron)                  │
│  ├─ Every 30 min: Price check          │
│  ├─ Every 6 hours: Launch scan         │
│  └─ Daily 7 AM: Briefing generation    │
├─────────────────────────────────────────┤
│  Scrapers                               │
│  ├─ Flipkart scraper (Puppeteer)       │
│  ├─ Amazon scraper (API + scrape)      │
│  └─ News aggregator (RSS + APIs)       │
├─────────────────────────────────────────┤
│  Alert System                           │
│  ├─ WhatsApp (Twilio)                  │
│  ├─ Telegram (Bot API)                 │
│  └─ Email (SendGrid/SES)               │
├─────────────────────────────────────────┤
│  Database (JSON/CSV)                    │
│  ├─ Price history                      │
│  ├─ Launch timeline                    │
│  └─ Alert log                          │
└─────────────────────────────────────────┘
```

---

## Safety Guardrails

- ✅ **Respect robots.txt** on all sites
- ✅ **Rate limiting**: Max 1 request per minute per site
- ✅ **User-Agent rotation**: Appears as legitimate browser
- ✅ **Data retention**: Only 90 days of history stored locally
- ✅ **Privacy**: No customer data scraped, only public pricing

---

## Credits

Built upon competitive-intel framework by Corey Haines (MIT License).
Enhanced with:
- Real-time scraping capabilities
- WhatsApp/Telegram integration
- Historical price tracking
- Smart alerting system

---

## Related Skills

- **pricing-optimizer**: Uses competitive data for dynamic pricing
- **meta-ads-optimizer**: Tracks competitor ad strategies
- **analytics-dashboard**: Visualizes competitive trends

---

*Part of the Brand Marketing Team framework.*
