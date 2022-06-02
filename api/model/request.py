from pydantic import BaseModel
from typing import List

class RequestImageBase64(BaseModel):
    imageString: str

class RequestImageBase64Indexed(BaseModel):
    index: int
    imageString: str

class RequestImagesBase64(BaseModel):
    images: List[RequestImageBase64Indexed]

