import tensorflow as tf
import numpy as np

from utils.class_names import CLASS_NAMES

MODEL = tf.keras.models.load_model("./models/3/pb/")

class Predict:
    def predict(self, image):
        predictions = MODEL.predict(image)
    
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])

        return {
            'class_name': predicted_class,
            'confidence': float(confidence)
        }