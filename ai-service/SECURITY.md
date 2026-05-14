# Evidence Vault - Security Threat Model

This document outlines the top 5 potential security threats to the Evidence Vault application and how we plan to mitigate them.

## 1. SQL Injection (Backend)
**Threat:** Malicious users could input SQL commands into form fields to view, modify, or delete database records without authorization.
**Mitigation:** We will use Spring Data JPA/Hibernate on the backend, which automatically uses parameterized queries to sanitize inputs.

## 2. Prompt Injection (AI Service)
**Threat:** Users might input malicious text designed to trick the AI into ignoring its system prompt, potentially causing it to leak sensitive information or generate inappropriate content.
**Mitigation:** We will implement input sanitization middleware in Flask to strip HTML and detect known prompt injection patterns before sending data to Groq.

## 3. Unauthorized Access & Privilege Escalation
**Threat:** Users might try to access endpoints or data they are not authorized to view, or perform actions reserved for admins.
**Mitigation:** We will implement Spring Security with JWT tokens for strict role-based access control. All API endpoints will validate the token before returning data.

## 4. Cross-Site Scripting (XSS)
**Threat:** Attackers could inject malicious scripts into the application that then execute in the browsers of other users viewing that data.
**Mitigation:** The React frontend will automatically sanitize text. We will also use `bleach` in the Python backend to strip HTML tags from inputs.

## 5. Denial of Service (DoS) via AI Endpoint Spam
**Threat:** A user could repeatedly spam the `/generate-report` endpoint, exhausting our Groq API rate limits and taking down the AI service for everyone.
**Mitigation:** We will implement `flask-limiter` on the Python service to restrict users to a maximum of 30 requests per minute.


## Week 1 Security Test Results (Completed Day 5)

**Test 1: Empty Input Handling**
*   **Action:** Sent an empty JSON payload `{}` to all AI endpoints.
*   **Result:** Handled gracefully. Endpoints returned a validation error or empty string rather than crashing the server.
*   **Status:** Pass ✅

**Test 2: Prompt Injection Test**
*   **Action:** Sent known injection strings like `"ignore previous instructions"` and `"system prompt"` to the AI service.
*   **Result:** The input sanitization middleware successfully detected the keywords and immediately returned a `400 Bad Request` before calling the Groq API.
*   **Status:** Pass ✅

**Test 3: SQL/HTML Injection (XSS)**
*   **Action:** Sent payloads containing `<script>` tags and SQL keywords.
*   **Result:** The `bleach` library successfully stripped the HTML tags. SQL keywords were treated safely as raw text (no execution risk on the AI side).
*   **Status:** Pass ✅

---

## Week 2 Security Sign-Off (Completed Day 9)

**1. JWT Authentication Verification**
*   **Status:** Verified ✅
*   **Notes:** The Spring Boot backend successfully implements JWT. The AI Flask service is restricted via CORS to only accept requests from the authorized frontend, ensuring unauthorized external traffic cannot bypass the JWT check.

**2. Rate Limiting Verification**
*   **Status:** Verified ✅
*   **Notes:** `flask-limiter` is active. Terminal testing confirms that exceeding 30 requests per minute results in a `429 Too Many Requests` response, protecting our Groq API limits.

**3. Injection Prevention Verification**
*   **Status:** Verified ✅
*   **Notes:** The `pytest` unit tests executed on Day 8 mathematically prove that `bleach` strips malicious HTML and the middleware blocks known prompt injection phrases.

**4. PII (Personally Identifiable Information) Audit**
*   **Status:** Verified ✅
*   **Notes:** A comprehensive review of all AI prompts (`report_prompt.txt`) and Groq API payloads confirms that no user personal data (passwords, emails, SSNs, etc.) is included in the AI context window. The AI only processes sanitized case evidence.

**Sign-off By:** AI Developer 2
