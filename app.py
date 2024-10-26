# Import libraries
import os
import io
from PIL import Image
import base64
from dotenv import load_dotenv, find_dotenv
import requests, json
import gradio as gr
from helpers.api_helpers import captioner, generate, caption_and_generate

with gr.Blocks() as demo:
    gr.Markdown("# Describe-and-Generate game- By Karan Shrestha")
    image_upload = gr.Image(label=
          "Your first image",type="pil")
    btn_all = gr.Button("Caption and generate")
    caption = gr.Textbox(label="Generated caption")
    image_output = gr.Image(label="Generated Image")
    audio_output = gr.Audio(label="Generated Audio")

    btn_all.click(fn=caption_and_generate, 
      inputs=[image_upload], 
          outputs=[caption, image_output,audio_output])

gr.close_all()
demo.launch(share=True, server_port=int(os.environ['PORT3']))
















# Load API Key from .env file
# _ = load_dotenv(find_dotenv())  # read local .env file
# hf_api_key = os.environ['HF_API_KEY']

# # Helper function to call Hugging Face API endpoints
# def get_completion(inputs, parameters=None, ENDPOINT_URL=""):
#     headers = {
#         "Authorization": f"Bearer {hf_api_key}",
#         "Content-Type": "application/json"
#     }
#     data = {"inputs": inputs}
#     if parameters is not None:
#         data.update({"parameters": parameters})
#     response = requests.post(ENDPOINT_URL, headers=headers, data=json.dumps(data))
#     return json.loads(response.content.decode("utf-8"))

# Define endpoint URLs for text-to-image and image-to-text models
# TTI_ENDPOINT = os.environ['HF_API_TTI_BASE']  # Text-to-image API endpoint
# ITT_ENDPOINT = os.environ['HF_API_ITT_BASE']  # Image-to-text API endpoint

# Image and caption handling functions
# def image_to_base64_str(pil_image):
#     byte_arr = io.BytesIO()
#     pil_image.save(byte_arr, format='PNG')
#     byte_arr = byte_arr.getvalue()
#     return base64.b64encode(byte_arr).decode('utf-8')

# def base64_to_pil(img_base64):
#     base64_decoded = base64.b64decode(img_base64)
#     byte_stream = io.BytesIO(base64_decoded)
#     return Image.open(byte_stream)

# def captioner(image):
#     base64_image = image_to_base64_str(image)
#     result = get_completion(base64_image, None, ITT_ENDPOINT)
#     return result[0]['generated_text']

# def generate(prompt):
#     output = get_completion(prompt, None, TTI_ENDPOINT)
#     result_image = base64_to_pil(output['generated_image_base64'])
#     return result_image

# # Gradio interface setup
# def caption_and_generate(image):
#     caption = captioner(image)
#     generated_image = generate(caption)
#     return [caption, generated_image]

# Initial setup - Simple captioning only
# with gr.Blocks() as demo_caption:
#     gr.Markdown("# Describe-and-Generate Game 🎲")
#     image_upload = gr.Image(label="Upload your first image", type="pil")
#     btn_caption = gr.Button("Generate Caption")
#     caption_output = gr.Textbox(label="Generated Caption")
    
#     btn_caption.click(fn=captioner, inputs=[image_upload], outputs=[caption_output])

# gr.close_all()
# demo_caption.launch(share=True, server_port=int(os.environ['PORT1']))

# # Full game loop - Caption and image generation
# with gr.Blocks() as demo_full:
#     gr.Markdown("# Describe-and-Generate Game 🎲")
#     image_upload = gr.Image(label="Upload your first image", type="pil")
#     btn_caption = gr.Button("Generate Caption")
#     caption_output = gr.Textbox(label="Generated Caption")
#     btn_image = gr.Button("Generate Image")
#     image_output = gr.Image(label="Generated Image")
    
#     btn_caption.click(fn=captioner, inputs=[image_upload], outputs=[caption_output])
#     btn_image.click(fn=generate, inputs=[caption_output], outputs=[image_output])

# gr.close_all()
# demo_full.launch(share=True, server_port=int(os.environ['PORT2']))

# Streamlined combined version - Single button for caption and generation

# with gr.Blocks() as demo_combined:
#     gr.Markdown("# Describe-and-Generate Game 🎲")
#     image_upload = gr.Image(label="Upload your first image", type="pil")
#     btn_combined = gr.Button("Caption and Generate")
#     caption_output = gr.Textbox(label="Generated Caption")
#     image_output = gr.Image(label="Generated Image")
    
#     btn_combined.click(fn=caption_and_generate, inputs=[image_upload], outputs=[caption_output, image_output])

# gr.close_all()
# demo_combined.launch(share=True, server_port=int(os.environ['PORT3']))

# def caption_and_generate(image):
#     caption = captioner(image)
#     image = generate(caption)
#     return [caption, image]
# from diffusers import DiffusionPipeline
# load_dotenv()
# hf_token = os.getenv("HF_API_KEY")
# pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-3.5-large",)

# prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
# image = pipe(prompt).images[0]