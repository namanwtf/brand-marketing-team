# Security Auditor Skill

This skill provides comprehensive security auditing capabilities, acting as a specialist in secure coding practices, vulnerability detection, and OWASP compliance. It's designed to review code and architectural decisions for potential security flaws and suggest actionable fixes.

## Features

- **OWASP Top 10 Audit**: Checks for common vulnerabilities listed in the OWASP Top 10 (e.g., Injection, Broken Access Control, Cryptographic Failures, XSS).
- **Secure Coding Best Practices**: Enforces principles like least privilege, input validation, encryption, and defense in depth.
- **Security Configuration Review**: Audits security headers (CSP, HSTS), cookie security, JWT best practices, and environment variable handling.
- **Dependency Vulnerability Checks**: Guides on using tools like `npm audit` to identify and fix known vulnerabilities in third-party libraries.
- **Structured Reporting**: Generates detailed security audit reports with vulnerability severity, location, recommended fixes, and risk assessments.

## Scripts

- `scripts/security_scan.py`: A Python script intended to simulate or orchestrate actual security scanning tools and apply security audit rules. It can be extended to integrate with SAST tools, dependency scanners, and custom vulnerability checks.

## Usage

Refer to `SKILL.md` for a detailed breakdown of the audit process, core security principles, OWASP checklists, and specific code examples for secure implementations (e.g., input validation, authentication, secret management). This skill is meant to be invoked when a security review or audit is required for code or architecture.
