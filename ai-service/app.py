from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import bleach
import json
import time

start_time = time.time()

# 1. Initialize the App FIRST
app = Flask(__name__)

# 2. Apply CORS security AFTER the app is initialized
CORS(app, resources={r"/*": {"origins": "http://localhost:80"}})

# 3. Setup Flask-Limiter: Restrict to 30 requests per minute
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://" 
)

# 4. List of phrases hackers use to break AI
INJECTION_KEYWORDS = [
    "ignore previous instructions",
    "ignore all previous",
    "system prompt",
    "bypass",
    "you are now",
    "forget everything"
]

# 5. Input Sanitization Middleware 
@app.before_request
def sanitize_input():
    if request.is_json and request.method in ['POST', 'PUT']:
        try:
            data = request.get_json()
        except:
            return jsonify({"error": "Invalid JSON format"}), 400
            
        for key, value in data.items():
            if isinstance(value, str):
                clean_value = bleach.clean(value, strip=True)
                lower_value = clean_value.lower()
                for keyword in INJECTION_KEYWORDS:
                    if keyword in lower_value:
                        return jsonify({"error": "Prompt injection detected."}), 400
                data[key] = clean_value
                
        request.data = json.dumps(data).encode('utf-8')

# --- Health Check Endpoint (For Demo Day) ---
@app.route('/health', methods=['GET'])
def health_check():
    uptime = round(time.time() - start_time, 2)
    return jsonify({
        "status": "UP",
        "service": "Evidence Vault AI",
        "model": "LLaMA 3 (Groq)",
        "uptime_seconds": uptime,
        "rate_limit": "30/minute"
    }), 200

# --- Test Route ---
@app.route('/test', methods=['POST'])
def test_security():
    safe_data = request.get_json(force=True)
    return jsonify({
        "status": "success", 
        "message": "Data is clean and safe!", 
        "data_received": safe_data
    })

if __name__ == '__main__':
    print("🛡️ Security Service starting on port 5000...")
    app.run(port=5000, debug=True)
