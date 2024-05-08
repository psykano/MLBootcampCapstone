#### Q&A

**Question:** Why not use the text descriptions from the dataset?
**Answer:** Because general, consistent descriptions of the image are needed for Stable Diffusion LoRA and none of the fields in of text in the dataset abide by those requirements.

**Question:** Did you used the entire dataset?
**Answer:** Yes, the entire dataset was able to be used as, when only using a small percentage (10 images) the time to train the model was approx. 1.2 minutes leading to the prediction that training the model using the entire dataset (approx. 2000 images) would take less than a day.