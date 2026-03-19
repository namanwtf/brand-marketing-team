#!/usr/bin/env node

/**
 * Validate all skills before deployment
 * Ensures every skill meets quality standards
 * 
 * Author: @namanwtf
 */

const fs = require('fs-extra');
const path = require('path');
const chalk = require('chalk');

const skillsDir = path.join(__dirname, '..', 'skills');

const requiredFields = [
  'name',
  'description',
  'author',
  'version'
];

async function validateSkills() {
  console.log(chalk.cyan('🔍 Validating all skills...\n'));
  
  const skills = await fs.readdir(skillsDir);
  let validCount = 0;
  let invalidCount = 0;
  
  for (const skill of skills) {
    const skillPath = path.join(skillsDir, skill);
    const stat = await fs.stat(skillPath);
    
    if (!stat.isDirectory()) continue;
    
    const skillFile = path.join(skillPath, 'SKILL.md');
    
    if (!(await fs.pathExists(skillFile))) {
      console.log(chalk.red(`❌ ${skill}: Missing SKILL.md`));
      invalidCount++;
      continue;
    }
    
    const content = await fs.readFile(skillFile, 'utf8');
    
    // Check for required fields in YAML frontmatter
    const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
    
    if (!frontmatterMatch) {
      console.log(chalk.red(`❌ ${skill}: Missing YAML frontmatter`));
      invalidCount++;
      continue;
    }
    
    const frontmatter = frontmatterMatch[1];
    
    let hasAllFields = true;
    for (const field of requiredFields) {
      if (!frontmatter.includes(`${field}:`)) {
        console.log(chalk.yellow(`⚠️  ${skill}: Missing field "${field}"`));
        hasAllFields = false;
      }
    }
    
    if (hasAllFields) {
      console.log(chalk.green(`✅ ${skill}`));
      validCount++;
    } else {
      invalidCount++;
    }
  }
  
  console.log(chalk.bold('\n📊 Validation Summary:'));
  console.log(chalk.green(`  ✅ Valid: ${validCount}`));
  console.log(chalk.red(`  ❌ Invalid: ${invalidCount}`));
  
  if (invalidCount > 0) {
    console.log(chalk.red('\n❌ Validation failed. Fix issues before deploying.'));
    process.exit(1);
  } else {
    console.log(chalk.green('\n✅ All skills validated successfully!'));
  }
}

validateSkills().catch(console.error);
