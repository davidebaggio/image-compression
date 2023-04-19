from importModules import *


def get_image(filepath):
    origin = cv2.imread(filepath)
    return origin


def img_resize(image, block_size):
    h, w = np.floor(np.array(image.shape[:2])/block_size) * block_size
    return cv2.resize(image, (int(w), int(h)))


def color2YCrCb(image):
    ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    return ycrcb
