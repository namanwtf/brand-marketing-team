<div align="center">

# 🚀 Brand Marketing Team

**Deploy a 24/7 AI Marketing Department in 60 seconds**

[![GitHub stars](https://img.shields.io/github/stars/namanwtf/brand-marketing-team?style=social)](https://github.com/namanwtf/brand-marketing-team/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/namanwtf/brand-marketing-team?style=social)](https://github.com/namanwtf/brand-marketing-team/fork)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![npm version](https://img.shields.io/npm/v/brand-marketing-team.svg)](https://www.npmjs.com/package/brand-marketing-team)

</div>

---

## 🎯 What is This?

Brand Marketing Team is an **open-source AI marketing framework** that deploys 10 specialized agents to handle your marketing 24/7. No agency fees. No delays. Just results.

Think of it as hiring a complete marketing department that never sleeps, never takes breaks, and costs $0/month.

---

## ⚡ Quick Start (60 Seconds)

```bash
# Install globally
npm install -g brand-marketing-team

# Or use npx (no install needed)
npx brand-marketing-team init my-brand

# Follow the wizard
cd my-brand
npm run setup
```

That's it. Your AI marketing team is now awake and working.

---

## 🤖 Your 24/7 Marketing Team

| Agent | Role | What It Does |
|-------|------|--------------|
| 🕵️ **Competitive Intel** | Intelligence | Monitors competitors 24/7, tracks prices, detects launches |
| 💰 **Pricing Optimizer** | Strategy | Dynamic pricing based on competitor moves and demand |
| 📝 **Copywriting** | Content | Creates conversion-optimized copy in your brand voice |
| 🎯 **Meta Ads Optimizer** | Paid Ads | Automates Meta Ads campaigns with smart optimization |
| 📊 **Analytics Dashboard** | Reporting | Real-time performance tracking and insights |
| 🔄 **Page CRO** | Conversion | Landing page optimization and A/B testing |
| 📧 **Email Sequences** | Lifecycle | Automated email flows for onboarding and retention |
| 📱 **Social Content** | Social | Platform-optimized content for Instagram, LinkedIn, X |
| 🧪 **Testing Framework** | Quality | Automated testing for all marketing initiatives |
| ⚡ **Auto-Setup** | Onboarding | 60-second brand discovery and configuration |

---

## 🎬 Demo

```bash
# Start the entire marketing team
npm start

# Watch a competitor
@competitive-intel watch competitor-a

# Get pricing recommendation
@pricing-optimizer recommend product-x

# Create homepage copy
@copywriting create homepage

# Launch Meta Ads campaign
@meta-ads-optimizer create campaign "Spring Sale"
```

---

## ✨ Key Features

### 🔥 **Real-Time Competitor Intelligence**
- Monitors competitor prices every 30 minutes
- Detects new product launches instantly
- Sends WhatsApp/Telegram alerts for major changes
- Tracks historical trends and patterns

### 💡 **Dynamic Pricing Optimization**
- Auto-recommends pricing based on competitor moves
- Margin protection guardrails
- A/B testing for price points
- Seasonal calendar integration

### 📝 **Brand-Voice Copywriting**
- Learns your brand voice from your website
- Applies psychology frameworks automatically
- Creates copy for any channel (ads, email, social, web)
- Multi-language support

### 🎯 **Meta Ads Automation**
- Auto-optimizes campaigns for ROAS
- Creative fatigue detection
- Smart budget scaling
- Audience overlap management

### 📱 **Multi-Platform Support**
Works seamlessly across:
- **OpenClaw** (primary)
- **Claude Code** (Anthropic)
- **Cursor** (IDE integration)
- **GitHub Copilot** (code editor)

---

## 📦 Installation

### Option 1: Global Installation
```bash
npm install -g brand-marketing-team
brand-marketing-team init my-brand
cd my-brand
npm run setup
```

### Option 2: npx (No Install)
```bash
npx brand-marketing-team init my-brand
cd my-brand
npm run setup
```

### Option 3: Git Clone
```bash
git clone https://github.com/namanwtf/brand-marketing-team.git
cd brand-marketing-team
npm install
npm run setup
```

---

## 🎮 Usage Examples

### Example 1: Monitor Competitors
```bash
# Start monitoring all competitors
@competitive-intel watch all

# Check specific competitor
@competitive-intel check competitor-a

# Get daily briefing
@competitive-intel daily-brief
```

### Example 2: Optimize Pricing
```bash
# Analyze current pricing
@pricing-optimizer analyze

# Get recommendation for product
@pricing-optimizer recommend product-x

# Enable auto-adjustment
@pricing-optimizer auto-adjust --threshold 5%
```

### Example 3: Create Marketing Copy
```bash
# Create homepage hero
@copywriting create homepage-hero

# Write landing page
@copywriting create landing-page "Product Launch"

# Optimize existing copy
@copywriting optimize meta-ads --variant B
```

### Example 4: Meta Ads Campaign
```bash
# Create campaign
@meta-ads-optimizer create campaign "Summer Sale"

# Optimize performance
@meta-ads-optimizer optimize --roas-target 2.5

# Scale winning ads
@meta-ads-optimizer scale --budget-increase 20%
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│              Brand Marketing Team                        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐  │
│  │ Competitive  │    │   Pricing    │    │  Copy    │  │
│  │ Intelligence │◄──►│  Optimizer   │◄──►│ Writing  │  │
│  └──────────────┘    └──────────────┘    └──────────┘  │
│         │                   │                  │        │
│         ▼                   ▼                  ▼        │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Shared Brand Context                   │  │
│  │         (Learned from your website)              │  │
│  └──────────────────────────────────────────────────┘  │
│         │                   │                  │        │
│         ▼                   ▼                  ▼        │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────┐  │
│  │  Meta Ads    │    │   Analytics  │    │   CRO    │  │
│  │  Optimizer   │◄──►│  Dashboard   │◄──►│  Agent   │  │
│  └──────────────┘    └──────────────┘    └──────────┘  │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
brand-marketing-team/
├── 📁 skills/                    # Marketing agents
│   ├── auto-setup/              # 60-second setup wizard
│   ├── competitive-intel/       # Competitor monitoring
│   ├── pricing-optimizer/       # Dynamic pricing
│   ├── copywriting/             # Brand-voice copy
│   ├── meta-ads-optimizer/      # Meta Ads automation
│   ├── analytics-dashboard/     # Performance tracking
│   ├── page-cro/                # Conversion optimization
│   ├── email-sequence/          # Lifecycle emails
│   ├── social-content/          # Social media content
│   └── testing-framework/       # Quality assurance
├── 📁 scripts/                   # CLI tools
│   ├── cli.js                   # Main CLI entry
│   ├── setup.js                 # Interactive setup
│   └── start-team.js            # Team orchestrator
├── 📄 brand-context.md           # Your brand profile
├── 📄 README.md                  # This file
├── 📄 LICENSE                    # MIT License
└── 📄 package.json               # NPM manifest
```

---

## ⚙️ Configuration

All configuration happens in `brand-context.md`:

```yaml
brand:
  name: "Your Brand"
  website: "https://yourbrand.com"
  industry: "saas"  # saas, ecommerce, mobile, etc.
  
voice:
  tone: "bold-energetic"
  personality: "confident, youthful, exciting"
  
competitors:
  - name: "Competitor A"
    website: "https://competitor-a.com"
    priority: "high"
    
pricing:
  strategy: "value-based"
  min-margin: 15%
  
alerts:
  whatsapp: true
  telegram: true
  email: false
```

---

## 🧪 Testing

```bash
# Run all tests
npm test

# Validate skill structure
npm run validate

# Run unit tests
npm run test:unit

# Run integration tests
npm run test:integration
```

---

## 🛡️ Safety Guardrails

- ✅ **Margin Protection**: Never recommends below minimum margin
- ✅ **Approval Gates**: Major changes require human approval
- ✅ **Rate Limiting**: Respects API limits and robots.txt
- ✅ **Privacy First**: No customer data scraped, only public info
- ✅ **Audit Trail**: All actions logged with rationale

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribute
```bash
# Fork the repo
git clone https://github.com/namanwtf/brand-marketing-team.git
cd brand-marketing-team

# Create branch
git checkout -b feature/amazing-feature

# Make changes and commit
git commit -m "Add amazing feature"

# Push and create PR
git push origin feature/amazing-feature
```

---

## 📈 Roadmap

### Phase 1: Core (✅ Complete)
- [x] 10 marketing agents
- [x] Auto-setup wizard
- [x] Multi-platform support
- [x] Testing framework

### Phase 2: Advanced (In Progress)
- [ ] Predictive analytics
- [ ] Automated creative generation
- [ ] Voice/SMS marketing
- [ ] Advanced A/B testing

### Phase 3: Enterprise (Planned)
- [ ] Multi-brand management
- [ ] Team collaboration
- [ ] Advanced permissions
- [ ] Custom agent creation

---

## 💬 Community

- **Twitter:** [@namanwtf](https://twitter.com/namanwtf)
- **Discord:** [Join our community](https://discord.gg/namanwtf)
- **Issues:** [GitHub Issues](https://github.com/namanwtf/brand-marketing-team/issues)

---

## 📄 License

MIT License - Copyright (c) 2026 @namanwtf

See [LICENSE](LICENSE) for full details.

---

## 🙏 Acknowledgments

Built with love by [Naman](https://twitter.com/namanwtf)

Special thanks to the open-source community for making this possible.

---

<div align="center">

### ⭐ Star this repo if you find it helpful!

**[🚀 Get Started Now](#quick-start-60-seconds)**

</div>
