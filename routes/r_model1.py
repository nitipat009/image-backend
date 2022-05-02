from fastapi import APIRouter, Response
from models.model1 import Model1
import io, base64
from PIL import Image
from api import remove_watermark
model1 = APIRouter(prefix="/Model1")


@model1.post('/')
async def get_Image(data:Model1) :
    image_buf = io.BytesIO(base64.decodebytes(data.image_path))
    mask_buf = io.BytesIO(base64.decodebytes(data.mask_path))
    img_str = remove_watermark(image_buf,mask_buf,data.MAX_DIM,data.REG_NOISE,data.INPUT_DEPTH,data.LR,data.SHOW_STEP,data.TRAINING_STEPS)
    return {"image" : img_str}

# def get_image()
#     image_bytes: bytes = generate_cat_picture()
#     # media_type here sets the media type of the actual response sent to the client.
#     return Response(content=image_bytes, media_type="image/png")


# @app.post("/vector_image")
# def image_endpoint(*, vector):
#     # Returns a cv2 image array from the document vector
#     cv2img = my_function(vector)
#     res, im_png = cv2.imencode(".png", cv2img)
#     return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")