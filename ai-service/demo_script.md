# AI Developer 2 - Demo Day Script (60 Seconds)

**Goal:** Explain the Flask + Groq integration to a non-technical panel and demonstrate the AI features.

---

## 1. The Setup 
*(Before it's your turn to speak, make sure you have the app open and are on the "Evidence List" page).*

## 2. The Demonstration

*(Action: Click on a specific Evidence record, then click the **"AI Recommend"** button).*

**🗣️ SCRIPT:** "Hello panel, I am the AI Developer for Evidence Vault. You are currently looking at our AI Recommend feature. When an investigator is stuck on a case, they simply click this button."

*(Action: Wait 2 seconds for the AI response to appear on screen).*

**🗣️ SCRIPT:** "As you can see, the AI just instantly analyzed the case and generated three actionable next steps—such as requesting CCTV footage and interviewing the primary witness."

*(Action: Navigate to the "Generate Report" page. Type this exact input into the box:)*
**Input to type:** `Suspect dropped a USB drive at the scene.`
*(Action: Click **"Generate Report"**).*

**🗣️ SCRIPT:** "Now let me show you our Report Generator. I type in some unstructured, messy field notes... and click Generate."

*(Action: Wait for the formatted report to appear on screen. Expected output is a structured report with Risk Level: HIGH).*

**🗣️ SCRIPT:** "The AI has transformed my raw notes into a perfectly formatted, professional JSON report, automatically flagging it as a HIGH risk level."

## 3. The Tech Explanation (Non-Technical)
*(Action: Stop clicking, look directly at the panel/camera).*

**🗣️ SCRIPT:** "So, how does this work under the hood? 

We built a custom microservice using Python and the Flask framework. Think of this service as a highly secure translator. When the investigator clicks a button, our Java backend sends the data to my Python service. 

My Python code instantly cleans the data—stripping out any malicious hacking attempts or HTML—and then securely forwards it to Groq, which is one of the fastest AI engines in the world. 

Because we engineered highly optimized 'System Prompts', the AI doesn't hallucinate or guess; it follows strict mathematical rules to return exactly the formatted data we need in under two seconds. It’s incredibly fast, it’s secure, and it saves investigators hours of paperwork."
