# EVIDENCE VAULT: AI Talking Points

## 🧠 Explaining Groq (Plain English)
*   *"We use Groq because it utilizes a custom computer chip (an LPU) designed specifically for AI. It allows our tool to read case files and generate reports nearly instantly, without making the investigator wait."*

## 📜 Explaining Our Prompts (Plain English)
*   *"We didn't just plug in an AI and hope it works. We wrote 'System Prompts', which act like a strict boss giving the AI rules. We force the AI to return data in a strict format and explicitly tell it 'DO NOT HALLUCINATE'. If the AI doesn't know something, our prompt forces it to admit it instead of making up fake evidence."*

## 🛡️ Security Talking Points
*   **Rate Limiting:** *"To prevent bots or hackers from spamming us, we built a limiter that restricts users to 30 requests per minute."*
*   **Prompt Injection:** *"We built a custom filter that acts like a bouncer. If someone types 'ignore previous instructions', our Python code catches it and throws a 400 Error before the AI even sees the message."*
*   **Data Privacy (PII):** *"We conducted an audit to ensure we do not send passwords or unnecessary personal information into the AI context window."*
