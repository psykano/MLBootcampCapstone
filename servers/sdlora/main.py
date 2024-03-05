import sys
import os
import random
import shortuuid
import torch
import cloudinary
import cloudinary.uploader
import ssl
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from diffuser_tools.text2img import Text2ImagePipe

class PromptRequest(BaseModel):
    key: str
    color: str
    shape: str
    top: str

class PromptResponse(BaseModel):
    image: str = ''

load_dotenv()

api_key = os.getenv("API_KEY")
base_path = os.getenv("BASE_PATH")
       
cloudinary.config(
    cloud_name = os.getenv("CL_CLOUD_NAME"),
    api_key = os.getenv("CL_API_KEY"),
    api_secret = os.getenv("CL_API_SECRET")
)

app = FastAPI()
ssl_keyfile = base_path + 'privkey.pem'
ssl_certfile = base_path + 'fullchain.pem'


@app.get("/")
async def read_root():
    return {"Helloo": "Worldo"}


@app.post("/api/prompt/")
async def create_prompt(prompt: PromptRequest):
    res = PromptResponse()

    # Check whether key is correct
    if prompt.key != api_key:
        return res
    
    # Validate request
    prompt.color = prompt.color.strip().lower()
    prompt.shape = prompt.shape.strip().lower()
    prompt.top = prompt.top.strip().lower()
    if not (prompt.color.isalpha() and prompt.shape.isalpha() and prompt.top.isalpha()):
        return res
    
    imageURL = await generate_image(prompt)
    res.image = imageURL

    return res


async def generate_image(prompt: PromptRequest):
    # Generate prompt
    positive_prompt = await generate_prompt(prompt)
    negative_prompt = """lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"""

    # Set sd params
    model_dir = base_path + "AnyLoRA_noVae_fp16-pruned.safetensors"
    lora_dir = base_path + "capstone.safetensors"
    clip_skip = 0
    scheduler = "EADS"
    seed = random.randint(42,4294967295)
    steps = 10

    # Initialize the text to image pipe class.
    text_2_img = Text2ImagePipe(
        model_dir = model_dir,
        prompt = positive_prompt,
        negative_prompt = negative_prompt,
        lora_dir = lora_dir,
        scheduler = scheduler,
        clip_skip = clip_skip,
        safety_checker = None,
        use_prompt_embeddings = True,
        split_character = ",",
        torch_dtype = torch.float16,
        device = torch.device("mps"),
    )

    # Run the text to image pipeline
    image = text_2_img.run_pipe(
        steps = steps,
        width = 512,
        height = 512,
        scale = 7.5,
        seed = seed,
        use_prompt_embeddings = False,
        verbose = True,
    )

    public_id = ""
    image_path = ""

    # Save image to disk
    while True:
        public_id = shortuuid.uuid()
        image_name = public_id + ".png"
        image_path = os.path.join(base_path, image_name)
        if os.path.isfile(image_path) is False:
            break
    image.save(image_path)

    cloudinary.uploader.upload(image_path, public_id=public_id, unique_filename=False, overwrite=True)
    srcURL = cloudinary.CloudinaryImage(public_id).build_url()

    # Remove file locally
    os.remove(image_path)

    return srcURL


async def generate_prompt(prompt: PromptRequest):
    return """masterpiece, best quality, simple background, white background, solo, perfume, bottle, a single bottle of perfume on a white background, {} and {} perfume bottle with a {} top""".format(prompt.shape, prompt.color, prompt.top)


# For debugging
import uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, ssl_keyfile=ssl_keyfile, ssl_certfile=ssl_certfile, workers=4)