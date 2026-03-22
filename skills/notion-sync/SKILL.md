---
summary: "Provides continuous 2-way synchronization between local markdown files and Notion workspace."
description: "Automates the synchronization of deliverables, reports, competitive intelligence, and research to Notion databases, ensuring data accessibility and structured organization. Syncs every 6 hours or on-demand."
configuration:
  sync_schedule:
    - "Every 6 hours (automated)"
    - "On heartbeat (if enabled)"
    - "Manual trigger: \"sync to notion\""
  files_tracked:
    - {pattern: "deliverables/*.md", destination: "🛠️ Nightly Builds & Projects"}
    - {pattern: "memory/2026*.md", destination: "📅 Daily Reports & Briefings"}
    - {pattern: "deliverables/*intel*.md", destination: "🔍 Competitive Intelligence"}
    - {pattern: "deliverables/*system*.md", destination: "📚 Research & Knowledge Base"}
    - {pattern: "deliverables/*social*.md", destination: "📱 Social Media Content Calendar"}
  notion_databases:
    - "🛠️ Nightly Builds & Projects"
    - "📅 Daily Reports & Briefings"
    - "🔍 Competitive Intelligence"
    - "📚 Research & Knowledge Base"
    - "📱 Social Media Content Calendar"
    - "📝 Tasks & Todos"
usage:
  auto: "Every 6 hours"
  manual: "\"Sync my files to Notion\""
  single_file: "\"Push [filename] to Notion\""
philosophy:
  concept: "Notion = 2nd Mind"
  benefits:
    - "Mobile access anywhere"
    - "Shareable with team"
    - "Searchable history"
    - "Structured databases > messy folders"
created: "March 2, 2026"
sync_interval: "Every 6 hours"
---

# Notion Sync Skill

## Summary
Continuous 2-way sync between local markdown files and Notion workspace. Maintains Notion as the "2nd Mind" — your always-accessible knowledge hub.

## Description
Auto-syncs deliverables, reports, intel, and research to Notion databases every 6 hours or on-demand. Ensures your competitive intelligence is always available in your pocket (Notion mobile app).

## Configuration

### Sync Schedule
- **Every 6 hours** (automated)
- **On heartbeat** (if enabled)
- **Manual trigger**: "sync to notion"

### Files Tracked
- `deliverables/*.md` → 🛠️ Nightly Builds & Projects
- `memory/2026*.md` → 📅 Daily Reports & Briefings
- `deliverables/*intel*.md` → 🔍 Competitive Intelligence
- `deliverables/*system*.md` → 📚 Research & Knowledge Base
- `deliverables/*social*.md` → 📱 Social Media Content Calendar

## Notion Databases
1. **🛠️ Nightly Builds & Projects** — All deliverables
2. **📅 Daily Reports & Briefings** — Daily logs and intel
3. **🔍 Competitive Intelligence** — Trends, threats, analysis
4. **📚 Research & Knowledge Base** — Systems, strategy docs
5. **📱 Social Media Content Calendar** — Content, drafts
6. **📝 Tasks & Todos** — Action items from reports

## Usage
- **Auto**: Every 6 hours
- **Manual**: "Sync my files to Notion"
- **Single file**: "Push [filename] to Notion"

## Philosophy
Notion = **2nd Mind**
- Mobile access anywhere
- Shareable with team
- Searchable history
- Structured databases > messy folders

---

**Created:** March 2, 2026
**Sync Interval:** Every 6 hours
