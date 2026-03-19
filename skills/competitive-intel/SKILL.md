---
name: competitive-intel
description: 24/7 competitor monitoring with real-time alerts
author: "@namanwtf"
version: 3.0.0
requires: brand-context
category: intelligence
---

# 🕵️ Competitive Intelligence Agent

**Purpose:** Monitor competitors 24/7, detect price changes, new launches, and marketing moves. Send instant alerts via WhatsApp/Telegram/Slack.

---

## When to Use

```bash
# Start 24/7 monitoring
@competitive-intel watch competitor-a competitor-b

# Check specific competitor
@competitive-intel check competitor-a

# Get daily briefing
@competitive-intel daily-brief

# Set up price alerts
@competitive-intel alert when "product-x" < 199

# Generate competitor report
@competitive-intel report --weekly
```

---

## Capabilities

### 1. Real-Time Price Monitoring
- Scrapes e-commerce sites and retailer websites
- Tracks price changes every 30 minutes
- Detects stock availability changes
- Monitors promotional offers and discounts

### 2. Launch Detection
- Watches for new product announcements
- Monitors certification databases
- Tracks press releases and news
- Detects social media teases and leaks

### 3. Smart Alerting
- WhatsApp notifications for major changes
- Telegram alerts for daily summaries
- Slack integration for team alerts
- Email reports for weekly analysis
- Only alerts on significant changes (>5% price drop, new launches)

### 4. Historical Analysis
- Price trend charts
- Seasonal pattern detection
- Competitor response tracking
- Market positioning analysis

---

## Usage Examples

### Monitor All Competitors
```
User: @competitive-intel watch all
Agent: Starting 24/7 monitoring for:
       • Competitor A (Product X, Product Y)
       • Competitor B (Product Z)
       • Competitor C (Full range)
       
       Alert settings:
       • Price drop > 10%: Immediate WhatsApp
       • New launch: Immediate WhatsApp
       • Daily summary: Telegram at 7 AM
       • Weekly report: Email every Monday
```

### Check Specific Product
```
User: @competitive-intel check "product-x"
Agent: 📊 PRODUCT-X STATUS
       
       Current Price: $199 (Platform A)
       Launch Date: March 2025
       Key Specs: Feature A, Feature B, Feature C
       
       Price History:
       • Mar 1: $229 (launch)
       • Mar 15: $199 (current, -13%)
       
       ⚠️ THREAT ANALYSIS:
       • Direct competitor to our Product Y
       • Similar feature set
       • $30 cheaper than our current pricing
       
       RECOMMENDED ACTION:
       Consider price match or bundle offer.
```

### Daily Briefing
```
User: @competitive-intel daily-brief
Agent: 🌅 DAILY COMPETITIVE BRIEF - March 20, 2025

       🔴 HIGH PRIORITY:
       • Competitor A dropped Product X price to $179 (-$20)
       • Competitor B stock running low on Platform Y
       
       🟡 MEDIUM PRIORITY:
       • Competitor C maintaining current pricing
       • Competitor D launch buzz building
       
       🟢 OPPORTUNITIES:
       • Competitor A out of stock on Platform B
       • Competitor C shipping delays reported
       
       YOUR POSITION:
       • Product Y: Price competitive, stock available
       • Recommendation: Maintain pricing, push availability messaging
```

---

## Configuration

Add to your `brand-context.md`:

```yaml
competitive-intel:
  competitors:
    - name: "Competitor A"
      products: ["Product X", "Product Y", "Product Z"]
      priority: "high"
      platforms: ["platform-a.com", "platform-b.com"]
    - name: "Competitor B"
      products: ["Product M", "Product N"]
      priority: "medium"
      platforms: ["platform-c.com"]
  
  alert-channels:
    whatsapp: true
    telegram: true
    email: false
    slack: true
  
  thresholds:
    price-drop: 10%      # Alert on >10% price drop
    price-increase: 5%   # Alert on >5% price increase
    stock-out: true      # Alert when competitor goes OOS
    new-launch: true     # Alert on new product launches
  
  monitoring:
    frequency: "30min"   # Check every 30 minutes
    sources: ["ecommerce", "news", "social", "certifications"]
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

- E-commerce platforms (price, stock, reviews)
- News aggregators (RSS + APIs)
- Social media monitoring
- Certification databases
- Press release trackers

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
│  ├─ E-commerce scrapers (Puppeteer)    │
│  ├─ News aggregators (RSS + APIs)      │
│  └─ Social media monitors              │
├─────────────────────────────────────────┤
│  Alert System                           │
│  ├─ WhatsApp (Twilio)                  │
│  ├─ Telegram (Bot API)                 │
│  ├─ Slack (Webhooks)                   │
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

## Related Skills

- **pricing-optimizer**: Uses competitive data for dynamic pricing
- **meta-ads-optimizer**: Tracks competitor ad strategies
- **analytics-dashboard**: Visualizes competitive trends

---

*Part of the Brand Marketing Team framework.*
*Author: @namanwtf | Version 3.0.0 | MIT License*
