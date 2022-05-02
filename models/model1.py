from lib2to3.pytree import Base
from fastapi import File
from pydantic import BaseModel

class Model1(BaseModel) :
    image_path : bytes  = File(...) 
    mask_path : bytes = File(...)
    INPUT_DEPTH : int
    LR : float 
    TRAINING_STEPS : int
    SHOW_STEP : int
    REG_NOISE : float
    MAX_DIM : int