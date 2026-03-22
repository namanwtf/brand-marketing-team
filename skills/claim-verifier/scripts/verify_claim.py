#!/usr/bin/env python3
"""
Claim Verifier Script
Fact-checking layer that validates competitive intel claims before delivery.
"""

import sys
import json
import re
from datetime import datetime
from typing import Dict, List, Optional


def verify_claim(claim: str) -> Dict:
    """
    Verify a claim and return verification status.
    
    Args:
        claim: The claim string to verify
        
    Returns:
        Dict with verification status, sources, and confidence
    """
    result = {
        "claim": claim,
        "status": "UNVERIFIED",
        "sources": [],
        "confidence": 0.0,
        "reason": "No verification performed",
        "verified_at": datetime.now().isoformat()
    }
    
    # Check for red flags
    red_flags = check_red_flags(claim)
    if red_flags:
        result["status"] = "SUSPICIOUS"
        result["reason"] = f"Red flags detected: {', '.join(red_flags)}"
        return result
    
    # Try to identify claim type
    claim_type = identify_claim_type(claim)
    result["claim_type"] = claim_type
    
    # Basic verification flow
    # Note: This is a minimal implementation. Full implementation would integrate
    # with web_search tool for source verification.
    
    if claim_type == "PRICE":
        result = verify_price_claim(claim, result)
    elif claim_type == "SPEC":
        result = verify_spec_claim(claim, result)
    elif claim_type == "LAUNCH_DATE":
        result = verify_launch_date(claim, result)
    elif claim_type == "TREND":
        result = verify_trend_claim(claim, result)
    else:
        result["reason"] = "Generic claim - manual verification required"
    
    return result


def check_red_flags(claim: str) -> List[str]:
    """Check claim against known red flags."""
    flags = []
    
    # Check for extreme specs at extreme prices
    if re.search(r'\d{3}MP.*₹\d{1,2},\d{3}', claim):
        flags.append("Extreme specs at low price")
    
    # Check for round numbers without context
    if re.search(r'₹\d{1,2},999', claim) and "confirmed" not in claim.lower():
        flags.append("Round pricing without source")
    
    # Check for "too good to be true" indicators
    if any(x in claim.lower() for x in ["revolutionary", "game-changing", "never before"]):
        flags.append("Hype language without verification")
    
    return flags


def identify_claim_type(claim: str) -> str:
    """Identify the type of claim being made."""
    claim_lower = claim.lower()
    
    if any(word in claim_lower for word in ["price", "₹", "rs", "cost", "priced"]):
        return "PRICE"
    elif any(word in claim_lower for word in ["mp", "megapixel", "screen", "display", "processor", "ram"]):
        return "SPEC"
    elif any(word in claim_lower for word in ["launch", "release", "announced", "coming"]):
        return "LAUNCH_DATE"
    elif any(word in claim_lower for word in ["trend", "popular", "demand", "search"]):
        return "TREND"
    else:
        return "GENERIC"


def verify_price_claim(claim: str, result: Dict) -> Dict:
    """Verify a price-related claim."""
    result["status"] = "UNVERIFIED"
    result["reason"] = "Price verification requires web search against Amazon/Flipkart/brand site"
    result["verification_steps"] = [
        "Search Amazon.in for product",
        "Search Flipkart.com for product",
        "Check official brand website",
        "Cross-reference with multiple sources"
    ]
    return result


def verify_spec_claim(claim: str, result: Dict) -> Dict:
    """Verify a specification-related claim."""
    result["status"] = "UNVERIFIED"
    result["reason"] = "Spec verification requires checking 91Mobiles/GSMArena/brand site"
    result["verification_steps"] = [
        "Check 91mobiles.com specifications",
        "Verify on GSMArena.com",
        "Cross-check with official brand site",
        "Compare with press releases"
    ]
    return result


def verify_launch_date(claim: str, result: Dict) -> Dict:
    """Verify a launch date claim."""
    result["status"] = "UNVERIFIED"
    result["reason"] = "Launch date verification requires press releases or reputable tech news"
    result["verification_steps"] = [
        "Check brand official press releases",
        "Search reputable tech outlets",
        "Verify on 91Mobiles/Gadgets 360",
        "Check social media announcements"
    ]
    return result


def verify_trend_claim(claim: str, result: Dict) -> Dict:
    """Verify a trends-related claim."""
    result["status"] = "UNVERIFIED"
    result["reason"] = "Trend verification requires Google Trends or market research data"
    result["verification_steps"] = [
        "Check Google Trends for keyword",
        "Reference Canalys/Counterpoint reports",
        "Verify with market research data"
    ]
    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: verify_claim.py '<claim text>'")
        print("\nExample:")
        print('  python verify_claim.py "Tecno Pova 6 will feature a 6000mAh battery"')
        sys.exit(1)
    
    claim = sys.argv[1]
    result = verify_claim(claim)
    
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()