# 📦 Install the libraries
!pip install --quiet diffusers transformers accelerate

# 🧠 Import tools
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import IPython.display as display
from google.colab import files
import uuid

# ✨ Load a better photorealistic model
print("🔄 Loading dreamlike-photoreal-2.0...")
pipe = StableDiffusionPipeline.from_pretrained(
    "dreamlike-art/dreamlike-photoreal-2.0",
    torch_dtype=torch.float16
).to("cuda")
print("✅ Model loaded!")

# 🚀 Loop for user prompts
while True:
    prompt = input("✏️ Enter your prompt (or 'exit'): ").strip()
    if prompt.lower() == "exit":
        print("👋 Done!")
        break
    if not prompt:
        print("⚠️ Enter something meaningful.")
        continue

    # 🔧 Auto-enhance the prompt
    enhanced_prompt = f"{prompt}, ultra detailed, cinematic lighting, 4k, trending on ArtStation, masterpiece"

    print(f"\n🖼️ Generating for: {enhanced_prompt}\n")

    # 🎲 Try 3 versions of each image
    for i in range(1, 4):
        with torch.autocast("cuda"):
            image = pipe(enhanced_prompt).images[0]

        filename = f"gen_{uuid.uuid4().hex[:6]}_{i}.png"
        image.save(filename)
        display.display(image)
        print(f"📸 Saved image {i}: {filename}")
        files.download(filename)

    print("✅ Prompt complete. Ready for next!\n")
