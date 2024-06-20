import torch
from diffusers import StableDiffusionPipeline

HUGGING_FACE_API_KEY = "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"

def generate_images(prompt):
    # Load the pipeline with your Hugging Face API token
    pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=HUGGING_FACE_API_KEY)
    pipeline.to("cpu")  

    # Generate image
    with torch.no_grad():
        image = pipeline(prompt).images[0]

    # Save the generated image
    image.save("generated_image.png")

# Example usage
prompt = "A futuristic city skyline at sunset"
generate_images(prompt)
