import os
import time
import json
import logging
from groq import Groq
from dotenv import load_dotenv

# Set up error logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class GroqClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            logger.error("GROQ_API_KEY not found in environment.")
            raise ValueError("API Key is missing")
        
        self.client = Groq(api_key=api_key)

    def generate_json_response(self, prompt_text, max_retries=3):
        """Sends a prompt to Groq, expects JSON back, with a 3-retry backoff mechanism."""
        
        for attempt in range(max_retries):
            try:
                logger.info(f"Attempt {attempt + 1}: Requesting AI response...")
                
                response = self.client.chat.completions.create(
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful assistant. You must always return your response in valid JSON format."
                        },
                        {
                            "role": "user",
                            "content": prompt_text
                        }
                    ],
                    model="llama3-8b-8192",
                    response_format={"type": "json_object"} # Forces JSON parsing
                )
                
                # Parse the JSON response
                raw_content = response.choices[0].message.content
                parsed_json = json.loads(raw_content)
                
                logger.info("Successfully received and parsed JSON from Groq.")
                return parsed_json
                
            except Exception as e:
                logger.error(f"Error on attempt {attempt + 1}: {e}")
                
                if attempt < max_retries - 1:
                    sleep_time = 2 ** (attempt + 1) # Backoff: waits 2s, then 4s
                    logger.info(f"Retrying in {sleep_time} seconds...")
                    time.sleep(sleep_time)
                else:
                    logger.error("All 3 retries failed.")
                    return {"error": "Failed to generate AI response after 3 attempts."}
