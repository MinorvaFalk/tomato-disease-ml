import numpy as np
import base64
import cv2

from PIL import Image
from io import BytesIO

# Open image and convert to numpy array to feed to model
def read_file_as_image(data) -> np.ndarray:
    return np.array(Image.open(BytesIO(data)))

# Model require [[]] data and 224x224 image size
def resize_to_224_and_expand(image):
    img = cv2.resize(image, (224, 224))
    img_batch = np.expand_dims(img, 0)

    return img_batch

# Extract base64 to image
def string_base64_to_image(stringImage):
    return base64.b64decode(stringImage)

def read_image(data):
    image = read_file_as_image(data)

    img = cv2.resize(image, (224, 224))
    img_batch = np.expand_dims(img, 0)

    return img_batch
