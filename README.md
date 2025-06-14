# 🧠 Text-to-Image Generator Web App

This project is a Gradio-based web application that uses the Stable Diffusion model (`dreamlike-photoreal-2.0`) to generate realistic, high-quality images from any natural language prompt.

## 🚀 Features
- Enter any creative prompt
- Enhanced prompt rendering using modifiers
- Generates realistic AI art using Stable Diffusion
- Clean and simple Gradio UI
- Downloadable output images

## 🧠 Tech Stack
- Python
- Hugging Face Diffusers
- Stable Diffusion (Dreamlike Photoreal 2.0)
- Gradio (for the web app UI)
- Google Colab (for deployment)

## 🔧 How to Run

### In Google Colab
1. Open Colab and paste `app.py` code
2. Make sure GPU is enabled (`Runtime > Change runtime type > GPU`)
3. Install dependencies:
```python
!pip install diffusers transformers accelerate gradio
