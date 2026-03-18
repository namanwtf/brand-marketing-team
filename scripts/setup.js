#!/usr/bin/env node

/**
 * Brand Marketing Team - Interactive Setup
 * 
 * This script creates your brand-context.md file by asking interactive questions
 * Run: npm run setup
 * Or: npx brand-marketing-team setup
 */

const inquirer = require('inquirer');
const fs = require('fs-extra');
const chalk = require('chalk');
const ora = require('ora');
const path = require('path');

console.log(chalk.cyan(`
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🚀 BRAND MARKETING TEAM - Setup                        ║
║                                                          ║
║   Create your AI marketing team in 2 minutes            ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
`));

const questions = [
  // Brand Identity
  {
    type: 'input',
    name: 'brandName',
    message: chalk.yellow('🏢 What is your brand name?'),
    validate: (input) => input.trim() !== '' || 'Brand name is required'
  },
  {
    type: 'input',
    name: 'industry',
    message: chalk.yellow('🏭 What industry are you in?'),
    default: 'Consumer Electronics',
    validate: (input) => input.trim() !== '' || 'Industry is required'
  },
  {
    type: 'input',
    name: 'tagline',
    message: chalk.yellow('✨ What is your brand tagline or slogan?'),
    default: ''
  },
  
  // Target Audience
  {
    type: 'checkbox',
    name: 'audienceAge',
    message: chalk.yellow('👥 What is your target age group?'),
    choices: [
      { name: '18-24 (Gen Z)', value: '18-24' },
      { name: '25-34 (Millennials)', value: '25-34' },
      { name: '35-44 (Gen X)', value: '35-44' },
      { name: '45-54', value: '45-54' },
      { name: '55+', value: '55+' }
    ],
    validate: (answer) => answer.length > 0 || 'Select at least one age group'
  },
  {
    type: 'checkbox',
    name: 'audienceLocation',
    message: chalk.yellow('🌍 What are your key markets?'),
    choices: [
      { name: 'India', value: 'India' },
      { name: 'United States', value: 'USA' },
      { name: 'Europe', value: 'Europe' },
      { name: 'Southeast Asia', value: 'SEA' },
      { name: 'Africa', value: 'Africa' },
      { name: 'Middle East', value: 'ME' },
      { name: 'Latin America', value: 'LATAM' }
    ],
    validate: (answer) => answer.length > 0 || 'Select at least one market'
  },
  {
    type: 'checkbox',
    name: 'audiencePersona',
    message: chalk.yellow('🎯 Which personas describe your audience?'),
    choices: [
      { name: 'Budget-conscious', value: 'budget-conscious' },
      { name: 'Tech enthusiasts', value: 'tech-enthusiasts' },
      { name: 'Gaming enthusiasts', value: 'gaming' },
      { name: 'Professionals/Business', value: 'professionals' },
      { name: 'Students', value: 'students' },
      { name: 'Parents/Families', value: 'families' },
      { name: 'Luxury/Premium seekers', value: 'luxury' }
    ]
  },
  
  // Product Details
  {
    type: 'input',
    name: 'heroProduct',
    message: chalk.yellow('⭐ What is your hero product (flagship/best-seller)?'),
    validate: (input) => input.trim() !== '' || 'Hero product is required'
  },
  {
    type: 'input',
    name: 'priceRange',
    message: chalk.yellow('💰 What is your price range? (e.g., ₹8,000 - ₹35,000)'),
    validate: (input) => input.trim() !== '' || 'Price range is required'
  },
  {
    type: 'checkbox',
    name: 'productCategories',
    message: chalk.yellow('📱 What product categories do you offer?'),
    choices: [
      { name: 'Entry-level/Budget', value: 'entry' },
      { name: 'Mid-range', value: 'mid-range' },
      { name: 'Premium/Flagship', value: 'premium' },
      { name: 'Accessories', value: 'accessories' },
      { name: 'Services', value: 'services' }
    ]
  },
  
  // Brand Positioning
  {
    type: 'input',
    name: 'valueProp',
    message: chalk.yellow('💎 What is your core value proposition?'),
    default: 'Best value for money',
    validate: (input) => input.trim() !== '' || 'Value proposition is required'
  },
  {
    type: 'input',
    name: 'keyDifferentiator',
    message: chalk.yellow('🦄 What makes you different from competitors?'),
    validate: (input) => input.trim() !== '' || 'Differentiator is required'
  },
  {
    type: 'list',
    name: 'brandVoice',
    message: chalk.yellow('🗣️ What is your brand voice?'),
    choices: [
      { name: 'Bold & Energetic', value: 'bold-energetic' },
      { name: 'Professional & Trustworthy', value: 'professional' },
      { name: 'Friendly & Approachable', value: 'friendly' },
      { name: 'Luxury & Premium', value: 'luxury' },
      { name: 'Tech-savvy & Innovative', value: 'tech-savvy' },
      { name: 'Youthful & Fun', value: 'youthful' }
    ]
  },
  
  // Competitors
  {
    type: 'input',
    name: 'competitors',
    message: chalk.yellow('🎯 Who are your main competitors? (comma-separated)'),
    default: 'Samsung, Realme, Vivo',
    validate: (input) => input.trim() !== '' || 'At least one competitor is required'
  },
  
  // Marketing Channels
  {
    type: 'checkbox',
    name: 'primaryChannels',
    message: chalk.yellow('📢 What are your primary marketing channels?'),
    choices: [
      { name: 'Meta Ads (Facebook/Instagram)', value: 'meta-ads' },
      { name: 'Google Ads', value: 'google-ads' },
      { name: 'E-commerce (Amazon, Flipkart)', value: 'ecommerce' },
      { name: 'Instagram Organic', value: 'instagram' },
      { name: 'YouTube', value: 'youtube' },
      { name: 'TikTok/Shorts', value: 'shorts' },
      { name: 'Influencer Partnerships', value: 'influencers' },
      { name: 'Email Marketing', value: 'email' },
      { name: 'SMS/WhatsApp', value: 'messaging' }
    ],
    validate: (answer) => answer.length > 0 || 'Select at least one channel'
  },
  {
    type: 'input',
    name: 'messagingFocus',
    message: chalk.yellow('📝 What are your key messaging pillars? (comma-separated)'),
    default: 'Battery life, Performance, Value for money',
    validate: (input) => input.trim() !== '' || 'Messaging focus is required'
  },
  
  // Setup Options
  {
    type: 'confirm',
    name: 'enableCompetitiveIntel',
    message: chalk.blue('🔍 Enable 24/7 Competitive Intelligence monitoring?'),
    default: true
  },
  {
    type: 'confirm',
    name: 'enablePricingOptimizer',
    message: chalk.blue('💰 Enable Dynamic Pricing Optimizer?'),
    default: true
  },
  {
    type: 'confirm',
    name: 'enableAlerts',
    message: chalk.blue('📱 Enable WhatsApp/Telegram alerts?'),
    default: true
  },
  {
    type: 'list',
    name: 'platform',
    message: chalk.blue('🤖 Which AI platform will you primarily use?'),
    choices: [
      { name: 'OpenClaw (24/7 autonomous)', value: 'openclaw' },
      { name: 'Claude Code (IDE-integrated)', value: 'claude-code' },
      { name: 'Cursor (Code editor)', value: 'cursor' },
      { name: 'Multiple/Not sure yet', value: 'multiple' }
    ]
  }
];

