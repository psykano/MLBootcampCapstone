import sys
import os
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
    
    #
    positivePrompt = generate_prompt(prompt)
    negativePrompt = """lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"""

    return res


def generate_prompt(prompt):
    return """masterpiece, best quality, simple background, white background, solo, perfume, bottle, a single bottle of perfume on a white background, {} and {} perfume bottle with a {} top""".format(prompt.shape, prompt.color. prompt.top)