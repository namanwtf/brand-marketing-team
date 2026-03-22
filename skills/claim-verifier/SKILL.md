---
name: claim-verifier
description: Fact-checking layer that validates all competitive intel claims before delivery to user. Prevents hallucination and maintains trust.
tags:
  - verification
  - fact-check
  - competitive-intel
  - trust
---

# Claim Verifier Skill

## Summary
Fact-checking layer that validates all competitive intel claims before delivery to user. Prevents hallucination and maintains trust.

## Core Rule
**NO UNVERIFIED CLAIMS GO TO USER**

Every claim must pass one of:
- ✅ Primary source (manufacturer website, press release)
- ✅ Secondary source (reputable tech outlet: 91Mobiles, Gadgets 360, GSMArena, Economic Times Tech)
- ✅ Google Trends data (screenshot/quantitative)
- ✅ Price verification (Amazon/Flipkart screenshot)
- ⚠️ Marked as "Unverified" if above unavailable

## Verification Workflow

### Step 1: Initial Claim Generation
Research agent generates competitive intel with sources

### Step 2: Verification Check
Verifier agent checks each claim:
- Price? → Screenshot Amazon/Flipkart
- Specs? → Official site or 91Mobiles/GSMArena
- Launch date? → Press release or reputable outlet
- Trend data? → Google Trends screenshot
- Market share? → Canalys/Counterpoint/IDC report

### Step 3: Confidence Rating
- **VERIFIED** — Multiple sources confirm
- **LIKELY** — Single reputable source, no contradictions
- **UNVERIFIED** — No source found or contradicts known data
- **SUSPICIOUS** — Contradicts existing data

### Step 4: User Delivery
- VERIFIED claims → Include source link
- LIKELY claims → Include source link + confidence note
- UNVERIFIED claims → "[Unverified - seeking confirmation]"
- SUSPICIOUS claims → Remove entirely, flag for manual check

## Red Flags (Auto-Suspend)
These trigger immediate "UNVERIFIED" flag:
- Extreme specs at extreme price (300MP at ₹12,999)
- Round numbers (₹8,999, ₹12,999) without source
- Contradicts established brand behavior
- No recent news coverage for "recent launch"
- Too good to be true pricing

## Verification Tools
1. **Price Check**: Amazon.in, Flipkart.com, brand site
2. **Spec Check**: 91mobiles.com, gsmarena.com, gadgets360.com
3. **News Check**: Google News Search with date filter
4. **Trends Check**: Google Trends screenshot
5. **Official**: brand.com/press or official social

## Output Format

### Verified Claim
```
✅ **Infinix GT 30 pricing**
Source: [Verifiable URL]
Status: VERIFIED
Claim: ₹24,999 base variant
Screenshot: [if captured]
```

### Unverified Claim
```
⚠️ **Infinix 200MP at ₹8,999**
Status: UNVERIFIED
Reason: No source found, contradicts component cost reality
Recommendation: Do not share with user
```

## Sub-Agent Instructions
Claim Verifier Sub-Agent task:
1. Receive claim list from research agent
2. For each claim: verify using tools above
3. Rate confidence (VERIFIED/LIKELY/UNVERIFIED/SUSPICIOUS)
4. Return annotated claim list
5. Never let SUSPICIOUS claims reach user

## User Communication
When sending intel to user:
- Lead with verified claims only
- Mark any "LIKELY" claims clearly
- Never present UNVERIFIED as fact
- If asked about unverified claim: "I don't have confirmed data on that yet"

---

**Created:** March 2, 2026
**Purpose:** Trust and accuracy preservation
**Rule:** Better to say "I don't know" than to make up impressive-sounding claims
