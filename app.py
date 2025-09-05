import torch
import gradio as gr
from diffusers import StableDiffusionPipeline

model_id = "kianelbo/magic-rugs-sd15"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
).to("cuda")

def generate(prompt, negative_prompt, steps, guidance, seed):
    generator = torch.manual_seed(seed) if seed != -1 else None
    image = pipe(
        prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,
        guidance_scale=guidance,
        generator=generator
    ).images[0]
    return image

demo = gr.Interface(
    fn=generate,
    inputs=[
        gr.Textbox(label="Prompt", placeholder="Describe your rug or..."),
        gr.Textbox(label="Negative Prompt", placeholder="What to avoid (optional)"),
        gr.Slider(10, 50, value=30, step=1, label="Steps"),
        gr.Slider(1, 15, value=7.5, step=0.5, label="Guidance Scale"),
        gr.Slider(-1, 999, value=-1, step=1, label="Seed (-1 = random)")
    ],
    outputs=gr.Image(label="Generated Image"),
    title="The Magic Rug Generator",
    description="LoRA fine-tuned diffuser on oriental rugs to generate beyond just rugs!"
)

if __name__ == "__main__":
    demo.launch()
