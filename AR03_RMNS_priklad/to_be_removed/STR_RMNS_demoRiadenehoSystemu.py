# -*- coding: utf-8 -*-




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

#
# Simulacia len samotneho riadeneho systemu
#
#



# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 200
sim_T_s = 0.1
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)



# Preddefinovane signaly

tab_delt_u = np.array([
                      [0, 0],
                      [1, 1],
                      [50, 0],
                      [100, -1],
                      [150, 0],
                      ])


sig_delt_u = np.zeros([sim_finalIndex, 1])
for idx in range(sig_delt_u.shape[0]):
    lastValue = tab_delt_u[:,1][tab_delt_u[:,0]<=idx*sim_T_s ][-1]
    sig_delt_u[idx] = lastValue



sig_u_ext = sig_delt_u

# Spustenie simulacie

t_log, x_log = fcn_simSch_01_zaklad(
                    sim_t_start,
                    sim_T_s,
                    sim_finalIndex,
                    sig_u_ext,
                    )

# %% --------------------------------------------------------------------------

execfile('fig/v_fig_lenSystem.py')

# %% --------------------------------------------------------------------------


































# %% --------------------------------------------------------------------------
