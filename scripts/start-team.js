#!/usr/bin/env node

/**
 * Brand Marketing Team - Start Script
 * 
 * Orchestrates all marketing agents
 * Run: npm run team:start
 */

const { spawn } = require('child_process');
const chalk = require('chalk');
const fs = require('fs');
const path = require('path');

console.log(chalk.cyan(`
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   🚀 BRAND MARKETING TEAM                                ║
║                                                          ║
║   Starting your AI marketing agents...                  ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
`));

// Check if brand-context.md exists
if (!fs.existsSync('brand-context.md')) {
  console.log(chalk.yellow('⚠️  brand-context.md not found. Running setup first...\n'));
  const setup = spawn('node', ['scripts/setup.js'], {
    stdio: 'inherit',
    shell: true
  });
  setup.on('close', (code) => {
    if (code === 0) {
      console.log(chalk.green('\n✅ Setup complete! Starting agents...\n'));
      startAgents();
    }
  });
} else {
  startAgents();
}

function startAgents() {
  const agents = [];
  
  // Read brand context to check what's enabled
  const brandContext = fs.readFileSync('brand-context.md', 'utf8');
  
  // Check which agents are enabled
  const competitiveIntelEnabled = brandContext.includes('Competitive Intelligence: ✅ Enabled');
  const pricingOptimizerEnabled = brandContext.includes('Pricing Optimizer: ✅ Enabled');
  
  console.log(chalk.blue('🔍 Checking enabled agents...\n'));
  
  if (competitiveIntelEnabled) {
    console.log(chalk.green('✅ Competitive Intelligence Agent: ENABLED'));
    // In real implementation, this would start the actual agent
    // For now, just a placeholder
    console.log(chalk.gray('   → Would start: npm run intel:watch'));
  } else {
    console.log(chalk.gray('❌ Competitive Intelligence Agent: DISABLED'));
  }
  
  if (pricingOptimizerEnabled) {
    console.log(chalk.green('✅ Pricing Optimizer Agent: ENABLED'));
    console.log(chalk.gray('   → Would start: npm run pricing:analyze'));
  } else {
    console.log(chalk.gray('❌ Pricing Optimizer Agent: DISABLED'));
  }
  
  console.log(chalk.cyan(`
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   ✅ AGENTS CONFIGURED                                   ║
║                                                          ║
║   To run agents manually:                               ║
║   • npm run intel:watch                                 ║
║   • npm run pricing:analyze                             ║
║   • npm run copy:create                                 ║
║                                                          ║
║   Or use individual skills:                             ║
║   • @competitive-intel watch all                        ║
║   • @pricing-optimizer analyze                          ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
`));
}
