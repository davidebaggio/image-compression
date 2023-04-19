from importModules import *


def quantization_of_matrix(dct_values, thresh):
    mat = np.copy(np.abs(dct_values))
    per = np.percentile(mat, thresh)
    return dct_values * (mat > per)


def quantization_of_matrixprev(dct_values, thresh):
    thresh = thresh / 100
    return dct_values * (abs(dct_values) > (thresh * np.max(abs(dct_values))))
