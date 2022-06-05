import tensorflow as tf
import numpy as np
import requests

from util.class_names import CLASS_NAMES

# Loading model from Endpoint
# http://localhost:8051/v1/models/${MODEL_NAME}[/versions/${VERSION}|/labels/${LABEL}]:predict
# For more infocheck https://www.tensorflow.org/tfx/serving/api_rest

ENDPOINT = "http://localhost:8501/v1/models/tomato-disease/versions/2:predict"

# Loading model locally
# MODEL = tf.keras.models.load_model("[model_path]")

class Predict:
    def predict(self, image):

        # predictions = MODEL.predict(image)
        # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        # confidence = np.max(predictions[0])

        json_data = {
            "instances": image.tolist()
        }

        response = requests.post(ENDPOINT, json=json_data)
        prediction = np.array(response.json()["predictions"][0])
        

        return {
            'class_name': CLASS_NAMES[np.argmax(prediction)],
            'confidence': np.max(prediction)
        }