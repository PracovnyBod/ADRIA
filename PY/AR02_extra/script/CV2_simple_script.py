# %% Import
import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt



# %% Initialization
# State-space representation
A = np.array([[0, 1], [-0.2, -0.3]])
B = np.array([[0], [0.15]])
C = np.array([[1, 0]])


def system(x, t, u):
    # Inputs:
    #     t ... current time, obligatory positional argument for "odeint"
    #     x ... current system state, obligatory positional argument for "odeint", must be a 1D-array
    #     u ... optional argument to the function, must be a 1D-array
    #
    # Output:
    #     Dx ... system time derivative, must be a 1D-array, obligatory output for "odeint"

    Dx = A @ x + B @ u
    
    return Dx


# Log variables declaration
t_log  = list()    # Time
x_log  = list()    # System states
y_log  = list()    # System output
ym_log = list()    # Model output
u_log  = list()    # Input
c_log  = list()    # Model parameters
P_log  = list()    # Covariance matrix

# Time constants
dt = 0.25             # Sample time
t_span = [0.0, 50]    # Time span
t = t_span[0]         # Initial time

# Initial conditions
x = np.array([0.0, 0.0])    # System states
y = C @ x                   # System outputs

h = np.array([[0], [0], [0], [0]])                    # h-vector
c = np.array([[0.001], [0.001], [0.001], [0.001]])    # Model parameters
P = np.identity(4)*10**6                              # Covariance matrix
l = 1.0                                               # Forgetting factor (lambda)

ym = h.T @ c            # Model outputs

# Input
t_intervals = np.array ([
    [0 , 10],
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50]
])
u_values = np.array(
    [[1], [0], [-1], [0], [1]]
)


# %% Simulation
while t <= t_span[1]:
    # Measurement =========================================================== #
    # Here the system measurement can be simulated. For example we can add a noise here.
    t = t
    x = x
    y = y

    # Input ================================================================= #
    # Here we can define the system input / control law.
    u = u_values.T @ ((t >= t_intervals[:, 0]) * (t < t_intervals[:, 1]))

    # Recursive least squares filter ======================================== #
    # This section is for the continuous identification of the system.
    c_prev = c
    h_prev = h
    P_prev = P

    ym  = h.T @ c
    e = y - ym
    Y = P @ h / (l + h.T @ P @ h)
    P = (P - Y @ h.T @ P) / l
    c = c + Y @ e
    h = np.array([-y, h[0], u, h[2]])

    # Logging =============================================================== #
    # Log the desired quantities.
    t_log.append(t)
    x_log.append(x)
    y_log.append(y)
    ym_log.append(ym)
    u_log.append(u)
    c_log.append(c_prev)
    P_log.append(P_prev)

    # Numerical integration ================================================= #
    # This section simulates sending the input to a real system.
    out = odeint(system, x, np.array([t, t + dt]), args=(u,))
    x   = out[-1]    # Unravel system states
    y   = C @ x

    # Next iteration ======================================================== #
    # This tracks the current time of the simulation.
    t = t + dt

# Conversion to a numpy array - better slicing than a list. The array slicing can be helpful during plotting.
t_log  = np.array(t_log)
x_log  = np.array(x_log)
y_log  = np.array(y_log)
ym_log = np.array(ym_log)
u_log  = np.array(u_log)
c_log  = np.array(c_log)
P_log  = np.array(P_log)

ym_log = ym_log.reshape(-1, 1)   # Unravel output
c_log  = c_log.reshape(-1, 4)    # Unravel parameters


# %% Plot
fig = plt.figure(figsize=[7, 5])
axes = fig.subplots(2)
fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, hspace=0.3)

axes[0].plot(t_log, y_log)
axes[0].step(t_log, ym_log)
axes[0].plot(t_log, u_log)
axes[0].set_xlabel(r"$t$")
axes[0].legend([r"$y$", r"$y_m$", r"$u$"])
axes[0].grid()
axes[0].minorticks_on()
axes[0].spines['right'].set_visible(False)
axes[0].spines['top'].set_visible(False)

axes[1].step(t_log, c_log)
axes[1].set_xlabel(r"$t$")
axes[1].legend([r"$a_1$", r"$a_2$", r"$b_1$", r"$b_2$"])
axes[1].grid()
axes[1].minorticks_on()
axes[1].spines['right'].set_visible(False)
axes[1].spines['top'].set_visible(False)

plt.show()
