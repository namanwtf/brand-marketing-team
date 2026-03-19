---
name: voice-search-optimizer
description: Optimizes content for voice search assistants like Alexa, Siri, and Google Assistant to capture conversational queries.
author: @namanwtf
version: 3.0.0
---

# Voice Search Optimizer Skill

## Overview

The `voice-search-optimizer` skill ensures your brand captures traffic from voice-enabled devices and assistants. It optimizes content for natural, conversational queries (long-tail keywords, question-based searches) that users speak rather than type, improving visibility on Alexa, Siri, Google Assistant, and other voice platforms.

## When to Use

Use this skill when you need to:

-   **Optimize content for voice queries:** Adapt website copy, FAQs, and blog posts for spoken search patterns.
-   **Create conversational FAQ schema:** Implement structured data to help voice assistants answer questions directly from your content.
-   **Target local voice searches:** Optimize for "near me" and location-based voice queries.
-   **Improve featured snippet opportunities:** Structure content to appear as voice-read answers.
-   **Analyze voice search performance:** Track how much traffic comes from voice and which queries drive it.
-   **Develop voice-specific content strategies:** Create content specifically designed for voice assistant responses.

**Commands:**

-   `voice-search analyze [url] --report [brief|detailed]`: Analyzes current voice search readiness of a webpage.
-   `voice-search optimize [content_path] --target [voice_assistant]`: Optimizes content for voice search.
-   `voice-search schema generate --faq "[faq_data_path]"`: Generates structured FAQ schema markup for voice search.
-   `voice-search keywords research --topic "[topic]" --locale [language_code]`: Researches conversational voice search queries.
-   `voice-search local optimize [business_name] --location "[city,country]"`: Optimizes for local voice search visibility.
-   `voice-search track [domain] --period [timeframe]`: Monitors voice search traffic and rankings.

## Capabilities

-   **Conversational Query Analysis:** Identifies long-tail, question-based keywords typical of voice search.
-   **Schema Markup Generation:** Creates FAQPage, HowTo, and Speakable schema for voice assistant compatibility.
-   **Content Restructuring:** Transforms standard text into voice-friendly formats (concise answers, bullet points).
-   **Local SEO Integration:** Optimizes for location-based voice queries and "near me" searches.
-   **Featured Snippet Optimization:** Structures content to capture position zero results read by voice assistants.
-   **Multi-language Voice Support:** Adapts optimization for different languages and regional voice search patterns.
-   **Performance Tracking:** Monitors voice search traffic, query patterns, and conversion rates.

## Usage Examples

### Scenario 1: Optimize a product page for voice search queries

```bash
voice-search analyze https://example.com/products/smartphone-x --report detailed
voice-search optimize content/product_page.html --target "all"
# Agent provides optimized content with conversational FAQ section and schema markup
```

### Scenario 2: Create FAQ schema for common customer questions

```bash
voice-search schema generate --faq "data/customer_faqs.json" --output schema/faq_schema.json
# Agent generates structured data markup ready for implementation
```

### Scenario 3: Research voice search keywords for a new product category

```bash
voice-search keywords research --topic "wireless earbuds battery life" --locale en-US
# Agent returns list of conversational queries like "how long do wireless earbuds last"
```

### Scenario 4: Optimize for local "near me" voice searches

```bash
voice-search local optimize "Tecno Store Delhi" --location "Delhi,India"
# Agent provides local optimization recommendations including Google Business Profile updates
```

## Configuration

Voice search optimization requires understanding conversational patterns and implementing structured data.

-   **`data/faqs.json`:** Frequently asked questions in natural language format.
-   **`schema/*.json`:** Generated structured data markup files.
-   **`content/*`:** Website content files to be optimized.
-   **`config/voice_preferences.json`:** Preferences for specific voice assistants or languages.

**Example FAQ data structure:**

```json
{
  "faqs": [
    {
      "question": "What is the battery life of the Tecno Pova 6?",
      "answer": "The Tecno Pova 6 offers up to 48 hours of battery life with regular usage, thanks to its 6000mAh battery.",
      "category": "product_specs"
    },
    {
      "question": "Where can I buy Tecno phones in Mumbai?",
      "answer": "Tecno phones are available at authorized retailers across Mumbai, including Croma, Reliance Digital, and select mobile stores.",
      "category": "availability"
    }
  ]
}
```

**Generated schema example:**

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is the battery life of the Tecno Pova 6?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The Tecno Pova 6 offers up to 48 hours of battery life with regular usage, thanks to its 6000mAh battery."
      }
    }
  ]
}
```

## Related Skills

-   **`seo-optimizer`**: For broader search engine optimization including traditional typed queries.
-   **`ai-chatbot-builder`**: To ensure consistent conversational experiences across voice and chat interfaces.
-   **`localization-automation`**: For voice search optimization across multiple languages and regions.
-   **`analytics-dashboard`**: To track voice search traffic and performance metrics.
