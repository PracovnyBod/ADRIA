import numpy as np

from sensor import Sensor
from controller import Controller



class Logger():
    """
    This object logs all the desired quantities. Any new logged quantity should be defined 
    and processed here.
    """
    def __init__(self, sensor: Sensor, controller: Controller) -> None:
        self._t_log : list = list()    # Time
        self._u_log : list = list()    # Input
        self._x_log : list = list()    # System states
        self._y_log : list = list()    # System output
        self._ym_log: list = list()    # Model output
        self._c_log : list = list()    # Model parameters
        self._P_log : list = list()    # Covariance matrix

        self._sensor    : Sensor    = sensor
        self._controller: Controller = controller


    def record(self) -> None:
        self._t_log.append(self._sensor.t)
        self._x_log.append(self._sensor.x)
        self._y_log.append(self._sensor.y)

        self._u_log.append(self._controller.u)
        self._ym_log.append(self._controller.identification.ym)
        self._c_log.append(self._controller.identification.c)
        self._P_log.append(self._controller.identification.P)


    # This is how getters are defined in a "Python" way.
    @property
    def t_log(self) -> np.array:
        t_log = np.array(self._t_log)

        return t_log


    @property
    def u_log(self) -> np.array:
        u_log = np.array(self._u_log)

        return u_log


    @property
    def x_log(self) -> np.array:
        x_log = np.array(self._x_log)

        return x_log


    @property
    def y_log(self) -> np.array:
        y_log = np.array(self._y_log)

        return y_log


    @property
    def ym_log(self) -> np.array:
        ym_log = np.array(self._ym_log)

        return ym_log


    @property
    def c_log(self) -> np.array:
        c_log = np.array(self._c_log)

        return c_log


    @property
    def P_log(self) -> np.array:
        P_log = np.array(self._P_log)

        return P_log
