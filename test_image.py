from google import genai
from PIL import Image
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

image = Image.open(
    "dataset/images/test/case_003/img_1.jpg"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        image,
        """
        Analyze this damage image.

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