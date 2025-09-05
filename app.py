import torch
import gradio as gr
from diffusers import StableDiffusionPipeline

model_id = "kianelbo/magic-rugs-sd15"

device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
).to(device)

def generate(prompt, resolution, steps, guidance):
    image = pipe(
        prompt,
        height=resolution,
        width=resolution,
        num_inference_steps=steps,
        guidance_scale=guidance
    ).images[0]
    return image

demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt", placeholder="Describe your rug or..."),
        gr.Slider(128, 1024, value=1024, step=128, label="Resolution"),
        gr.Slider(10, 50, value=30, step=1, label="Steps"),
        gr.Slider(1, 15, value=7.5, step=0.5, label="Guidance Scale"),
    ],
    outputs=gr.Image(label="Generated Image"),
    title="The Magic Rug Generator",
    description="LoRA fine-tuned diffuser on oriental rugs to generate beyond just rugs!"
)

if __name__ == "__main__":
    demo.launch()
