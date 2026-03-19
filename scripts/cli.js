#!/usr/bin/env node

/**
 * Brand Marketing Team - Universal CLI
 * One command to setup, deploy, and manage your AI marketing team
 * 
 * Usage:
 *   npx brand-marketing-team init my-brand
 *   npx brand-marketing-team setup --auto
 *   npx brand-marketing-team start
 *   npx brand-marketing-team test --all
 * 
 * Author: @namanwtf
 * Twitter: https://twitter.com/namanwtf
 */

const { program } = require('commander');
const fs = require('fs-extra');
const path = require('path');
const chalk = require('chalk');
const ora = require('ora');
const { spawn } = require('child_process');

program
  .name('brand-marketing-team')
  .description('Deploy a 24/7 AI Marketing Department')
  .version('3.0.0');

// INIT - Create new project
program
  .command('init [project-name]')
  .description('Create new brand marketing project')
  .option('-a, --auto', 'Auto-discover from website')
  .option('-u, --url <url>', 'Website URL for auto-discovery')
  .action(async (projectName, options) => {
    const name = projectName || 'my-brand';
    const spinner = ora(`Creating ${name}...`).start();
    
    try {
      // Create project structure
      await fs.ensureDir(name);
      await fs.ensureDir(path.join(name, 'skills'));
      await fs.ensureDir(path.join(name, 'data'));
      await fs.ensureDir(path.join(name, 'logs'));
      
      // Copy core files
      const coreFiles = ['README.md', 'LICENSE', 'package.json'];
      for (const file of coreFiles) {
        if (await fs.pathExists(file)) {
          await fs.copy(file, path.join(name, file));
        }
      }
      
      // Copy all skills
      await fs.copy('skills', path.join(name, 'skills'));
      
      spinner.succeed(`Created ${name}`);
      
      console.log(chalk.green(`
✅ Project created: ${name}

${options.auto ? '🤖 Running auto-discovery...' : ''}

Next steps:
  cd ${name}
  ${options.auto ? 'npm run setup --auto' : 'npm run setup'}
  npm start

📚 https://github.com/namanwtf/brand-marketing-team
💬 https://discord.gg/namanwtf
`));

    } catch (error) {
      spinner.fail(`Failed: ${error.message}`);
      process.exit(1);
    }
  });

// SETUP - Interactive or auto setup
program
  .command('setup')
  .description('Setup your brand marketing team')
  .option('-a, --auto', 'Auto-discover from website')
  .action(async (options) => {
    console.log(chalk.cyan('⚙️  Setting up...\n'));
    console.log('Running automated setup wizard...');
  });

program.parse(process.argv);
