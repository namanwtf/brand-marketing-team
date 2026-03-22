## Claim Verifier - Fact-checking layer

This skill provides a fact-checking layer to validate competitive intelligence claims before they are delivered to the user. It helps prevent hallucination and maintains trust.

### Core Functionality

The `verify_claim.py` script takes a claim as input and attempts to verify it against predefined sources.

### Verification Process

1. **Input:** A claim (e.g., "Tecno Pova 6 will have a new processor X").
2. **Verification Logic:** The script uses web search (Brave API) to look for official announcements, reputable tech news sites, or product pages that confirm or refute the claim.
3. **Output:** Returns a status (VERIFIED, LIKELY, UNVERIFIED, SUSPICIOUS) and a reason/source.

### Usage

To verify a claim:

```bash
python scripts/verify_claim.py "Tecno Pova 6 will feature the Dimensity 6020 processor."
```

Refer to `SKILL.md` for detailed verification rules and confidence ratings.
