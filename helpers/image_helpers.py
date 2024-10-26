from PIL import Image
import io
import base64

def image_to_base64_str(pil_image):
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    byte_arr = byte_arr.getvalue()
    return base64.b64encode(byte_arr).decode('utf-8')

def base64_to_pil(img_base64):
    byte_stream = io.BytesIO(base64.b64decode(img_base64))
    return Image.open(byte_stream)
