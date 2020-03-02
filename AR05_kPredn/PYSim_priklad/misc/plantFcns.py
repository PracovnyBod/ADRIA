# -*- coding: utf-8 -*-

import numpy as np

def fcn_LTIS(x, t, A, b, u):
    dotx = np.matmul(A, x) + np.matmul(b, u)
    return dotx
