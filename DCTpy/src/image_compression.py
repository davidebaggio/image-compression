# import required libraries
from colorconversion import *
from imgDCT_IDCT import *
from quantization import *
from math import *


def img_comp(image, block_size: int, param: list, info=False):

    # extract Y, Cb, Cr channels
    y, Cr, Cb = cv2.split(image)

    # perform dct over color channels with block size
    y_dct = blocks_DCT(y, block_size)
    cr_dct = blocks_DCT(Cr, block_size)
    cb_dct = blocks_DCT(Cb, block_size)

    # quantization of matrix
    y_qdct = quantization_of_matrix(y_dct, param[0])
    cr_qdct = quantization_of_matrix(cr_dct, param[1])
    cb_qdct = quantization_of_matrix(cb_dct, param[1])

    # perform idct over color channels with block size
    backY = blocks_IDCT(y_qdct, block_size)
    backCr = blocks_IDCT(cr_qdct, block_size)
    backCb = blocks_IDCT(cb_qdct, block_size)

    # calculation of MSE and PSNR
    MSE_y = np.mean(np.square(np.subtract(y, backY)))
    MSE_Cr = np.mean(np.square(np.subtract(Cr, backCr)))
    MSE_Cb = np.mean(np.square(np.subtract(Cb, backCb)))

    MSE_p = (3/4) * MSE_y + (1/8) * (MSE_Cr + MSE_Cb)
    PSNR = 10*log10(pow(255, 2)/MSE_p)

    if info is True:
        cv2.imshow("y_dct", y_dct)
        cv2.imshow("cr_dct", cr_dct)
        cv2.imshow("cb_dct", cb_dct)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imshow("y_qdct", y_qdct)
        cv2.imshow("cr_qdct", cr_qdct)
        cv2.imshow("cb_qdct", cb_qdct)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imshow("y_back", backY)
        cv2.imshow("cr_back", backCr)
        cv2.imshow("cb_back", backCb)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        merged = cv2.merge([backY, backCr, backCb])
        final_image = cv2.cvtColor(merged, cv2.COLOR_YCrCb2BGR)
        cv2.imshow("final", final_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        cv2.imwrite("./img/final_image.jpeg", final_image)

    return np.array([MSE_p, PSNR])
