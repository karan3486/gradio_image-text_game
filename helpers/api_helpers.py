import requests
import json
import os
from dotenv import load_dotenv
from PIL import Image
import io
import base64
# Load environment variables
load_dotenv()

hf_api_key = os.environ['HF_API_KEY']
def compress_image(image, max_size=(512, 512), quality=70):
    # Resize image if it exceeds max size
    image.thumbnail(max_size, Image.LANCZOS)
    
    # Save the image to a bytes buffer with compression
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=quality)
    
    # Convert the compressed image to Base64
    byte_data = buffer.getvalue()
    base64_image = base64.b64encode(byte_data).decode("utf-8")
    
    return base64_image

def get_completion(inputs, parameters=None, ENDPOINT_URL="",isImage=False):
    headers = {
        "Authorization": f"Bearer {hf_api_key}",
        "Content-Type": "application/json"
    }
    data = {"inputs": inputs}
    if parameters is not None:
        data.update({"parameters": parameters})

    response = requests.post(ENDPOINT_URL, headers=headers, data=json.dumps(data))
    if isImage: return response.content
    return response.json()

# Function to caption an image
def captioner(image):
    from helpers.image_helpers import image_to_base64_str
    # base64_image = image_to_base64_str(image)
    compressed_image = compress_image(image)
    result = get_completion(compressed_image, None, os.environ['HF_API_ITT_BASE'])
    return result[0]['generated_text']

# Function to generate an image from a prompt
def generate(prompt):
    import io
    from PIL import Image
    from datetime import datetime
    save_folder = 'generated_images'
    
    from helpers.image_helpers import base64_to_pil
    output = get_completion(prompt, None, os.environ['HF_API_TTI_BASE'],True)
    image = Image.open(io.BytesIO(output))
    filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
    save_path = os.path.join(save_folder, filename)
    
    # Save the image to the specified folder
    image.save(save_path, format="JPEG")
    return image

def text_to_audio(caption):
    result = get_completion(caption, None, os.environ['HF_API_TTS_BASE'],True)
    return result

# Function to handle both captioning and generating image
def caption_and_generate(image):
    caption = captioner(image)
    generated_image = generate(caption)
    audio_data = text_to_audio(caption)
    return [caption, generated_image, audio_data]
