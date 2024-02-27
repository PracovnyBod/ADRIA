import numpy as np

from sensor import Sensor



class Identification():
    """
    Here we implement the least squares recursive filter.
    """
    def __init__(self, h: np.array, c: np.array, P: np.array, l: np.array=1.0) -> None:
        self._h: np.array = h
        self._c: np.array = c
        self._P: np.array = P

        # We want to log the previous values, so the sample has the correct timestamp.
        self._h_prev: np.array = h
        self._c_prev: np.array = c
        self._P_prev: np.array = P

        self._l: np.array = l

        self._ym: np.array = None
        self._e : np.array = None


    def least_squares_recursive_filter(self, y: np.array, u: np.array):
        # The quantities h, c, P are computed here for the next iteration. We store their previous 
        # value for the logger.
        self._h_prev = self._h
        self._c_prev = self._c
        self._P_prev = self._P

        self._ym = self._h.T @ self._c
        self._e  = y - self._ym
        self._Y  = self._P @ self._h / (self._l + self._h.T @ self.P @ self._h)
        self._P  = (self._P - self._Y @ self._h.T @ self._P) / self._l
        self._c  = self._c + self._Y @ self._e

        self._h  = np.array([-y, self._h[0], u, self._h[2]])


    # This is how getters are defined in a "Python" way.
    @property
    def c(self) -> np.array:
        c = self._c_prev.reshape(-1,)

        return c


    @property
    def P(self) -> np.array:
        return self._P_prev


    @property
    def ym(self) -> np.array:
        ym = self._ym.reshape(-1,)

        return ym



class Controller():
    """
    The system's input generation should be defined here. If the closed-loop is being simulated, 
    then a reference signal also needs to be implemented here.
    """
    def __init__(self, sensor: Sensor, identification: Identification) -> None:
        self._t_intervals: np.array = np.array(
            [
                [0 , 10],
                [10, 20],
                [20, 30],
                [30, 40],
                [40, 50]
            ]
        )
        self._u_values: np.array = np.array(
            [[1], [0], [-1], [0], [1]]
        )
        
        self._sensor        : Sensor         = sensor
        self._identification: Identification = identification
        
        self._u: np.array = None


    def input(self) -> None:
        t = self._sensor.t
        y = self._sensor.y

        self._u = self._u_values.T @ ((t >= self._t_intervals[:, 0]) * (t < self._t_intervals[:, 1]))
        self._identification.least_squares_recursive_filter(y, self._u)

        return self._u


    # This is how getters are defined in a "Python" way.
    @property
    def u(self) -> np.array:
        return self._u


    @property
    def identification(self) -> Identification:
        return self._identification
