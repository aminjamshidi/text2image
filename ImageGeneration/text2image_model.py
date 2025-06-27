from ImageGeneration.setting import settings
from together import Together
import base64


async def generate_image(prompt: str, output_path: str):

    together_client = Together(api_key=settings.TOGETHER_API_KEY)

    try:
        response = together_client.images.generate(
            prompt=prompt,
            model=settings.TTI_MODEL_NAME,
            width=1024,
            height=768,
            steps=4,
            response_format="b64_json",
        )
        image_data = base64.b64decode(response.data[0].b64_json)
        with open(output_path, "wb") as f:
            f.write(image_data)
        return True
    except:
        return False
