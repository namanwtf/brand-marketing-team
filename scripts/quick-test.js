#!/usr/bin/env node

/**
 * Quick Test Validation
 * Checks all skills are properly formatted
 * 
 * Author: @namanwtf
 */

const fs = require('fs');
const path = require('path');

const skillsDir = path.join(__dirname, '..', 'skills');

console.log('🧪 Testing Brand Marketing Team Skills...\n');

const skills = [
  'auto-setup',
  'competitive-intel',
  'pricing-optimizer',
  'copywriting',
  'meta-ads-optimizer',
  'analytics-dashboard',
  'page-cro',
  'email-sequence',
  'social-content',
  'testing-framework',
  'seo-optimizer',
  'influencer-outreach',
  'content-calendar',
  'video-marketing',
  'affiliate-manager',
  'retention-analyzer',
  'viral-loop-designer',
  'market-research',
  'pr-distributor',
  'community-manager'
];

let passed = 0;
let failed = 0;

skills.forEach(skill => {
  const skillPath = path.join(skillsDir, skill, 'SKILL.md');
  
  if (!fs.existsSync(skillPath)) {
    console.log(`❌ ${skill}: Missing SKILL.md`);
    failed++;
    return;
  }
  
  const content = fs.readFileSync(skillPath, 'utf8');
  
  // Check required sections
  const hasName = content.match(/^name:/m);
  const hasDescription = content.match(/^description:/m);
  const hasAuthor = content.match(/^author:/m);
  const hasVersion = content.match(/^version:/m);
  const hasUsage = content.match(/## When to Use|## Usage|## Commands/i);
  
  if (hasName && hasDescription && hasAuthor && hasVersion && hasUsage) {
    console.log(`✅ ${skill}`);
    passed++;
  } else {
    console.log(`⚠️  ${skill}: Missing sections`);
    failed++;
  }
});

console.log(`\n📊 Results:`);
console.log(`✅ Passed: ${passed}`);
console.log(`❌ Failed: ${failed}`);

if (failed === 0) {
  console.log('\n🎉 All skills tested and verified!');
  console.log('Ready to push to GitHub.');
  process.exit(0);
} else {
  console.log('\n⚠️  Some skills need fixes.');
  process.exit(1);
}
