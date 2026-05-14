# OWASP ZAP Scan Report
**Date:** May 2026
**Target:** `http://localhost:5000` (AI Flask Service)

## Executive Summary
The AI service was scanned using OWASP ZAP. Thanks to the sanitization and rate-limiting middleware implemented previously, no injection or DoS vulnerabilities were found. 

However, 1 Critical and 2 Medium vulnerabilities were detected.

### 🔴 CRITICAL FINDINGS (Fixed on Day 7)
**1. Wildcard CORS Policy (Cross-Origin Resource Sharing)**
*   **Description:** The application currently allows any website on the internet to send API requests to it. A malicious website could trick a user's browser into sending unauthorized requests to our AI service.
*   **Fix Applied:** Installed `flask-cors` and restricted the origins to ONLY allow `http://localhost:80` (our React Frontend).

### 🟡 MEDIUM FINDINGS (Planned for Day 8)
**1. Missing Anti-Clickjacking Header**
*   **Description:** The response does not include `X-Frame-Options`.
*   **Plan:** AI Developer 1 will implement standard Security Headers on Day 8.

**2. Missing Strict-Transport-Security Header**
*   **Description:** Application is not enforcing HTTPS.
*   **Plan:** AI Developer 1 will implement standard Security Headers on Day 8.
