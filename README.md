# Image Generation with Stable Diffusion  
This project demonstrates how to generate images from text prompts using the Stable Diffusion model with the Hugging Face diffusers library. Stable Diffusion is a state-of-the-art text-to-image generation model that produces high-quality images based on textual descriptions. This project will guide you through setting up the environment, installing the necessary packages, and running a script to generate images.


## Introduction
Text-to-image generation is an exciting application of deep learning where a model generates images based on textual descriptions. This project utilizes the Stable Diffusion model, which is known for its ability to create detailed and coherent images from text prompts. By leveraging the Hugging Face diffusers library, we can easily integrate and use this model.

The Stable Diffusion model has various applications, including:  
⦁	Creative art generation  
⦁	Automated image synthesis for storytelling  
⦁	Generating visual content for marketing  
⦁	Enhancing user interfaces with dynamic visuals  

In this project, we will:  
⦁	Set up a Python virtual environment.  
⦁	Install the necessary dependencies.  
⦁	Write a Python script to generate images from text prompts.  
⦁	Execute the script to create and save generated images.  
Let's get started!  


## Pre-requisite
⦁	Download and install Anaconda(recommended) from their official website.   (https://www.anaconda.com/products/distribution)


## Setup
### 1. Create a folder and activate a virtual environment inside the folder
First, we need to create a folder for the project and create Python virtual environment in it to manage our project's dependencies. We'll use conda for this purpose:

(type in anaconda cmd)

#Create folder: `mkdir folder_name`      
#Navigate folder: `cd folder_name`  
#Create virtual environment: `conda create --name myenv python=3.7`  
#Activate virtual environment: `conda activate myenv`


### 2. Install the required packages
Next, we'll install the necessary Python packages: torch, diffusers, and transformers. These packages are required to run the Stable Diffusion model:

(type in anaconda cmd)  
`pip install torch diffusers transformers`


### 3. Obtain a Hugging Face API token
To use the Stable Diffusion model from Hugging Face, we need an API token. Follow these steps to obtain one:  
⦁	Go to the Hugging Face website.  
⦁	Sign up for an account or log in if you already have one.  
⦁	Navigate to your account settings and generate a new API token.  
⦁	Copy the API token; you will need it to authenticate your requests.  


## Code
Create a Python script named generate_images.py in your project folder and add the following code:  
```
import torch
from diffusers import StableDiffusionPipeline

HUGGING_FACE_API_KEY = "your_hugging_face_api_key_here"

def generate_images(prompt):
    # Load the pipeline with your Hugging Face API token
    pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=HUGGING_FACE_API_KEY)
    pipeline.to("cpu")  

    # Generate image
    with torch.no_grad():
        image = pipeline(prompt).images[0]

    # Save the generated image
    image.save("generated_image.png")

#Example usage
prompt = "<The text for which you have to generate image>"
generate_images(prompt)
```

*Note: Replace "your_hugging_face_api_key_here" with your actual Hugging Face API key.*


## Running the Project
To generate an image, run the script with: 

(type in anaconda cmd)  
`python generate_images.py`

This will generate an image based on the provided prompt and save it as generated_image.png.


## Example
The provided example prompt is:  

(type in prompt of the code)  
`"A futuristic city skyline at sunset"`

The generated image will be saved as generated_image.png in the same directory as your script.


## Notes  
⦁	Ensure that you have a valid Hugging Face API token.  
⦁	You can specify different prompts to generate various images.  


## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:  
⦁	Fork the repository.  
⦁	Create a new branch with a descriptive name (git checkout -b my-branch-name).  
⦁	Make your changes and commit them (git commit -am 'Add some feature').  
⦁	Push to the branch (git push origin my-branch-name).  
⦁	Create a new Pull Request.  

*Please make sure your code follows the project's coding standards and includes relevant tests.*
