"""
This is the way. The proper object-oriented Python-ish one.
"""

import numpy as np

from simulation import Simulation
from system import System
from sensor import Sensor
from controller import Identification, Controller
from plotter import Plotter



def main() -> None:
    # Yes, Python can define a variable type during a declaration as: `variable: TYPE = value`
    # and for the return type `def fun() -> TYPE`. But it is more a guideline than an actual rule.

    # Time constants
    dt    : float = 0.25                      # Sample time
    t_span: np.array = np.array([0.0, 50])    # Time span

    # Initial conditions
    x0: np.array = np.array([0.0, 0.0])    # System states

    h : np.array = np.array([[0], [0], [0], [0]])                    # h-vector
    c : np.array = np.array([[0.001], [0.001], [0.001], [0.001]])    # Model parameters
    P : np.array = np.identity(4)*10**6                              # Covariance matrix
    l : float    = 1.0                                               # Forgetting factor (lambda)

    # Everything in Python is an object. Python has two types of variables: immutable and mutable. 
    # Immutable are, for example, built-in data types (numbers, boolean, string, ...), they are passed
    # by a value. Mutable objects are passed by a reference. The user defined objects belong to 
    # this category, unless specified otherwise. For more information, read the Python documentation 
    # or try a personal consultation.
    system         = System(t0=t_span[0], dt=dt, x0=x0)
    sensor         = Sensor(system=system)
    identification = Identification(h=h, c=c, P=P, l=l)
    controller     = Controller(sensor=sensor, identification=identification)

    plotter        = Plotter()
    simulation     = Simulation(
        t_span=t_span, 
        dt=dt, 
        system=system, 
        controller=controller, 
        sensor=sensor
    )

    simulation.run()
    plotter.plot(simulation.logger)


if __name__ == "__main__":
    main()
