import torch
from diffusers import StableDiffusionPipeline
import gradio as gr

# Load the model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
).to("cuda" if torch.cuda.is_available() else "cpu")

# Function to generate image
def generate_image(prompt):
    image = pipe(prompt).images[0]
    return image

# Gradio interface
interface = gr.Interface(
    fn=generate_image,
    inputs="text",
    outputs="image",
    title="Text to Image Generator using Stable Diffusion"
)

# Run app
if __name__ == "__main__":
    interface.launch(share=True)
