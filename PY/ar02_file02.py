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
def fcn_difRovnice_01(x, t, param_a):

    a = param_a

    u = 0

    dotx = a*x + u

    return dotx                                                 ### cellE c01 ###








# ---------------------------------------------------------------------------
                                                                ### cellB c02 ###
def fcn_simSch_01(t_start, t_final, T_s, param_a):

    #-----------------------------------------
    t_log = np.arange(sim_t_start, sim_t_final+sim_T_s, sim_T_s).reshape(-1,1)

    #-----------------------------------------
    x_0 = 1

    #-----------------------------------------
    odeOut = odeint(fcn_difRovnice_01,
                    x_0,
                    t_log[:,0],
                    args=(param_a,)
                    )

    return [t_log, odeOut]                                      ### cellE c02 ###









# ---------------------------------------------------------------------------
                                                                ### cellB c03 ###
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 3
sim_T_s = 0.1

param_a = -1

# -----------------------------------------------------------

# Simulacia

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param_a)
                                                                ### cellE c03 ###







# ---------------------------------------------------------------------------
                                                                ### cellB c04 ###
# Obrazok

figName = 'figsc_ar02_fig03'
figNameNum = 0

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c04 ###





# ---------------------------------------------------------------------------
                                                                ### cellB c05 ###
param_a = 1

# Simulacia

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param_a)

# Obrazok

figName = 'figsc_ar02_fig03'
figNameNum = 1

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c05 ###







# ---------------------------------------------------------------------------
                                                                ### cellB c05 ###
param_a = 1

# Simulacia

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param_a)

# Obrazok

figName = 'figsc_ar02_fig03'
figNameNum = 2

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c05 ###







# ---------------------------------------------------------------------------
                                                                ### cellB c06 ###
def fcn_difRovnice_02(x, t, param_a):

    x, k = x

    a = param_a

    dotk = x**2

    u = -k*x

    dotx = a*x + u

    return [dotx, dotk]
                                                                ### cellE c06 ###






# ---------------------------------------------------------------------------
                                                                ### cellB c07 ###
def fcn_simSch_02(t_start, t_final, T_s, param_a):

    #-----------------------------------------
    t_log = np.arange(sim_t_start, sim_t_final+sim_T_s, sim_T_s).reshape(-1,1)

    #-----------------------------------------
    x_0 = [1, 0]

    #-----------------------------------------
    odeOut = odeint(fcn_difRovnice_02,
                    x_0,
                    t_log[:,0],
                    args=(param_a,)
                    )

    return [t_log, odeOut]
                                                                ### cellE c07 ###






# ---------------------------------------------------------------------------
                                                                ### cellB c08 ###
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 5
sim_T_s = 0.05

# Simulacia

t_log, x_log, = fcn_simSch_02(sim_t_start, sim_t_final, sim_T_s, param_a)
                                                                ### cellE c08 ###




# ---------------------------------------------------------------------------
                                                                ### cellB c09 ###
# Obrazok

figName = 'figsc_ar02_fig01'
figNameNum = 3

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c09 ###
