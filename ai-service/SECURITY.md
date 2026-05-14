# Evidence Vault - Final Security Threat Model & Audit

## Executive Summary
This document outlines the security architecture of the Evidence Vault application. Throughout the development sprint, we identified 5 primary threat vectors, implemented targeted mitigations (including JWT, rate limiting, and input sanitization), and conducted rigorous unit testing and OWASP ZAP scanning to verify our defenses. As of Day 12, all Critical and High vulnerabilities have been resolved.

---

## 1. Threat Model & Mitigations

### 1.1 SQL Injection (Backend)
**Threat:** Malicious users could input SQL commands to view, modify, or delete database records.
**Mitigation:** The Spring Boot backend uses Spring Data JPA/Hibernate, leveraging parameterized queries to sanitize all database inputs.

### 1.2 Prompt Injection (AI Service)
**Threat:** Users might input malicious text designed to trick the AI into ignoring its system prompt (e.g., "ignore previous instructions").
**Mitigation:** The Flask AI service uses a custom middleware to detect known prompt injection phrases and immediately rejects the request with a `400 Bad Request`.

### 1.3 Unauthorized Access & Privilege Escalation
**Threat:** Users might try to access endpoints or data they are not authorized to view.
**Mitigation:** Spring Security and JWT tokens strictly enforce role-based access control. The AI Service uses CORS to ensure it only accepts requests from the authorized frontend.

### 1.4 Cross-Site Scripting (XSS)
**Threat:** Attackers could inject malicious scripts (`<script>`) into the application.
**Mitigation:** The React frontend automatically sanitizes DOM text. The Python AI service uses `bleach` to strip HTML tags from incoming payloads.

### 1.5 Denial of Service (DoS) via AI Endpoint Spam
**Threat:** A user could spam AI endpoints, exhausting Groq API rate limits and taking down the service.
**Mitigation:** `flask-limiter` restricts users to a maximum of 30 requests per minute on the AI service.

---

## 2. Test Results & Verification

### Week 1 Security Tests
*   **Empty Input Handling:** Pass ✅ (Handled gracefully via validation)
*   **Prompt Injection:** Pass ✅ (Middleware successfully blocked attacks)
*   **HTML Injection (XSS):** Pass ✅ (`bleach` successfully stripped tags)

### OWASP ZAP Scan
*   **Critical Findings:** 1 (Wildcard CORS Policy) -> **FIXED** by restricting origins to localhost.
*   **Medium Findings:** 2 (Missing Security Headers) -> **FIXED** by adding Strict-Transport-Security.
*   **Remaining Critical/High Vulnerabilities:** 0

### Week 2 Security Sign-Off
*   **JWT Verification:** Verified ✅
*   **Rate Limiting:** Verified ✅
*   **PII Audit:** Verified ✅ (No personal data is sent to Groq)

---

## 3. Residual Risks (Unavoidable Threats)
*   **Zero-Day AI Jailbreaks:** New prompt injection techniques are discovered regularly by hackers. While our keyword blocklist catches known attacks, highly sophisticated, newly invented "jailbreaks" might still bypass our filter. 
*   **Dependency Vulnerabilities:** Future security flaws could be discovered in our Python or Java libraries. We plan to use Dependabot on GitHub to monitor this in the future.

---

## 4. Final Team Sign-Off
By signing below, the team confirms that the security measures outlined in this document have been implemented, tested, and verified in the containerized production environment.

*   **Java Developer 1:** [Signed]
*   **Java Developer 2:** [Signed]
*   **AI Developer 1:** [Signed]
*   **AI Developer 2:** [Signed]
