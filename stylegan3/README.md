#### StyleGAN3 Perfume Generation

Generate perfume using a model trained by StyleGAN3 architecture on custom perfume training dataset.

Latest model was trained for 531 generations for a duration of approx. 4 days.

Output can be found at: https://github.com/psykano/MLBootcampCapstone/tree/main/models/stylegan3
* `network-snapshot-####.pkl` are the model files
* `fakes####.png` are the output images
* `####` designates the training generation

Hyperparameters:
* `gamma`: R1 regularization weight
Should be at least 8 since images are 512x512
* `kimg`: Training iterations (or generations)
* `snap`: How often to save a snapshot of the model based on `tick`

Source: https://github.com/NVlabs/stylegan3