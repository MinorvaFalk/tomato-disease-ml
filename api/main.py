from fastapi import FastAPI, HTTPException, UploadFile, File, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

from model.request import RequestImageBase64, RequestImagesBase64
from utils import helpers, connManager
from resources import resourcePing, resourcePredict

import json

app = FastAPI(
    title= "Tomato Disease",
    description=
    """
    Visit localhost:8080/docs for Documentation
    """,
    version= "1.0.0"
)

# Middleware configuration
origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = methods,
    allow_headers = headers   
)


@app.get("/")
async def root():
    return resourcePing.ping()


# Handler for still image with Base64 body
@app.post("/still_image_base64")
async def still_image_base64(
    request: RequestImageBase64
):
    imageBase64 = helpers.string_base64_to_image(request.imageString)
    image = helpers.read_image(imageBase64)
    return resourcePredict.predict(image)

@app.post("/still_images_base64")
async def still_images_base64(
    request: RequestImagesBase64
):
    result = []

    for image in request.images:
        imageBase64 = helpers.string_base64_to_image(image.imageString)
        imageBase64 = helpers.read_image(imageBase64)

        predictions =  resourcePredict.predict(imageBase64)

        result.append({
            "index": image.index,
            "class_name": predictions['class_name'],
            "confidence": predictions['confidence']
        })

    return {
        "result" : result
    }


# Handler for still image with image form data
@app.post("/still_image")
async def still_image(
    file: UploadFile = File(...)
):
    image = helpers.read_image(await file.read())
    return resourcePredict.predict(image)


# Handler for web socket for live detection
@app.websocket("/ws/live_detection")
async def live_detection(websocket: WebSocket):
    await connManager.connect(websocket)

    try :
        while True:
            data = await websocket.receive_json()
            
            imageBase64 = helpers.string_base64_to_image(data["imageString"])
            image = helpers.read_image(imageBase64)

            await connManager.send_message(json.dumps(resourcePredict.predict(image)), websocket)

    except WebSocketDisconnect:
        print("Client disconnected")
        connManager.disconnect(websocket)
    

if __name__ == "__main__":
    run(app, host='localhost', port=8080)