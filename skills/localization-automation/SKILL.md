---
name: localization-automation
description: Automates content translation, cultural adaptation, and multi-market campaign scaling.
author: @namanwtf
version: 3.0.0
---

# Localization Automation Skill

## Overview

The `localization-automation` skill enables rapid, culturally-aware expansion into new markets by automating translation, adaptation, and deployment of marketing content across languages and regions. It ensures brand consistency while respecting local cultural nuances, regulatory requirements, and market preferences.

## When to Use

Use this skill when you need to:

-   **Translate marketing content:** Convert website copy, ads, emails, and social posts into multiple languages.
-   **Adapt content culturally:** Modify messaging, imagery, and tone for local cultural contexts.
-   **Launch multi-market campaigns:** Deploy campaigns simultaneously across different countries/regions.
-   **Manage translation workflows:** Organize translators, reviewers, and approval processes.
-   **Ensure regulatory compliance:** Adapt content to meet local advertising and privacy regulations.
-   **Optimize for local SEO:** Adapt keywords and content for regional search engines.
-   **Maintain brand consistency:** Ensure core brand messages translate appropriately across cultures.

**Commands:**

-   `localize translate [content_path] --source [lang] --targets "[lang1,lang2,lang3]"`: Translates content.
-   `localize adapt [content_path] --market "[country/region]" --check cultural_fit`: Adapts content culturally.
-   `localize campaign launch [campaign_name] --markets "[market_list]" --sync [true|false]`: Launches multi-market campaign.
-   `localize review [content_path] --market "[market]"`: Reviews content for cultural appropriateness.
-   `localize seo optimize [content_path] --market "[market]" --keywords "[local_keywords]"`: Optimizes for local search.
-   `localize glossary create [product_name] --languages "[lang_list]"`: Creates translation glossaries.
-   `localize status [campaign_name]`: Checks localization progress across markets.

## Capabilities

-   **AI Translation:** Leverages machine translation with post-editing workflows.
-   **Cultural Adaptation:** Adjusts imagery, colors, symbols, and messaging for local markets.
-   **Transcreation:** Re-creates content to evoke the same emotional response in different cultures.
-   **Local SEO Optimization:** Adapts keywords and metadata for regional search engines.
-   **Regulatory Compliance:** Checks content against local advertising and data privacy laws.
-   **Workflow Management:** Tracks content through translation, review, and approval stages.
-   **Quality Assurance:** Validates translations for accuracy, consistency, and cultural fit.
-   **Multi-market Deployment:** Coordinates simultaneous launches across regions.

## Usage Examples

### Scenario 1: Translate product launch content for multiple markets

```bash
localize translate content/pova6_launch/ --source en --targets "hi,ta,bn,te,mr,gu,kn,ml,pa,ur"
# Agent translates all content files into 10 Indian regional languages
```

### Scenario 2: Adapt campaign creative for specific market

```bash
localize adapt campaigns/pova6_hero_banner.jpg --market "India" --check cultural_fit
# Agent reviews imagery and suggests adaptations for Indian cultural context
```

### Scenario 3: Launch campaign across multiple markets simultaneously

```bash
localize campaign launch "Pova6_Gaming_Edition" --markets "India,Nigeria,Kenya,Philippines,Indonesia" --sync true
# Agent coordinates launch timing and ensures all market content is ready
```

### Scenario 4: Create product terminology glossary

```bash
localize glossary create "Tecno Pova 6" --languages "hi,ta,bn,te,mr"
# Agent creates standardized terminology for product features and specs
```

### Scenario 5: Optimize content for local search

```bash
localize seo optimize content/pova6_product_page.html --market "India" --keywords "best gaming phone under 15000,6000mah battery phone"
# Agent adapts content with local keywords and search intent
```

## Configuration

Localization requires translation settings, cultural guidelines, and market-specific configurations.

-   **`config/market_profiles.json`:** Cultural preferences, regulations, and market characteristics.
-   **`glossaries/*.json`:** Approved terminology for products, features, and brand language.
-   **`style_guides/*.md`:** Tone, voice, and writing guidelines for each language/market.
-   **`translation_memory/*.tmx`:** Previously translated content for consistency.
-   **`workflows/*.json`:** Translation and review workflow definitions.

**Example market profile:**

```json
{
  "market": "India",
  "languages": ["en", "hi", "ta", "bn", "te", "mr", "gu", "kn", "ml", "pa", "ur"],
  "cultural_considerations": {
    "colors": {
      "auspicious": ["red", "orange", "yellow"],
      "avoid": ["black"]
    },
    "imagery": {
      "include_diversity": true,
      "family_focused": true
    },
    "festivals": ["Diwali", "Holi", "Eid", "Christmas"]
  },
  "regulatory": {
    "advertising_standards": "ASCI",
    "data_privacy": "DPDP_Act_2023"
  },
  "local_preferences": {
    "price_sensitivity": "high",
    "battery_importance": "very_high",
    "camera_priority": "selfie_focused"
  }
}
```

## Related Skills

-   **`voice-search-optimizer`**: For voice search optimization in local languages.
-   **`content-calendar`**: To coordinate localized content publishing schedules.
-   **`social-content`**: For culturally-adapted social media content.
-   **`seo-optimizer`**: For technical and content SEO across markets.
-   **`analytics-dashboard`**: To track performance across different markets.
