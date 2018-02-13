# -*- coding: utf-8 -*-
"""
@author: MT
"""




# %% --------------------------------------------------------------------------


import numpy as np
from scipy.integrate import odeint


# %% --------------------------------------------------------------------------


%matplotlib inline
# %matplotlib nbagg

# %matplotlib qt

%load_ext autoreload
%autoreload

import sys
sys.path.append('./misc/')
from figFcns import *


from simSchFcns import *

import plantFcns







# %% --------------------------------------------------------------------------

# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 500
sim_T_s = 0.1
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)


# Preddefinovane signaly

period_time = 200
period_tab = np.array([
                      [0, 1],
                      [50, 0],
                      [100, -1],
                      [150, 0],
                      ])

sig_vysl = np.zeros([sim_finalIndex, 1])

for period in range(int(sim_t_final/period_time) + 1):


    for idx in range( int((period*period_time)/sim_T_s), int((period*period_time + period_time)/sim_T_s)):

        lastValue = period_tab[:,1][(period_tab[:,0] + (period*period_time))<=idx*sim_T_s ][-1]
        try:
            sig_vysl[idx] = lastValue
        except:
            break

# %% --------------------------------------------------------------------------

sig_u_ext = sig_vysl


# %% --------------------------------------------------------------------------


# Spustenie simulacie

t_log, x_log, RMNS_y_predict_log, RMNS_theta_log, y_log_noise = fcn_simSch_02_lenRMNS_noise(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_u_ext,
    )




execfile('fig/v_fig_lenRMNS_noise.py')
