import sys
import os
import torch
from diffuser_tools.text2img import Text2ImagePipe
from diffuser_tools.utilities import plot_images, save_images

def main(argv):
    # Define model and LoRA paths
    model_dir = "/Users/christopherjohns/Documents/tmpo/AnyLoRA_noVae_fp16-pruned.safetensors"
    lora_dir = "/Users/christopherjohns/Documents/tmpo/capstone.safetensors"

    # Clip skip.
    clip_skip = 0

    # Scheduler.
    scheduler = "EADS"

    # Create prompt and negative prompts.
    prompt = """masterpiece, best quality, simple background, white background, solo, perfume, bottle, a single bottle of perfume on a white background, square and red perfume bottle with a black top"""
    negative_prompt = """lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"""

    # Initialize the text to image pipe class.
    text_2_img = Text2ImagePipe(
        model_dir = model_dir,
        prompt = prompt,
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

    # Set seed
    seed = 25

    # Run the text to image pipeline
    image = text_2_img.run_pipe(
        steps = 25,
        width = 512,
        height = 512,
        scale = 7.5,
        seed = seed,
        use_prompt_embeddings = False,
        verbose = True,
    )

    # Save image to disk
    image_name = str(seed) + ".png"
    image.save(os.path.join("/Users/christopherjohns/Documents/tmpo", image_name))

if __name__ == "__main__":
    main(sys.argv)