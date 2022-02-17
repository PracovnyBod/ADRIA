# -*- coding: utf-8 -*-

# %% ---------------------------------------------------------------------------

# import rozneho potrebneho...

%load_ext autoreload
%autoreload


import numpy as np
from scipy.integrate import odeint

import sys
sys.path.append('./misc/')

# %% ---------------------------------------------------------------------------

figSaveDir = './fig/'





# %% ---------------------------------------------------------------------------
                                                                ### cellB c00 ###
A = np.array([[0, 1], [-0.2, -0.3]])
b = np.array([[0], [0.15]])                                     ### cellE c00 ###



# %% ---------------------------------------------------------------------------
                                                                ### cellB c01 ###
def fcn_difRovnice(x, t, u):

    dotx = np.dot(A,x) + np.dot(b,u)

    return dotx                                                 ### cellE c01 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c02 ###
def fcn_simSch_01_zaklad(t_start, T_s, finalIndex, sig_u_ext):

    #-----------------------------------------
    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    x_0 = np.array([0, 0])

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    #-----------------------------------------


    #-----------------------------------------
    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        u = sig_u_ext[idx-1,:]

        odeOut = odeint(fcn_difRovnice,
                        x_log[idx-1,:],
                        timespan,
                        args=(u,)
                        )

        x_log[idx,:] = odeOut[-1,:]
        t_log[idx,:] = timespan[-1]

    return [t_log, x_log]                                       ### cellE c02 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c03 ###
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 200
sim_T_s = 0.1
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1) ### cellE c03 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c04 ###
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


sig_u_ext = sig_delt_u                                          ### cellE c04 ###











# %% ---------------------------------------------------------------------------
                                                                ### cellB c05 ###
# Spustenie simulacie

t_log, x_log = fcn_simSch_01_zaklad(
                    sim_t_start,
                    sim_T_s,
                    sim_finalIndex,
                    sig_u_ext,
                    )                                           ### cellE c05 ###





# %% ---------------------------------------------------------------------------
                                                                ### cellB c06 ###
# Obrazok

figName = 'figsc_ar03_fig01'
figNameNum = 0

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c06 ###
