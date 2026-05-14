# Evidence Vault: Post-Demo Review (Day 19)
**Author:** AI Developer 2

## 1. Lessons Learned
*   **Prompt Engineering is a Science:** I learned that AI requires highly specific, structural instructions to be reliable in an enterprise application. Transitioning from a generic "Summarize this" prompt to strict JSON constraints dramatically improved our success rate.
*   **Security is Paramount:** Implementing the Flask middleware for sanitization taught me that you cannot trust user input, especially when passing data to third-party LLMs like Groq. Rate limiting (`flask-limiter`) was also a crucial learning point for protecting our API quotas from abuse.

## 2. Features for Future Sprints
*   **AI Explainability:** Add a feature where the AI highlights exactly which sentences from the raw evidence led to a HIGH or CRITICAL risk rating, building trust with the investigators.
*   **Multi-Model Fallback:** If Groq experiences an outage, the application should automatically fall back to another LLM provider without crashing.
*   **PDF Upload Support:** Allow investigators to upload PDF police reports or images directly to the AI service rather than having to type out the text manually.

## 3. Feedback to Mentor
*   The sprint structure was highly effective. Having day-by-day tasks allowed me to focus on learning specific technologies (like Pytest, Flask security, and Groq API integration) without getting overwhelmed by the big picture.
*   *Suggestion:* It would be helpful to have a dedicated "integration day" slightly earlier in the sprint to ensure the Java backend and Python AI service can communicate smoothly before we hit Week 3.
