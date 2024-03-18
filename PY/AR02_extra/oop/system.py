import numpy as np
from scipy.integrate import odeint



class System():
    """
    Here, you can define your system.
    """
    def __init__(self, t0: float, dt: float, x0: np.array) -> None:
        self._A: np.array = np.array([[0, 1], [-0.2, -0.3]])
        self._B: np.array = np.array([[0], [0.15]])
        self._C: np.array = np.array([[1, 0]])

        self._dt: float    = dt    # System and simulation can have a different sample time, but this implementation is just for the same sample time.
        self._t : float    = t0
        self._u : np.array = None
        self._x : np.array = x0
        self._y : np.array = self.output(self._x, self._t, self._u)


    def system(self, x: np.array, t: float, u: np.array) -> np.array:
        Dx = self._A @ x + self._B @ u

        return Dx


    def output(self, x: np.array, t: float, u: np.array) -> None:
        y = self._C @ x

        return y


    def evolve(self, u: np.array) -> None:
        # Time evolution of the system to the next iteration.
        out = odeint(self.system, self._x, [self._t, self._t + self._dt], args=(u,))

        self._t = self._t + self._dt
        self._u = u
        self._x = out[-1]
        self._y = self.output(self._x, self._t, self._u)


    # This is how getters are defined in a "Python" way.
    @property
    def t(self):
        return self._t


    @property
    def u(self):
        return self._u


    @property
    def x(self):
        return self._x


    @property
    def y(self):
        return self._y
