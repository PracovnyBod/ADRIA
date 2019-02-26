
import numpy as np


A = np.array([[0, 1], [-0.2, -0.3]])
b = np.array([[0], [0.15]])


def fcn_difRovnice(x, t, u):

    dotx = np.dot(A,x) + np.dot(b,u)

    return dotx
