import numpy as np

from system import System



class Sensor():
    """
    This object simulates a sensor. Measurement noise can also be implemented here.
    """
    def __init__(self, system: System) -> None:
        self._system: System = system

        self._t: float    = self._system.t
        self._u: np.array = self._system.u
        self._x: np.array = self._system.x
        self._y: np.array = self._system.y


    def measure(self) -> None:
        self._t = self._system.t
        self._u = self._system.u
        self._x = self._system.x
        self._y = self._system.y


    @property
    def system(self) -> System:
        return self._system


    @property
    def t(self) -> float:
        return self._t


    @property
    def u(self) -> np.array:
        return self._u


    @property
    def x(self) -> np.array:
        return self._x


    @property
    def y(self) -> np.array:
        return self._y
