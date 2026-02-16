# -*- coding: utf-8 -*-

# import rozneho potrebneho...

import numpy as np
from scipy.integrate import odeint

import sys
sys.path.append('./figjobs/')

# ---------------------------------------------------------------------------

figSaveDir = './fig/'

# ---------------------------------------------------------------------------

def fcn_difRovnice_01(x, t, param_a):

    a = param_a
  

    u = 0

    dotx = a*x + u

    return dotx







# ---------------------------------------------------------------------------

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

    return [t_log, odeOut]




# ---------------------------------------------------------------------------
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 3
sim_T_s = 0.1

param_a = 1





# ---------------------------------------------------------------------------
# Simulacia

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param_a)





# ---------------------------------------------------------------------------
# Obrazok

print('----------------')

figName = 'figsc_ar02_fig00'
figNameNum = 0

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())













# -------------------------------------------------------------------------

def fcn_difRovnice_02(x, t, param_a):

    x, k = x

    a = param_a

    dotk = x**2

    u = -k*x

    dotx = a*x + u

    return [dotx, dotk]




# -------------------------------------------------------------------------

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



# -------------------------------------------------------------------------
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 5
sim_T_s = 0.05

param_a = 1



# -------------------------------------------------------------------------
# Simulacia

t_log, x_log, = fcn_simSch_02(sim_t_start, sim_t_final, sim_T_s, param_a)



# ---------------------------------------------------------------------------
# Obrazok

print('----------------')

figName = 'figsc_ar02_fig01'
figNameNum = 1

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())

# ---------------------------------------------------------------------------














# -------------------------------------------------------------------------

# testovanie pre rôzne hodnoty parametra a (parameter riadeného systému)


testPripady = {'pripad1': 2,
               'pripad2': 3,
               'pripad3': 4}


t_log_rec = np.arange(sim_t_start, sim_t_final+sim_T_s, sim_T_s).reshape(-1,1)

x_log_rec = []



for pripad, data in testPripady.items():

    param_a = data

     # Simulacia
    t_log, x_log, = fcn_simSch_02(sim_t_start, sim_t_final, sim_T_s, param_a)


    x_log_rec.append(x_log)


# ---------------------------------------------------------------------------

# Obrazok

figName = 'figsc_ar02_fig02'
figNameNum = 2

exec(open('./figjobs/' + figName + '.py', encoding='utf-8').read())

# ---------------------------------------------------------------------------
# 
