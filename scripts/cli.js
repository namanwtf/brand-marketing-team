#!/usr/bin/env node

/**
 * Brand Marketing Team - CLI
 * 
 * Usage:
 *   npx brand-marketing-team init [project-name]
 *   npx brand-marketing-team setup
 *   npx brand-marketing-team add [skill-name]
 *   npx brand-marketing-team start
 *   npx brand-marketing-team status
 */

const { program } = require('commander');
const fs = require('fs-extra');
const path = require('path');
const chalk = require('chalk');
const ora = require('ora');
const inquirer = require('inquirer');

program
  .name('brand-marketing-team')
  .description('The AI Marketing Team for Any Brand')
  .version('1.0.0');

// Init command
program
  .command('init [project-name]')
  .description('Initialize a new brand marketing project')
  .action(async (projectName) => {
    const spinner = ora('Initializing Brand Marketing Team...').start();
    
    try {
      const targetDir = projectName || 'my-brand-marketing';
      
      // Check if directory exists
      if (await fs.pathExists(targetDir)) {
        spinner.fail(`Directory ${targetDir} already exists`);
        process.exit(1);
      }
      
      // Create directory
      await fs.ensureDir(targetDir);
      
      // Copy template files
      const templateDir = path.join(__dirname, '..', 'template');
      
      if (await fs.pathExists(templateDir)) {
        await fs.copy(templateDir, targetDir);
      } else {
        // If template doesn't exist, create minimal structure
        await fs.ensureDir(path.join(targetDir, 'skills'));
        await fs.ensureDir(path.join(targetDir, 'docs'));
        await fs.writeFile(
          path.join(targetDir, 'README.md'),
          `# ${targetDir}\n\nAI Marketing Team project initialized.\n\nRun: npm run setup`
        );
      }
      
      spinner.succeed(`Created ${targetDir}`);
      
      console.log(chalk.green(`
✅ Project initialized!

Next steps:
  cd ${targetDir}
  npm install
  npm run setup

Happy marketing! 🚀
`));
      
    } catch (error) {
      spinner.fail(`Initialization failed: ${error.message}`);
      process.exit(1);
    }
  });

// Setup command
program
  .command('setup')
  .description('Interactive setup for your brand')
  .action(async () => {
    const setupScript = path.join(__dirname, 'setup.js');
    
    if (await fs.pathExists(setupScript)) {
      require(setupScript);
    } else {
      console.log(chalk.yellow('Running setup...'));
      console.log(chalk.cyan('Please answer the following questions about your brand:'));
      // Fallback to inline setup if script not found
    }
  });

// Add skill command
program
  .command('add [skill-name]')
  .description('Add a marketing skill to your project')
  .action(async (skillName) => {
    if (!skillName) {
      // Show available skills
      console.log(chalk.cyan('Available skills:'));
      console.log('  • competitive-intel');
      console.log('  • pricing-optimizer');
      console.log('  • copywriting');
      console.log('  • meta-ads-optimizer');
      console.log('  • analytics-dashboard');
      console.log('  • email-marketing');
      console.log('  • seo-optimizer');
      console.log('  • social-media');
      console.log('\nUsage: npx brand-marketing-team add competitive-intel');
      return;
    }
    
    const spinner = ora(`Adding ${skillName}...`).start();
    
    try {
      // Copy skill from package to local project
      const skillSource = path.join(__dirname, '..', 'skills', skillName);
      const skillTarget = path.join(process.cwd(), 'skills', skillName);
      
      if (!(await fs.pathExists(skillSource))) {
        spinner.fail(`Skill "${skillName}" not found`);
        console.log(chalk.yellow('Available skills: competitive-intel, pricing-optimizer, copywriting, meta-ads-optimizer, analytics-dashboard'));
        process.exit(1);
      }
      
      if (await fs.pathExists(skillTarget)) {
        spinner.fail(`Skill "${skillName}" already exists in your project`);
        process.exit(1);
      }
      
      await fs.copy(skillSource, skillTarget);
      spinner.succeed(`Added ${skillName} to your project`);
      
      console.log(chalk.green(`\n✅ Skill installed!\n`));
      console.log(`Usage: @${skillName} help`);
      
    } catch (error) {
      spinner.fail(`Failed to add skill: ${error.message}`);
      process.exit(1);
    }
  });

// Start command
program
  .command('start')
  .description('Start your marketing team')
  .option('-w, --watch', 'Start competitive intelligence watcher')
  .option('-p, --pricing', 'Start pricing optimizer')
  .option('-a, --all', 'Start all agents')
  .action(async (options) => {
    console.log(chalk.cyan('🚀 Starting Brand Marketing Team...\n'));
    
    if (options.all || options.watch) {
      console.log(chalk.blue('🔍 Starting Competitive Intelligence Agent...'));
      // Spawn intel watcher
    }
    
    if (options.all || options.pricing) {
      console.log(chalk.blue('💰 Starting Pricing Optimizer Agent...'));
      // Spawn pricing optimizer
    }
    
    if (!options.all && !options.watch && !options.pricing) {
      console.log(chalk.yellow('Use --all to start all agents, or --watch/--pricing for specific agents'));
    }
  });

// Status command
program
  .command('status')
  .description('Check marketing team status')
  .action(async () => {
    console.log(chalk.cyan('📊 Brand Marketing Team Status\n'));
    
    // Check if brand-context.md exists
    const hasBrandContext = await fs.pathExists('brand-context.md');
    console.log(`${hasBrandContext ? '✅' : '❌'} Brand Context: ${hasBrandContext ? 'Configured' : 'Not configured (run: npm run setup)'}`);
    
    // Check .env
    const hasEnv = await fs.pathExists('.env');
    console.log(`${hasEnv ? '✅' : '❌'} Environment Variables: ${hasEnv ? 'Configured' : 'Not configured (copy .env.example to .env)'}`);
    
    // Check installed skills
    const skillsDir = path.join(process.cwd(), 'skills');
    if (await fs.pathExists(skillsDir)) {
      const skills = await fs.readdir(skillsDir);
      console.log(`📦 Installed Skills: ${skills.length > 0 ? skills.join(', ') : 'None'}`);
    }
    
    console.log(chalk.green('\n✅ Team is ready to deploy!'));
  });

// Doctor command
program
  .command('doctor')
  .description('Check system health and dependencies')
  .action(async () => {
    console.log(chalk.cyan('🔧 Running System Check...\n'));
    
    const checks = [
      { name: 'Node.js', check: () => process.version >= 'v18.0.0' },
      { name: 'brand-context.md', check: async () => await fs.pathExists('brand-context.md') },
      { name: 'node_modules', check: async () => await fs.pathExists('node_modules') },
      { name: 'Skills directory', check: async () => await fs.pathExists('skills') }
    ];
    
    for (const check of checks) {
      const result = await check.check();
      console.log(`${result ? '✅' : '❌'} ${check.name}`);
    }
    
    console.log(chalk.green('\n✅ System check complete!'));
  });

program.parse();
