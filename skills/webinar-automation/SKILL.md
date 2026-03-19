---
name: webinar-automation
description: Creates and manages automated webinar funnels from registration to follow-up sequences.
author: @namanwtf
version: 3.0.0
---

# Webinar Automation Skill

## Overview

The `webinar-automation` skill streamlines the entire webinar lifecycle—from promotion and registration to live delivery and post-event follow-up. It creates automated funnels that maximize attendance, engagement, and conversion, whether running live webinars, automated replays, or hybrid events.

## When to Use

Use this skill when you need to:

-   **Create webinar funnels:** Design end-to-end automated sequences for webinar promotion and follow-up.
-   **Automate registration workflows:** Set up registration pages, confirmation emails, and reminder sequences.
-   **Manage attendee communications:** Automate pre-webinar reminders and post-webinar nurture sequences.
-   **Generate webinar content:** Create scripts, slide decks, and promotional materials.
-   **Track webinar metrics:** Monitor registration rates, attendance, engagement, and conversions.
-   **Set up evergreen webinars:** Create automated replay funnels that run continuously.
-   **Integrate with marketing stack:** Connect webinars to CRM, email platforms, and analytics tools.

**Commands:**

-   `webinar create [webinar_name] --type [live|automated|hybrid] --topic "[topic]"`: Creates a new webinar project.
-   `webinar funnel setup [webinar_name] --stages "[registration,reminder,followup]"`: Sets up the automated funnel.
-   `webinar content generate [webinar_name] --format "[script|slides|emails]"`: Generates webinar content.
-   `webinar promote [webinar_name] --channels "[email,social,ads]"`: Launches promotional campaigns.
-   `webinar monitor [webinar_name] --metrics "[registrations,attendance,engagement]"`: Tracks webinar performance.
-   `webinar replay setup [webinar_name] --automation "[evergreen|scheduled]"`: Configures replay automation.

## Capabilities

-   **Funnel Design:** Creates multi-stage funnels with registration, reminder, live event, and follow-up sequences.
-   **Landing Page Generation:** Builds optimized registration pages with conversion-focused copy.
-   **Email Sequence Automation:** Sets up behavioral email triggers based on registration, attendance, and engagement.
-   **Content Creation:** Generates webinar scripts, slide outlines, and promotional copy.
-   **Attendee Segmentation:** Segments audiences based on behavior (registered, attended, dropped off, engaged).
-   **Evergreen Automation:** Configures automated replay systems for continuous lead generation.
-   **Integration Hub:** Connects with Zoom, GoToWebinar, WebinarJam, CRMs, and email platforms.
-   **Analytics & Reporting:** Tracks funnel metrics, ROI, and audience engagement patterns.

## Usage Examples

### Scenario 1: Create a complete webinar funnel for product launch

```bash
webinar create "Tecno Pova 6 Launch" --type live --topic "Gaming Performance Showcase"
webinar funnel setup "Tecno Pova 6 Launch" --stages "registration,3_reminders,live_event,3_followups"
webinar content generate "Tecno Pova 6 Launch" --format "script,slides,emails"
webinar promote "Tecno Pova 6 Launch" --channels "email,social,meta_ads"
```

### Scenario 2: Set up an evergreen automated webinar

```bash
webinar create "Mobile Photography Masterclass" --type automated --topic "Pro Tips for Smartphone Photography"
webinar funnel setup "Mobile Photography Masterclass" --stages "registration,immediate_access,3_value_emails,offer"
webinar replay setup "Mobile Photography Masterclass" --automation evergreen
```

### Scenario 3: Monitor webinar performance and optimize

```bash
webinar monitor "Tecno Pova 6 Launch" --metrics "registrations,show_rate,engagement_score,conversion_rate"
# Agent provides detailed analytics and recommendations for improvement
```

### Scenario 4: Generate follow-up sequences for different attendee segments

```bash
webinar content generate "Tecno Pova 6 Launch" --format "followup_emails" --segments "attended_full,attended_partial,no_show"
# Agent creates tailored email sequences for each segment
```

## Configuration

Webinar automation requires configuring platforms, content templates, and behavioral triggers.

-   **`config/platform_credentials.json`:** API keys for webinar platforms (Zoom, WebinarJam, etc.).
-   **`templates/emails/*.html`:** Email templates for different funnel stages.
-   **`templates/landing_pages/*.html`:** Registration page templates.
-   **`content/webinars/*`:** Webinar-specific content (scripts, slide decks).
-   **`funnels/*.json`:** Funnel configuration files defining stage sequences and triggers.

**Example funnel configuration:**

```json
{
  "webinar_name": "Tecno Pova 6 Launch",
  "type": "live",
  "funnel_stages": [
    {
      "stage": "registration",
      "trigger": "page_visit",
      "actions": ["capture_lead", "send_confirmation_email"]
    },
    {
      "stage": "reminder_24h",
      "trigger": "time_before_event",
      "delay": "24_hours",
      "actions": ["send_reminder_email", "sms_notification"]
    },
    {
      "stage": "reminder_1h",
      "trigger": "time_before_event",
      "delay": "1_hour",
      "actions": ["send_final_reminder", "calendar_notification"]
    },
    {
      "stage": "post_attended",
      "trigger": "attended_full",
      "actions": ["send_thank_you", "send_replay", "offer_discount"]
    },
    {
      "stage": "post_no_show",
      "trigger": "did_not_attend",
      "actions": ["send_replay_access", "invite_next_webinar"]
    }
  ]
}
```

## Related Skills

-   **`email-sequence`**: For advanced email automation and nurturing sequences.
-   **`lead-scoring`**: To score and prioritize webinar leads based on engagement.
-   **`analytics-dashboard`**: For comprehensive webinar performance tracking.
-   **`content-calendar`**: To schedule and coordinate webinar promotions across channels.
-   **`ai-chatbot-builder`**: To add chatbot support for webinar Q&A and registration assistance.
