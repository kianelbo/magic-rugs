---
title: Magic Rugs Generator
emoji: 🧿
sdk: gradio
sdk_version: 5.44.1
app_file: app.py
license: cc0-1.0
---

# 🧿 Magic Rugs
I am fascinated with Persian rugs, so at first I decided to make a _thisrugdoesnotexist.com_!  
But there were no public dataset of rug images so I gathered one myself. The images are scraped from https://www.rugvista.com/.  
Then, I fine-tuned a stable diffusion model using LoRA with moderate success on rug generation.  
However, the model produces more interesting results when you ask it to generate other things!

<img src="https://media.githubusercontent.com/media/kianelbo/magic-rugs/refs/heads/main/samples/rug_dataset.jpg" alt="rug from the dataset" width="200"/><img src="https://media.githubusercontent.com/media/kianelbo/magic-rugs/refs/heads/main/samples/rug_generated.jpg" alt="generated rug" width="200"/><img src="https://media.githubusercontent.com/media/kianelbo/magic-rugs/refs/heads/main/samples/trees.jpg" alt="generated trees" width="200"/>

## The Dataset
The dataset is composed of 1000 square-padded rug images, all from top view in jpg format. The images are 1024x1024 and in 10 different styles (denoted by file names).  
The dataset is available [here](https://www.kaggle.com/datasets/kianeliasi/oriental-rug-images).

## The Model
A pre-trained stable diffusion 1.5 was used as the base model, further trained with LoRA (config available in the fine-tuning notebook) on the dataset. As this a text-to-image model, a prompt is needed. Therefore, prompts other than rugs can be used to generate odd images influenced by the learnt intricate floral patterns of rugs.  
The full merged model is uploaded and [available at Hub](https://huggingface.co/kianelbo/magic-rugs-sd15).

A working demo is also [available at Spaces](https://huggingface.co/spaces/kianelbo/magic-rugs-generator). Unfortunately, since it is on free cpu tier it takes ages to generate.
