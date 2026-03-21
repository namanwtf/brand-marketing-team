<div align="center">

# 🚀 Brand Marketing Team

**The World's Largest Open-Source AI Marketing Department**

[![Skills](https://img.shields.io/badge/Skills-30-blue)](https://github.com/namanwtf/brand-marketing-team/tree/main/skills)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/namanwtf/brand-marketing-team?style=social)](https://github.com/namanwtf/brand-marketing-team/stargazers)
[![Author](https://img.shields.io/badge/Author-@namanwtf-orange)](https://twitter.com/namanwtf)

**30 Autonomous Marketing Agents | OpenClaw Native | Universal Framework**

[Installation](#installation) • [Documentation](#documentation) • [Skills](#all-30-skills) • [Contributing](#contributing)

</div>

---

## 📋 Table of Contents

1. [What is This?](#what-is-this)
2. [Installation](#installation)
3. [All 30 Skills](#all-30-skills)
4. [Quick Start](#quick-start)
5. [Documentation](#documentation)
6. [Architecture](#architecture)
7. [Contributing](#contributing)
8. [License & Attribution](#license--attribution)
9. [Changelog](#changelog)
10. [Roadmap](#roadmap)

---

## What is This?

Brand Marketing Team is the **world's most comprehensive open-source AI marketing framework**. It deploys 30 autonomous agents that handle every aspect of marketing—from competitive intelligence to viral growth.

### Key Features

- 🎯 **30 Specialized Agents** - Each masters one marketing discipline
- 🤖 **Autonomous Operation** - Works 24/7 without manual intervention
- ⚡ **OpenClaw Native** - Designed specifically for OpenClaw integration
- 🌐 **Universal** - Works for any brand, any industry, any market
- 🔧 **Auto-Configuration** - Discovers your brand in 60 seconds
- 📱 **Real-Time Alerts** - WhatsApp/Telegram notifications for critical events

---

## Installation

### Option 1: OpenClaw (Recommended - 30 seconds)

```bash
# Install all 30 skills at once
openclaw skills install https://github.com/namanwtf/brand-marketing-team

# Activate
@auto-setup init
```

### Option 2: Git Clone

```bash
git clone https://github.com/namanwtf/brand-marketing-team.git
cd brand-marketing-team
npm install
npm run setup
```

### Option 3: NPM

```bash
npm install -g brand-marketing-team
npx brand-marketing-team init my-brand
```

---

## All 30 Skills

### Core Marketing (10)

| Skill | Command | Purpose |
|-------|---------|---------|
| **auto-setup** | `@auto-setup init` | 60-second brand discovery |
| **competitive-intel** | `@competitive-intel watch` | 24/7 competitor monitoring |
| **pricing-optimizer** | `@pricing-optimizer analyze` | Dynamic pricing recommendations |
| **copywriting** | `@copywriting create` | Brand-voice conversion copy |
| **meta-ads-optimizer** | `@meta-ads-optimizer launch` | Meta Ads automation |
| **analytics-dashboard** | `@analytics-dashboard view` | Performance tracking |
| **page-cro** | `@page-cro optimize` | Landing page optimization |
| **email-sequence** | `@email-sequence create` | Lifecycle email automation |
| **social-content** | `@social-content schedule` | Multi-platform content |
| **testing-framework** | `@testing-framework run` | Quality assurance |

### Advanced Growth (10)

| Skill | Command | Purpose |
|-------|---------|---------|
| **seo-optimizer** | `@seo-optimizer research` | Search ranking optimization |
| **influencer-outreach** | `@influencer-outreach find` | Creator discovery & management |
| **content-calendar** | `@content-calendar plan` | Automated scheduling |
| **video-marketing** | `@video-marketing script` | TikTok/Reels/YouTube content |
| **affiliate-manager** | `@affiliate-manager setup` | Affiliate program automation |
| **retention-analyzer** | `@retention-analyzer risk` | Churn prediction & prevention |
| **viral-loop-designer** | `@viral-loop-designer create` | Referral programs & gamification |
| **market-research** | `@market-research survey` | Customer insights & surveys |
| **pr-distributor** | `@pr-distributor write` | Press releases & media outreach |
| **community-manager** | `@community-manager setup` | Discord/Reddit management |

### AI-Powered (10)

| Skill | Command | Purpose |
|-------|---------|---------|
| **ai-chatbot-builder** | `@ai-chatbot-builder create` | Conversational marketing bots |
| **personalization-engine** | `@personalization-engine setup` | Dynamic content personalization |
| **predictive-analytics** | `@predictive-analytics forecast` | Trend & demand forecasting |
| **voice-search-optimizer** | `@voice-search-optimizer optimize` | Alexa/Siri/Google optimization |
| **webinar-automation** | `@webinar-automation create` | Automated webinar funnels |
| **case-study-generator** | `@case-study-generator create` | Customer success stories |
| **partnership-scout** | `@partnership-scout find` | Strategic partner discovery |
| **crisis-manager** | `@crisis-manager monitor` | Brand reputation protection |
| **localization-automation** | `@localization-automation translate` | Multi-language scaling |
| **lead-scoring** | `@lead-scoring analyze` | AI-powered lead qualification |

---

## Quick Start

### 1. Initialize Your Brand

```bash
@auto-setup init
# Enter your brand website
# AI auto-discovers everything
```

### 2. Start Monitoring Competitors

```bash
@competitive-intel watch all
# Real-time price tracking
# Launch detection
# WhatsApp alerts
```

### 3. Optimize Pricing

```bash
@pricing-optimizer auto-adjust --enable
# Dynamic pricing
# Margin protection
# Smart recommendations
```

### 4. Create Marketing Content

```bash
@copywriting create homepage
@video-marketing script --platform tiktok
@seo-optimizer research keywords
```

---

## Documentation

### Skill Documentation

Each skill includes comprehensive documentation:
- **When to Use** - Command reference
- **Capabilities** - Feature overview
- **Usage Examples** - Real-world scenarios
- **Configuration** - Setup options
- **Related Skills** - Integration points

View skill docs: `/skills/[skill-name]/SKILL.md`

### Architecture

```
Brand Marketing Team
├── Core Layer (10 skills)
│   ├── auto-setup
│   ├── competitive-intel
│   └── ...
├── Advanced Layer (10 skills)
│   ├── seo-optimizer
│   ├── influencer-outreach
│   └── ...
└── AI Layer (10 skills)
    ├── ai-chatbot-builder
    ├── predictive-analytics
    └── ...
```

### Configuration

All configuration happens in `brand-context.md`:

```yaml
brand:
  name: "Your Brand"
  website: "https://yourbrand.com"
  industry: "saas"
  
competitors:
  - name: "Competitor A"
    website: "https://competitor-a.com"
    
alerts:
  whatsapp: true
  telegram: true
```

---

## Architecture

### Multi-Agent System

```
┌─────────────────────────────────────────────────────────┐
│              Brand Marketing Team                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐  │
│  │ Competitive  │◄──►│   Pricing    │◄──►│  Copy    │  │
│  │ Intelligence │    │  Optimizer   │    │ Writing  │  │
│  └──────────────┘    └──────────────┘    └──────────┘  │
│         │                   │                  │        │
│         ▼                   ▼                  ▼        │
│  ┌──────────────────────────────────────────────────┐  │
│  │           Shared Brand Context (YAML)            │  │
│  └──────────────────────────────────────────────────┘  │
│         │                   │                  │        │
│         ▼                   ▼                  ▼        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐  │
│  │  Meta Ads    │◄──►│  Analytics   │◄──►│   CRO    │  │
│  │  Optimizer   │    │  Dashboard   │    │  Agent   │  │
│  └──────────────┘    └──────────────┘    └──────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribute

```bash
# Fork and clone
git clone https://github.com/YOUR_USERNAME/brand-marketing-team.git

# Create branch
git checkout -b feature/amazing-skill

# Make changes
git commit -m "✨ Add amazing skill"

# Push and PR
git push origin feature/amazing-skill
```

---

## License & Attribution

### Apache License 2.0

Copyright 2026 namanwtf

This software is licensed under the **Apache License 2.0**.

**What this means:**
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Sublicense
- ✅ Patent protection included

**Requirements:**
- 📝 **Include License** - Copy of Apache 2.0 license
- 📝 **Include NOTICE** - See [NOTICE](NOTICE) file for attribution requirements
- 📝 **State Changes** - Document any modifications you make

### Attribution

While Apache 2.0 doesn't require it, we appreciate attribution to support the project:

```
Powered by Brand Marketing Team
Created by @namanwtf (https://github.com/namanwtf)
Original: https://github.com/namanwtf/brand-marketing-team
```

**Full License:** [LICENSE](LICENSE)  
**Attribution Notice:** [NOTICE](NOTICE)

---

## Changelog

### v3.0.0 (2026-03-20)
- 🚀 **30 Skills Released** - Complete marketing framework
- ✨ **AI-Powered Layer** - 10 advanced AI agents
- 🔧 **OpenClaw Native** - Full integration
- 📦 **Universal Framework** - Any brand, any market

### v2.0.0 (2026-03-19)
- Added 10 advanced skills
- SEO, influencers, video, PR

### v1.0.0 (2026-03-18)
- Initial 10 core skills
- Basic marketing automation

---

## Roadmap

### Q2 2026
- [ ] 40 total skills
- [ ] Mobile app integration
- [ ] Advanced AI models

### Q3 2026
- [ ] 50 total skills
- [ ] Enterprise features
- [ ] White-label option

### Q4 2026
- [ ] Marketplace for custom skills
- [ ] AI-generated skills
- [ ] Global enterprise adoption

---

## Stats

- ⭐ **Stars:** Growing daily
- 🍴 **Forks:** Active community
- 👁️ **Watchers:** Marketing professionals
- 📦 **Skills:** 30 autonomous agents
- 💾 **Size:** Lightweight & efficient
- 🚀 **Performance:** 24/7 operation

---

## Connect

- **Author:** [@namanwtf](https://twitter.com/namanwtf)
- **GitHub:** [namanwtf](https://github.com/namanwtf)
- **Project:** [brand-marketing-team](https://github.com/namanwtf/brand-marketing-team)

---

<div align="center">

**Built with ❤️ by @namanwtf**

**[⭐ Star This Repo](https://github.com/namanwtf/brand-marketing-team)** • **[🍴 Fork It](https://github.com/namanwtf/brand-marketing-team/fork)** • **[🐛 Report Issues](https://github.com/namanwtf/brand-marketing-team/issues)**

</div>
