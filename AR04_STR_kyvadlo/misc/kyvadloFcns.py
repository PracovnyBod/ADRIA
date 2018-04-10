
import numpy as np

m = 1
l = 1
g = 9.81
beta = 2 * 0.33 *np.sqrt(g/l)





def fcn_difRovnice(x, t, u):

    x_1, x_2 = x

    dotx_1 = x_2
    dotx_2 = -(beta/m*l**2) * x_2 - (g/l) * np.sin(x_1) + (1/m*l**2) * u

    return [dotx_1, dotx_2]





def fcn_PrevodChar(u_pb_vals):

    y_pb_vals = np.arcsin((1.0/(m*l*g)) * u_pb_vals )

    return y_pb_vals
