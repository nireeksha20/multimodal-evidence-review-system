from google import genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("GEMINI_API_KEY"))
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

image = Image.open(
    "dataset/images/sample/case_001/img_1.jpg"
)

response = client.models.generate_content(
    model="gemini-2.0-flash-lite",
    contents=[
        image,
        """
        Analyze this image.

        Return:
        - object type
        - visible damage
        - damaged part
        - severity

        Keep response short.
        """
    ]
)

print(response.text)