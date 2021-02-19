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
# Simulacna schema:

def fcn_simSch_02_lenRMNS_noise(t_start, T_s, finalIndex, sig_u_ext, lambdaKoef):

    #-----------------------------------------
    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    x_0 = np.array([0, 0])

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0


    y_log_noise = np.zeros([finalIndex, 1])
    y_log_noise[0,0] = x_log[0,0]

    #-----------------------------------------

    u_log = np.zeros([finalIndex, 1])

    #-----------------------------------------

    RMNS_theta_0 = np.array([[ 0.001],
                             [ 0.001],
                             [ 0.001],
                             [ 0.001]])


    RMNS_theta_log = np.zeros([finalIndex, len(RMNS_theta_0)])
    RMNS_theta_log[0,:] = RMNS_theta_0.reshape(1,-1)

    RMNS_P_0 = np.identity(4) * 10**2

    RMNS_P_log = np.zeros([finalIndex, RMNS_P_0.size])
    RMNS_P_log[0,:] = RMNS_P_0.reshape(1,-1)

    RMNS_y_predict_log = np.zeros([finalIndex, 1])

    #-----------------------------------------
    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        odeOut = odeint(fcn_difRovnice,
                        x_log[idx-1,:],
                        timespan,
                        args=(u_log[idx-1,:],)
                        )

        x_log[idx,:] = odeOut[-1,:]
        t_log[idx,:] = timespan[-1]

        # Tu sa umelo pridava sum k vystupnej velicine riadeneho systemu

        y_log_noise[idx,0] = x_log[idx,0] + np.random.normal(0, 0.1, size=1)

        #--------------------
        # ALGORITMUS RMNS

        # Pri RMNS sa vyuziva zasumena vystupna velicina

        y_k = y_log_noise[idx,0]

        h_k = np.array([[-y_log_noise[idx-1,0]],
                        [-y_log_noise[idx-2,0]], # pozor na idx-2 !!!
                        [u_log[idx-1,0]],
                        [u_log[idx-2,0]], # pozor na idx-2 !!!
                        ])

        theta_km1 = RMNS_theta_log[idx-1,:].reshape(4,-1)
        P_km1 = RMNS_P_log[idx-1,:].reshape(4,4)

        #----------
        e_k = y_k - np.matmul(h_k.T, theta_km1)
        Y_k =  np.matmul(P_km1, h_k) / (lambdaKoef + np.matmul(np.matmul(h_k.T, P_km1), h_k))
        P_k = (1/lambdaKoef) * (P_km1 - np.matmul(np.matmul(Y_k, h_k.T), P_km1))
        theta_k = theta_km1 + Y_k * e_k

        #----------
        RMNS_theta_log[idx,:] = theta_k.reshape(1,-1)
        RMNS_P_log[idx,:] = P_k.reshape(1,-1)

        RMNS_y_predict_log[idx,:] = np.matmul(h_k.T, theta_km1)

        #--------------------
        u_log[idx,:] = sig_u_ext[idx-1,:]

    return [t_log, x_log, RMNS_y_predict_log, RMNS_theta_log, y_log_noise]
                                                                ### cellE c02 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c03 ###
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 250
sim_T_s = 0.1
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1) ### cellE c03 ###






# %% ---------------------------------------------------------------------------
                                                                ### cellB c04 ###
# Preddefinovane signaly

period_time = 200
period_tab = np.array([
                      [0, 1],
                      [80, 0],
                      [120, -1],
                      [180, 0],
                      ])

sig_vysl = np.zeros([sim_finalIndex, 1])

for period in range(int(sim_t_final/period_time) + 1):

    for idx in range( int((period*period_time)/sim_T_s), int((period*period_time + period_time)/sim_T_s)):

        lastValue = period_tab[:,1][(period_tab[:,0] + (period*period_time))<=idx*sim_T_s ][-1]
        try:
            sig_vysl[idx] = lastValue
        except:
            break

sig_u_ext = sig_vysl                                            ### cellE c04 ###




# %% ---------------------------------------------------------------------------
                                                                ### cellB c04l ###
sim_lambdaKoef = 1.0
### cellE c04l ###








# %% ---------------------------------------------------------------------------
                                                                ### cellB c05 ###
# Spustenie simulacie

t_log, x_log, RMNS_y_predict_log, RMNS_theta_log, y_log_noise = fcn_simSch_02_lenRMNS_noise(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_u_ext,
    sim_lambdaKoef
    )                                                          ### cellE c05 ###





# %% ---------------------------------------------------------------------------
                                                                ### cellB c06 ###
# Obrazok

figName = 'figsc_ar03_fig03'
figNameNum = 0

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c06 ###












# %% ---------------------------------------------------------------------------
                                                                ### cellB c07 ###
sim_lambdaKoef = 0.987

# Spustenie simulacie

t_log, x_log, RMNS_y_predict_log, RMNS_theta_log, y_log_noise = fcn_simSch_02_lenRMNS_noise(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_u_ext,
    sim_lambdaKoef
    )

# Obrazok

figName = 'figsc_ar03_fig03'
figNameNum = 1

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())  ### cellE c07 ###




















# %% ---------------------------------------------------------------------------
                                                                ### cellB c08 ###
sim_lambdaKoef = 0.957

# Spustenie simulacie

t_log, x_log, RMNS_y_predict_log, RMNS_theta_log, y_log_noise = fcn_simSch_02_lenRMNS_noise(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_u_ext,
    sim_lambdaKoef
    )

# Obrazok

figName = 'figsc_ar03_fig03'
figNameNum = 2

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())  ### cellE c08 ###
