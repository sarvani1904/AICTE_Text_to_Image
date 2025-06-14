
---

### 🧠 `app.py`

```python
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import uuid
import gradio as gr

pipe = StableDiffusionPipeline.from_pretrained(
    "dreamlike-art/dreamlike-photoreal-2.0", 
    torch_dtype=torch.float16
).to("cpu")  # or "cuda" if GPU is available

def generate_image(prompt):
    enhanced_prompt = f"{prompt}, ultra detailed, cinematic lighting, masterpiece, 4k, trending on ArtStation"
    image = pipe(enhanced_prompt).images[0]
    filename = f"generated_{uuid.uuid4().hex[:6]}.png"
    image.save(filename)
    return image, filename

with gr.Blocks() as demo:
    gr.Markdown("## 🎨 Text-to-Image Generator (AI Internship Project)")
    prompt_input = gr.Textbox(label="Enter your prompt")
    generate_btn = gr.Button("Generate")
    output_img = gr.Image(label="Generated Image")
    download_file = gr.File(label="Download")

    generate_btn.click(generate_image, inputs=prompt_input, outputs=[output_img, download_file])

demo.launch(share=True)
