from fastapi import APIRouter, Response
from models.model2 import Model2
import io, base64
from PIL import Image

model2 = APIRouter(prefix="/Model2")


@model2.post('/')
async def get_Image(data:Model2) :
    # with open("imageToSave.png", "wb") as fh:
    #     fh.write(base64.decodebytes(data.image_path))
    return data