import torch
from torch import nn
from torch.autograd import Variable
from torch.nn import functional as F
import torch.utils.data

from torchvision.models.inception import inception_v3

import numpy as np
from scipy.stats import entropy

# From https://github.com/sbarratt/inception-score-pytorch
from inception_score import inception_score

import os
from PIL import Image
import numpy as np

# Parameters
outdir = '--outdir=/content/drive/MyDrive/Capstone/stylegan3/results'
cfg = '--cfg=stylegan3-t'
data = '--data=/content/drive/MyDrive/Capstone/stylegan3/datasets/dataset_512.zip'
gpus = '--gpus=1'
batch = '--batch=32'
batch_gpu = '--batch-gpu=8'
mirror = '--mirror=0'
kimg = '--kimg=50'
tick = '--tick=2'
snap = '--snap=4'
workers = '--workers=2'

def load_images_from_directory(directory, start_idx=20, end_idx=50):
    """Load images from directory, convert them to 3xHxW numpy arrays normalized in the range [-1, 1]."""
    images = []
    for idx in range(start_idx, end_idx + 1):
        image_name = f'fakes{idx:06d}.png'
        image_path = os.path.join(directory, image_name)
        if os.path.exists(image_path):
            with Image.open(image_path) as img:
                img = img.convert('RGB')  # Ensure image is RGB
                # Convert image to numpy array and normalize to [-1, 1]
                np_img = np.array(img, dtype=np.float32) / 127.5 - 1.0
                # Rearrange the array dimensions to be (3, H, W)
                np_img = np_img.transpose(2, 0, 1)
                images.append(np_img)
    return np.array(images)

# Training loop for different gamma values
gamma_values = np.linspace(4, 10, num=7)
results = []
for gamma in gamma_values:
    gamma_str = f'--gamma={gamma}'
    command = f'python /content/drive/MyDrive/Capstone/stylegan3/train.py {outdir} {cfg} {data} {gpus} {batch} {batch_gpu} {gamma_str} {mirror} {kimg} {tick} {snap}'
    subprocess.run(command, shell=True)

    # Load images from outdir
    imgs = load_images_from_directory(outdir)

    # Calculate inception score
    score, std = inception_score(imgs)
    results.append((gamma, score, std))

# Print results
for gamma, score, std in results:
    print(f'Gamma: {gamma:.1f}, Inception Score: {score:.2f} +/- {std:.2f}')

