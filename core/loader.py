import cv2 as cv

def load_image(path):
    img = cv.imread(str(path))
    if img is None:
        raise FileNotFoundError("Could Not Find Image")
    
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    return img_rgb