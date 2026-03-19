# 🤝 Contributing to Brand Marketing Team

Thank you for your interest in contributing! This document provides guidelines for contributing to the world's largest open-source AI marketing framework.

## 🎯 Ways to Contribute

### 1. **Build New Skills**
- Create new marketing agents
- Follow the SKILL.md format
- Test thoroughly before submitting

### 2. **Improve Existing Skills**
- Fix bugs
- Add new capabilities
- Improve documentation

### 3. **Documentation**
- Fix typos
- Clarify instructions
- Add examples

### 4. **Marketing**
- Share on social media
- Write blog posts
- Create tutorials

### 5. **Testing**
- Report bugs
- Test on different platforms
- Verify universal applicability

---

## 📝 Skill Contribution Guidelines

### Skill Structure

Each skill must include:

```markdown
---
name: skill-name
description: Clear description
author: "@yourusername"
version: 3.0.0
requires: [dependency-skills]
category: [core|advanced|ai]
---

# Skill Name

**Purpose:** One-line description

## When to Use

```bash
@skill-name command --option
```

## Capabilities

### 1. Feature Name
- Bullet points
- Of capabilities

## Usage Examples

### Example 1: Scenario
```
User: @skill-name command

Agent: Response format
```

## Configuration

```yaml
skill-name:
  option: value
```

## Related Skills

- [skill1](link)
- [skill2](link)

---

*Part of the Brand Marketing Team framework.*
*Author: @yourusername | Version 3.0.0 | BMTL-1.0 License*
```

### Requirements

1. **Universal Content**
   - No brand-specific examples (use "Product X")
   - No region-specific references
   - Works for any industry

2. **Complete Documentation**
   - Frontmatter with all fields
   - "When to Use" section with commands
   - Minimum 3 usage examples
   - Configuration section
   - Related skills

3. **Testing**
   - Run `node scripts/quick-test.js`
   - Must pass validation
   - No broken links

4. **Original Content**
   - 100% original (no copy-paste)
   - Proper attribution if inspired
   - No copyrighted material

---

## 🚀 Pull Request Process

### 1. Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/brand-marketing-team.git
cd brand-marketing-team
```

### 2. Create Branch

```bash
git checkout -b feature/your-skill-name
# or
git checkout -b fix/skill-improvement
```

### 3. Make Changes

- Edit files
- Test thoroughly
- Update documentation

### 4. Commit

```bash
git add .
git commit -m "✨ Add [skill-name] skill

- Description of changes
- Why this is useful
- Testing performed"
```

### 5. Push & PR

```bash
git push origin feature/your-skill-name
```

Create Pull Request with:
- Clear title
- Description of changes
- Screenshots/examples (if applicable)
- Testing checklist

---

## ✅ PR Checklist

Before submitting:

- [ ] Skill follows format guidelines
- [ ] All tests pass (`npm test`)
- [ ] Documentation is complete
- [ ] Examples are realistic
- [ ] Content is universal (no brand references)
- [ ] License attribution included
- [ ] README updated (if needed)

---

## 🐛 Bug Reports

Use GitHub Issues with template:

```markdown
**Bug Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Environment:**
- OS: [e.g., Ubuntu 20.04]
- Node.js: [e.g., 18.x]
- OpenClaw: [e.g., 1.0.0]
```

---

## 💡 Feature Requests

Use GitHub Discussions:

- Describe the feature
- Explain use case
- Suggest implementation
- Discuss with community

---

## 📜 License & Attribution

By contributing, you agree that your contributions will be licensed under **BMTL-1.0**.

You retain copyright of your contributions but grant usage rights to the project.

---

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in skill documentation

---

## ❓ Questions?

- **General:** GitHub Discussions
- **Bugs:** GitHub Issues
- **Direct:** [@namanwtf](https://twitter.com/namanwtf)

---

Thank you for making Brand Marketing Team better! 🚀
