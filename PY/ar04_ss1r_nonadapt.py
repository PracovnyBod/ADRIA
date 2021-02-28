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




# %% ---------------------------------------------------------------------------
                                                                ### cellB c01 ###
def fcn_LTIS(x, t, A, b, u):
    dotx = np.matmul(A, x) + np.matmul(b, u)
    return dotx                                                ### cellE c01 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c02 ###
def fcn_simSch1(t_start, T_s, finalIndex, sig_r_ext):

    A_m = np.array([[-1]])
    b_m = np.array([[1]])

    A = np.array([[-0.55]])
    b = np.array([[1]])
    c = np.array([[1]])

    ThetaStar = np.array([[b_m[-1, 0]],[A_m[-1, 0] - A[-1, 0]]])

    #-----------------------------------------
    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    x_m_0 = np.array([0])

    x_m_log = np.zeros([finalIndex, len(x_m_0)])
    x_m_log[0,:] = x_m_0

    #-------------------------
    x_0 = np.array([0])

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    y_log = np.zeros([finalIndex, 1])
    y_log[0,:] = np.dot(c, x_0)

    #-------------------------
    u_log = np.zeros([finalIndex, 1])
    u_log[0,:] = 0

    #-----------------------------------------
    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        t_log[idx,:] = timespan[-1]

        # ------------
        odeOut = odeint(fcn_LTIS,
                        x_m_log[idx-1,:],
                        timespan,
                        args=(A_m, b_m, sig_r_ext[idx-1,:])
                        )

        x_m_log[idx,:] = odeOut[-1,:]

        # ------------
        odeOut = odeint(fcn_LTIS,
                        x_log[idx-1,:],
                        timespan,
                        args=(A, b, u_log[idx-1,:])
                        )

        x_log[idx,:] = odeOut[-1,:]
        y_log[idx,:] = np.dot(c, x_log[idx,:])

        # -------------------------

        omega = np.array([sig_r_ext[idx-1,:], y_log[idx-1,:]])

        u_log[idx,:] = np.dot(ThetaStar.T, omega)

        # ------------

    return [t_log, x_m_log, x_log, y_log, u_log]
                                                                ### cellE c02 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c03 ###
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 100
sim_T_s = 0.005
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)



# Preddefinovane signaly

period_time = 20
period_tab = np.array([
                      [0, 1],
                      [10, -1],
                      ])

sig_vysl = np.zeros([sim_finalIndex, 1])

for period in range(int(sim_t_final/period_time) + 1):


    for idx in range( int((period*period_time)/sim_T_s), int((period*period_time + period_time)/sim_T_s)):

        lastValue = period_tab[:,1][(period_tab[:,0] + (period*period_time))<=idx*sim_T_s ][-1]
        try:
            sig_vysl[idx] = lastValue
        except:
            break

sig_r_ext = sig_vysl
                                                                ### cellE c03 ###














# %% ---------------------------------------------------------------------------
                                                                ### cellB c05 ###
# Spustenie simulacie

t_log, x_m_log, x_log, y_log, u_log = fcn_simSch1(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_r_ext,
    )                                                        ### cellE c05 ###





# %% ---------------------------------------------------------------------------
                                                                ### cellB c06 ###
# Obrazok

figName = 'figsc_ar04_fig_ss1r_yu'
figNameNum = 0

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c06 ###
