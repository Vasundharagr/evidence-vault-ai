# EVIDENCE VAULT: AI Summary Card
**Developer:** AI Developer 2
**GitHub Link:** https://github.com/Vasundharagr/evidence-vault-ai.git

## 🛠️ Tech Stack
*   **Language:** Python 3.12
*   **Framework:** Flask
*   **AI Engine:** Groq API (Model: LLaMA3-8b-8192)
*   **Security:** `flask-limiter` (Rate Limiting), `bleach` (HTML stripping), `flask-cors` (Access Control)

## 🌐 The 3 AI Endpoints
1. **`/describe` (POST)**
   *   *Input:* Raw, messy crime scene data.
   *   *Output:* A concise, clean summary identifying key entities.
2. **`/recommend` (POST)**
   *   *Input:* Current case details.
   *   *Output:* A JSON array of 3 actionable next steps for investigators.
3. **`/generate-report` (POST)**
   *   *Input:* Unstructured field notes.
   *   *Output:* A highly structured JSON report automatically assigning a Risk Level (LOW, MEDIUM, HIGH, CRITICAL).
