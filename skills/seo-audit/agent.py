import json

def run_full_seo_audit(target_url, competitor_urls=None):
    """Performs a comprehensive SEO audit including technical, on-page, backlink, and competitor analysis.

    Args:
        target_url (str): The URL of the website or page to audit.
        competitor_urls (list, optional): List of competitor URLs for gap analysis. Defaults to None.

    Returns:
        str: A JSON string of the full SEO audit report.
    """
    print(f"Running full SEO audit for {target_url}...")
    audit_report = {
        "target_url": target_url,
        "overall_health_score": "[AI Gen] 85/100",
        "key_findings_recommendations": {
            "technical_seo": json.loads(audit_technical_seo(target_url)),
            "on_page_seo": json.loads(audit_on_page_seo(target_url)),
            "backlink_analysis": json.loads(analyze_backlinks(target_url)),
        }
    }
    if competitor_urls:
        audit_report["key_findings_recommendations"]["competitor_gap_analysis"] = \n            json.loads(perform_competitor_gap_analysis(target_url, competitor_urls))

    return json.dumps(audit_report, indent=2)

def audit_technical_seo(target_url):
    """Focuses on technical SEO aspects like crawlability, indexability, site speed, etc.

    Args:
        target_url (str): The URL to audit.

    Returns:
        str: A JSON string of technical SEO findings and recommendations.
    """
    print(f"Auditing technical SEO for {target_url}...")
    findings = [
        {"issue": "[AI Gen] Missing sitemap.xml entry", "recommendation": "[AI Gen] Create/update sitemap.xml and submit to GSC.", "impact": "High", "effort": "Low"},
        {"issue": "[AI Gen] Page load speed (LCP) is slow", "recommendation": "[AI Gen] Optimize images and minify CSS/JS.", "impact": "Medium", "effort": "Medium"}
    ]
    return json.dumps(findings, indent=2)

def audit_on_page_seo(page_url, keywords=None):
    """Specifically audits on-page elements like title tags, meta descriptions, content quality.

    Args:
        page_url (str): The URL of the page to audit.
        keywords (list, optional): Target keywords for the page. Defaults to None.

    Returns:
        str: A JSON string of on-page SEO findings and recommendations.
    """
    print(f"Auditing on-page SEO for {page_url}...")
    findings = [
        {"issue": "[AI Gen] Meta description too long", "recommendation": "[AI Gen] Shorten meta description to ~155 characters.", "impact": "Medium", "effort": "Low"},
        {"issue": "[AI Gen] H1 tag missing or incorrect", "recommendation": "[AI Gen] Ensure a single, descriptive H1 tag is present.", "impact": "High", "effort": "Low"}
    ]
    if keywords:
        findings.append({"issue": "[AI Gen] Keyword density low for some target keywords", "recommendation": f"[AI Gen] Naturally integrate {keywords} more frequently.", "impact": "Medium", "effort": "Medium"})

    return json.dumps(findings, indent=2)

def analyze_backlinks(target_domain, competitor_domains=None):
    """Evaluates backlink profiles for quality, quantity, and anchor text distribution.

    Args:
        target_domain (str): The domain to analyze backlinks for.
        competitor_domains (list, optional): List of competitor domains for comparison. Defaults to None.

    Returns:
        str: A JSON string of backlink analysis findings and recommendations.
    """
    print(f"Analyzing backlinks for {target_domain}...")
    findings = [
        {"issue": "[AI Gen] Low diversity of referring domains", "recommendation": "[AI Gen] Pursue link building from diverse sources.", "impact": "High", "effort": "High"},
        {"issue": "[AI Gen] Potential toxic backlinks identified", "recommendation": "[AI Gen] Disavow harmful links via GSC.", "impact": "High", "effort": "Medium"}
    ]
    if competitor_domains:
        findings.append({"finding": f"[AI Gen] Competitors have more EDU/GOV links than {target_domain}.", "recommendation": "[AI Gen] Explore outreach to educational/governmental institutions.", "impact": "High", "effort": "High"})

    return json.dumps(findings, indent=2)

def perform_competitor_gap_analysis(target_domain, competitor_domains):
    """Compares website performance with key competitors to identify opportunities.

    Args:
        target_domain (str):
        competitor_domains (list):

    Returns:
        str: A JSON string of competitor gap analysis findings.
    """
    print(f"Performing competitor gap analysis for {target_domain} against {competitor_domains}...")
    findings = [
        {"gap": "[AI Gen] Competitors rank for more long-tail keywords in 'accessories' category.", "recommendation": "[AI Gen] Create content around long-tail accessory keywords.", "impact": "High", "effort": "Medium"},
        {"gap": "[AI Gen] Competitor X has richer featured snippets for product reviews.", "recommendation": "[AI Gen] Implement/improve schema markup for reviews on product pages.", "impact": "Medium", "effort": "Low"}
    ]
    return json.dumps(findings, indent=2)
