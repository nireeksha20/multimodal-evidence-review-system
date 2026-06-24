from google import genai
from PIL import Image
from dotenv import load_dotenv
import os
import json
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

PROMPT = """
You are an insurance claim reviewer.

Analyze the image.

Return ONLY valid JSON.

{
  "valid_image": true,
  "issue_type": "dent",
  "object_part": "door",
  "severity": "medium",
  "evidence_standard_met": true,
  "evidence_reason": "damage clearly visible"
}

Allowed issue_type values:
dent,scratch,crack,shatter,broken,missing,torn,crushed,water,stain,none,unknown

Allowed severity values:
none,low,medium,high,unknown

JSON only.
"""

def analyze_image(image_path):

    retries = 5

    for attempt in range(retries):

        try:

            image = Image.open(image_path)

            response = client.models.generate_content(
                model="gemini-flash-lite-latest",
                contents=[
                    image,
                    PROMPT
                ]
            )

            text = response.text.strip()

            start = text.find("{")
            end = text.rfind("}") + 1

            text = text[start:end]

            result = json.loads(text)

            return result

        except Exception as e:

            print(
                f"Retry {attempt+1}/5:",
                e
            )

            time.sleep(15)

    return {
        "valid_image": False,
        "issue_type": "unknown",
        "object_part": "unknown",
        "severity": "unknown",
        "evidence_standard_met": False,
        "evidence_reason": "analysis failed"
    }