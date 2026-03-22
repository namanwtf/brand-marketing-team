# Notion Sync Skill

This skill enables continuous, two-way synchronization between local markdown files and your Notion workspace. It ensures that critical information—such as deliverables, reports, competitive intelligence, and research—is always up-to-date and accessible within Notion.

## Features

- **Automated Sync**: Synchronizes files every 6 hours automatically.
- **On-Demand Sync**: Supports manual triggers for immediate synchronization.
- **Flexible File Tracking**: Configurable to sync specific file patterns to designated Notion databases.
- **Notion as a Second Brain**: Promotes Notion as a central hub for all structured and unstructured data, accessible from any device.

## Scripts

- `scripts/sync.py`: A Python script responsible for reading local markdown files and interacting with the Notion API to create or update pages in the configured databases. This script is designed to be executable and handles the core synchronization logic.

## Usage

Refer to `SKILL.md` for detailed instructions on configuration, tracked files, and the various Notion databases involved. You can trigger a sync automatically, on heartbeat, or manually via specific commands.