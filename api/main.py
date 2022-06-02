from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from regex import P
from uvicorn import run


from model.request import RequestImageBase64
from utils.helper import read_image, string_base64_to_image
from resources import resourcePing, resourcePredict

import base64

import tensorflow as tf

app = FastAPI()

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

@app.post("/still_image_base64")
async def still_image_base64(
    request: RequestImageBase64
):
    image = read_image(string_base64_to_image(request.imageString))
    return resourcePredict.predict(image)

@app.post("/still_image")
async def still_image(
    file: UploadFile = File(...)
):
    image = read_image(await file.read())
    return resourcePredict.predict(image)
    

if __name__ == "__main__":
    run(app, host='localhost', port=8080)