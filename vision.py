
import mss
from PIL import Image
import io
import base64

def capture_screen() -> Image.Image:
	"""
	Captures the current screen and returns a Pillow Image object.
	"""
	with mss.mss() as sct:
		monitor = sct.monitors[1]  # Primary monitor
		sct_img = sct.grab(monitor)
		img = Image.frombytes('RGB', sct_img.size, sct_img.rgb)
		return img

def image_to_base64_data_uri(img: Image.Image) -> str:
	"""
	Converts a Pillow Image to a base64-encoded PNG data URI.
	"""
	buffered = io.BytesIO()
	img.save(buffered, format="PNG")
	img_bytes = buffered.getvalue()
	base64_str = base64.b64encode(img_bytes).decode('utf-8')
	return f"data:image/png;base64,{base64_str}"
