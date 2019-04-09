import cv2
import numpy as np

def merge(*imgs) :
    length = len(imgs)
    
    
    rows = np.concatenate( (imgs[i*j], imgs[i*j+1]), axis=0