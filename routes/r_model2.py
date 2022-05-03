import cv2
from fastapi import APIRouter, Response
from models.model2 import Model2
import io, base64
from PIL import Image
from inpaint import formatMask , remove_watermark
from helper import *
model2 = APIRouter(prefix="/Model2")


@model2.post('/')
async def get_Image(data:Model2) :
    image_buf = io.BytesIO(base64.decodebytes(data.image_path))
    mask_buf = io.BytesIO(base64.decodebytes(data.mask_path))
    image_buf = cv2.imdecode(np.frombuffer(image_buf.read(), np.uint8), 1)
    mask_buf = cv2.imdecode(np.frombuffer(mask_buf.read(), np.uint8), 1)
    add_mark = formatMask(image_buf, mask_buf)
    result = remove_watermark(add_mark)
    result = result[:,:,::-1]
    result = Image.fromarray(result)
    result = img_to_base64_str(result)
    return {"image" : result}