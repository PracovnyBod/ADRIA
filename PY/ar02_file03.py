# -*- coding: utf-8 -*-

# ---------------------------------------------------------------------------

# import rozneho potrebneho...

import numpy as np
from scipy.integrate import odeint

import sys
sys.path.append('./misc/')

# ---------------------------------------------------------------------------

figSaveDir = './fig/'








# ---------------------------------------------------------------------------
                                                                ### cellB c01 ###
def fcn_difRovnice_01(x, t, a, u):

    dotx = a*x + u

    return dotx                                                 ### cellE c01 ###






# ---------------------------------------------------------------------------
                                                                ### cellB c02 ###
def fcn_simSch_03(t_start, T_s, finalIndex, param_a):

    #-----------------------------------------
    # casovy vektor

    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    # vektor stavu riadeneho systemu

    x_0 = np.array([1])

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    #-----------------------------------------
    # vektor adaptovaneho parametra

    k_log = np.zeros([finalIndex, 1])

    #-----------------------------------------
    # vektor akcneho zasahu

    u_log = np.zeros([finalIndex, 1])

    #-----------------------------------------

    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        #-------------------------------------
        # Riadeny system - simulacia (pomocou ODEsolvera)

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        odeOut = odeint(fcn_difRovnice_01,
                        x_log[idx-1,:],
                        timespan,
                        args=(param_a, u_log[idx-1,:])
                        )

        x_log[idx,:] = odeOut[-1,:]
        t_log[idx,:] = timespan[-1]

        #-------------------------------------
        # Riadiaci system:

        # zakon adaptacie:
        deltk = x_log[idx-1,:]*x_log[idx-1,:]

        # adaptovany parameter (numericka integracia - vlastne sumator)
        k_log[idx,:] = k_log[idx-1,:] +  (deltk * T_s)

        # zakon riadenia:
        u_log[idx,:] = -k_log[idx-1,:] * x_log[idx-1,:]

    return [t_log, x_log, u_log, k_log]
                                                                ### cellE c02 ###













# ---------------------------------------------------------------------------
                                                                ### cellB c03 ###
# Nastavenia simulacie
sim_t_start = 0
sim_t_final = 5
sim_T_s = 0.05
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)

param_a = 1

# Simulacia
t_log, x_log, u_log, k_log, = fcn_simSch_03(sim_t_start,
                                            sim_T_s,
                                            sim_finalIndex,
                                            param_a,
                                            )
                                                                ### cellE c03 ###





# ---------------------------------------------------------------------------
                                                                ### cellB c04 ###
figName = 'figsc_ar02_f03_f01'
figNameNum = 0

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c04 ###
