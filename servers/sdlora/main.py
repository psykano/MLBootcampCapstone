import sys
import os
import random
import torch
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

app = FastAPI()


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
    
    # Generate prompt
    positive_prompt = generate_prompt(prompt)
    negative_prompt = """lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"""

    # Set sd params
    model_dir = "/Users/christopherjohns/Documents/python/sdlora-capstone-server/AnyLoRA_noVae_fp16-pruned.safetensors"
    lora_dir = "/Users/christopherjohns/Documents/python/sdlora-capstone-server/capstone.safetensors"
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

    # Save image to disk
    image_name = str(seed) + ".png"
    image.save(os.path.join("/Users/christopherjohns/Documents/python/sdlora-capstone-server", image_name))

    res.image = image_name
    return res


def generate_prompt(prompt: PromptRequest):
    return """masterpiece, best quality, simple background, white background, solo, perfume, bottle, a single bottle of perfume on a white background, {} and {} perfume bottle with a {} top""".format(prompt.shape, prompt.color, prompt.top)


# For debugging
import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)