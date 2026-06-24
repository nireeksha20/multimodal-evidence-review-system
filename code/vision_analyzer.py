from google import genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

image = Image.open(
    "../dataset/images/sample/case_001/img_1.jpg"
)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[
        image,
        """
        Return ONLY JSON.

        {
          "issue_type":"",
          "object_part":"",
          "severity":""
        }
        """
    ]
)

print(response.text)