async function setup() {
  try {
    const answers = await inquirer.prompt(questions);
    
    const spinner = ora('Creating your brand context...').start();
    
    // Format competitors as array
    const competitorsArray = answers.competitors.split(',').map(c => c.trim());
    
    // Format messaging pillars as array
    const messagingArray = answers.messagingFocus.split(',').map(m => m.trim());
    
    // Create brand-context.md content
    const brandContext = `---
name: brand-context
description: Core brand details for ${answers.brandName}
author: Brand Marketing Team
version: 1.0.0
last-updated: ${new Date().toISOString().split('T')[0]}
---

# ${answers.brandName} - Brand Context

## 🏢 Brand Identity

- **Brand Name:** ${answers.brandName}
- **Industry:** ${answers.industry}
${answers.tagline ? `- **Tagline:** "${answers.tagline}"` : ''}
- **Price Range:** ${answers.priceRange}

## 👥 Target Audience

- **Age Groups:** ${answers.audienceAge.join(', ')}
- **Key Markets:** ${answers.audienceLocation.join(', ')}
- **Personas:** ${answers.audiencePersona.join(', ') || 'General consumers'}

## 📱 Product Portfolio

- **Hero Product:** ${answers.heroProduct}
- **Categories:** ${answers.productCategories.join(', ') || 'Multiple segments'}

## 🎯 Brand Positioning

- **Value Proposition:** ${answers.valueProp}
- **Key Differentiator:** ${answers.keyDifferentiator}
- **Brand Voice:** ${answers.brandVoice}

## 🎯 Competitors

Primary competitors to monitor:
${competitorsArray.map(c => `- ${c}`).join('\n')}

## 📢 Marketing Strategy

### Primary Channels
${answers.primaryChannels.map(c => `- ${c}`).join('\n')}

### Key Messaging Pillars
${messagingArray.map(m => `- ${m}`).join('\n')}

## 🤖 AI Team Configuration

- **Competitive Intelligence:** ${answers.enableCompetitiveIntel ? '✅ Enabled' : '❌ Disabled'}
- **Pricing Optimizer:** ${answers.enablePricingOptimizer ? '✅ Enabled' : '❌ Disabled'}
- **Alerts:** ${answers.enableAlerts ? '✅ Enabled' : '❌ Disabled'}
- **Primary Platform:** ${answers.platform}

---

## 📝 Notes

This file is read by all marketing skills before executing tasks.
Update this context as your brand evolves.

Last updated: ${new Date().toLocaleDateString()}
`;

    // Write brand-context.md
    await fs.writeFile('brand-context.md', brandContext);
    
    // Create .env template if it doesn't exist
    if (!await fs.pathExists('.env')) {
      const envTemplate = `# Brand Marketing Team - Environment Variables
# Copy this to .env and fill in your values

# Brand Configuration
BRAND_NAME="${answers.brandName}"
BRAND_INDUSTRY="${answers.industry}"

# API Keys (Required for full functionality)
# Get from: https://developers.facebook.com/apps
META_ADS_ACCESS_TOKEN=

# Get from: https://www.twilio.com/console
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
WHATSAPP_RECIPIENT=

# Get from: @BotFather on Telegram
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=

# Alert Preferences
ENABLE_WHATSAPP_ALERTS=${answers.enableAlerts}
ENABLE_TELEGRAM_ALERTS=${answers.enableAlerts}
ALERT_THRESHOLD_PRICE_CHANGE=10

# Monitoring Settings
COMPETITIVE_INTEL_ENABLED=${answers.enableCompetitiveIntel}
PRICING_OPTIMIZER_ENABLED=${answers.enablePricingOptimizer}
DAILY_BRIEF_TIME=07:00
`;
      await fs.writeFile('.env.example', envTemplate);
    }
    
    // Create quick-start script
    const quickStart = `#!/bin/bash
# Brand Marketing Team - Quick Start

echo "🚀 Starting ${answers.brandName} Marketing Team..."

# Check if dependencies are installed
if [ ! -d "node_modules" ]; then
  echo "📦 Installing dependencies..."
  npm install
fi

# Run setup if brand-context.md doesn't exist
if [ ! -f "brand-context.md" ]; then
  echo "⚙️  Running initial setup..."
  npm run setup
fi

# Start monitoring
echo "🔍 Starting competitive intelligence..."
npm run intel:watch &

echo "💰 Starting pricing optimizer..."
npm run pricing:analyze &

echo "✅ Marketing team is now active!"
echo "📊 View dashboard: npm run dashboard"
echo "🛑 Stop team: npm run team:stop"
`;
    await fs.writeFile('start-team.sh', quickStart);
    await fs.chmod('start-team.sh', 0o755);
    
    spinner.succeed('Brand context created successfully!');
    
    console.log(chalk.green(`
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ✅ SETUP COMPLETE!                                     ║
║                                                          ║
║   Your AI Marketing Team is ready for ${answers.brandName}
║                                                          ║
╚══════════════════════════════════════════════════════════╝

📄 Files created:
   • brand-context.md (Your brand details)
   • .env.example (API keys template)
   • start-team.sh (Quick start script)

🚀 Next steps:
   1. Copy .env.example to .env and add your API keys
   2. Run: npm run team:start
   3. Or use individual agents:
      • npm run intel:watch
      • npm run pricing:analyze

📚 Documentation:
   • README.md - Full documentation
   • docs/setup-guide.md - Detailed setup instructions

💬 Need help?
   • Open an issue: https://github.com/@samen namanwtf/brand-marketing-team/issues
   • Join Discord: discord.gg/@samen namanwtf

Happy marketing! 🎉
`));

    // Create platform-specific setup instructions
    if (answers.platform === 'openclaw') {
      console.log(chalk.cyan(`
🔧 OpenClaw Users:
   Add this to your SOUL.md:
   
   I am the marketing agent for ${answers.brandName}.
   Read brand-context.md before every marketing task.
   Use the skills in skills/ directory for specialized tasks.
`));
    } else if (answers.platform === 'claude-code') {
      console.log(chalk.cyan(`
🔧 Claude Code Users:
   The skills are in .claude/skills/ directory.
   Use @skill-name to invoke specific marketing skills.
`));
    }

  } catch (error) {
    console.error(chalk.red('❌ Setup failed:'), error.message);
    process.exit(1);
  }
}

setup();
