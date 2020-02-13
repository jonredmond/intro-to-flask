import keras.backend.tensorflow_backend as tb
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import Model
from keras.layers import Input, GlobalAveragePooling2D, Dense
from keras.applications.resnet50 import ResNet50
from keras.applications import resnet50
import numpy as np
from io import BytesIO
import base64

tb._SYMBOLIC_SCOPE.value = False
model = ResNet50(weights='imagenet', include_top=True)


def classify(imageData):
    # Decoding and pre-processing base64 image
    img = image.img_to_array(image.load_img(BytesIO(base64.b64decode(imageData)),
                                            target_size=(224, 224)))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    print(img)

    predictions = model.predict(
        img)
    print(decode_predictions(predictions))
