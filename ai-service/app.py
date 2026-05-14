from flask import Flask, request, jsonify
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import bleach
import json
from flask_cors import CORS


app = Flask(# CRITICAL FIX (Day 7): Restrict API access to ONLY the React frontend
CORS(app, resources={r"/*": {"origins": "http://localhost:80"}})
)

# 1. Setup Flask-Limiter: Restrict to 30 requests per minute
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["30 per minute"],
    storage_uri="memory://" # Uses local memory to track IPs
)

# 2. List of phrases hackers use to break AI
INJECTION_KEYWORDS = [
    "ignore previous instructions",
    "ignore all previous",
    "system prompt",
    "bypass",
    "you are now",
    "forget everything"
]

# 3. Input Sanitization Middleware (Runs before EVERY request)
@app.before_request
def sanitize_input():
    # We only need to check POST/PUT requests that contain JSON data
    if request.is_json and request.method in ['POST', 'PUT']:
        try:
            data = request.get_json()
        except:
            return jsonify({"error": "Invalid JSON format"}), 400
            
        # Loop through the data to clean it and check for threats
        for key, value in data.items():
            if isinstance(value, str):
                
                # A. Strip HTML tags using bleach
                clean_value = bleach.clean(value, strip=True)
                
                # B. Detect Prompt Injection
                lower_value = clean_value.lower()
                for keyword in INJECTION_KEYWORDS:
                    if keyword in lower_value:
                        return jsonify({"error": "Prompt injection detected. Request blocked."}), 400
                
                # C. Update the data with the safe, stripped text
                data[key] = clean_value
                
        # Safely overwrite the incoming request with the cleaned data
        request.data = json.dumps(data).encode('utf-8')

# --- A simple route to test that it works! ---
@app.route('/test', methods=['POST'])
def test_security():
    # If the code reaches here, the middleware confirmed the input is safe!
    safe_data = request.get_json(force=True)
    return jsonify({
        "status": "success", 
        "message": "Data is clean and safe!", 
        "data_received": safe_data
    })

if __name__ == '__main__':
    print("🛡️ Security Service starting on port 5000...")
    app.run(port=5000, debug=True)
