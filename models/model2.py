from lib2to3.pytree import Base
from fastapi import File
from pydantic import BaseModel

class Model2(BaseModel) :
    image_path : bytes  = File(...) 
    mask_path : bytes = File(...)
    BATCH_SIZE : int
    LEARNING_RATE : float 