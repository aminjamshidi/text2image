from ImageGeneration.text2image_model import generate_image


from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/imageGeneration/")
async def text2image(prompt: str):
    output = await generate_image(prompt=prompt, output_path="image.png")
    if output:
        print()
        return JSONResponse(
            {"message": "the image is successfully saved in path : path.png"}
        )
    else:
        return JSONResponse({"message": "There is error while generating image"})
