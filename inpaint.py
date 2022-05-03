import tensorflow as tf
from tensorflow import keras

import os
import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

from tensorflow.keras import backend as K
from tensorflow.keras.layers import InputSpec
from tensorflow.keras.layers import Conv2D

## For more information into formulation: https://www.youtube.com/watch?v=AZr64OxshLo
## Metric
def dice_coef(y_true, y_pred):
    y_true_f = keras.backend.flatten(y_true)
    y_pred_f = keras.backend.flatten(y_pred)
    intersection = keras.backend.sum(y_true_f * y_pred_f)
    return (2. * intersection) / (keras.backend.sum(y_true_f + y_pred_f))

# ==================================================================== #

def showImg(img) :
    plt.figure(figsize=(20, 20))
    plt.subplot(1, 1, 1)
    plt.imshow(img)
    plt.axis('off')
    plt.title("")    
    plt.show()
    
def plotImg(img_set, dim=(4, 4), figsize=(20, 20)) :
    count = 0
    plt.figure(figsize=figsize)
    for i in range(dim[0]) :
        for j in range(dim[1]) :
            plt.subplot(dim[0], dim[1], count + 1)
            plt.imshow(img_set[count % len(img_set)])
            plt.title("")
            count += 1
    plt.show()
            
# ==================================================================== #

model = tf.keras.models.load_model('model2.h5', custom_objects={"dice_coef": dice_coef})

def scale(data: np.array, from_range = (0, 255), to_range = (0, 1), dtype=np.float64) -> np.array :
    return np.array(((data - from_range[0]) / (from_range[1] - from_range[0])) * (to_range[1] - to_range[0]) + to_range[0], dtype=dtype)

def remove_watermark(input_img) :
    return np.array(scale(model.predict(np.expand_dims(input_img, axis=0))[0], from_range=(0, 1), to_range=(0, 255)), np.uint8)

def resizeImg(img) :
    return cv.resize(img, (32, 32))

def resizeMask(mask) :
    return cv.resize(mask, (32, 32), interpolation=cv.INTER_NEAREST)

def formatMask(img, mask) :
    return scale(resizeImg(img) & resizeMask(mask))

# if __name__ == "__main__" :
#     scale_ratio = 0.5
#     img = cv.imread('img_2.jpg')
#     mask = cv.imread('img_2_mask.jpg')
#     add_mark = formatMask(img, mask)
#     result = remove_watermark(add_mark)
#     plotImg([img[:,:,::-1], mask, add_mark[:,:,::-1], result[:,:,::-1]], dim=(1, 4))