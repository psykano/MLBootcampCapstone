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

# Training loop for different gamma values
gamma_values = np.linspace(4, 10, num=7)
results = []
for gamma in gamma_values:
    gamma_str = f'--gamma={gamma}'
    command = f'python /content/drive/MyDrive/Capstone/stylegan3/train.py {outdir} {cfg} {data} {gpus} {batch} {batch_gpu} {gamma_str} {mirror} {kimg} {tick} {snap}'
    subprocess.run(command, shell=True)

    # Load images from outdir (This needs to be replaced with actual code to load images)
    imgs = load_images_from_directory(outdir)  # You need to implement this function

    # Calculate inception score
    score, std = inception_score(imgs)
    results.append((gamma, score, std))

# Print results
for gamma, score, std in results:
    print(f'Gamma: {gamma:.1f}, Inception Score: {score:.2f} +/- {std:.2f}')

