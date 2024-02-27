import numpy as np

from system import System
from sensor import Sensor
from controller import Controller
from logger import Logger



class Simulation():
    """
    This object puts everything together and generates a simulated output.
    """
    def __init__(self, t_span: np.array, dt: float, system: System, controller: Controller, sensor: Sensor) -> None:
        self._t_span    : float      = t_span
        self._dt        : float      = dt
        self._system    : System     = system
        self._controller: Controller = controller
        self._sensor    : Sensor     = sensor
        self._logger    : Logger     = Logger(sensor=sensor, controller=controller)


    def run(self) -> None:
        t = self._t_span[0]

        # self._logger.record(self._dt)

        while t <= self._t_span[1]:
            # Measure the current state.
            self._sensor.measure()

            # Compute the input, for the current measurement.
            u = self._controller.input()

            # Log the current simulation state.
            self._logger.record()

            # Send the input to the system.
            self._system.evolve(u)

            # Next iteration
            t = t + self._dt


    # This is how getters are defined in a "Python" way.
    @property
    def logger(self) -> Logger:
        return self._logger
