# -*- coding: utf-8 -*-

%load_ext autoreload
%autoreload

import numpy as np
from scipy.integrate import odeint

import sys
sys.path.append('./misc/')

# %% ---------------------------------------------------------------------------

import plantFcns

# %% ---------------------------------------------------------------------------








# %% ---------------------------------------------------------------------------







# %% ---------------------------------------------------------------------------






# %% ---------------------------------------------------------------------------




# %% ---------------------------------------------------------------------------




# %% ---------------------------------------------------------------------------





















# %% ---------------------------------------------------------------------------






def fcn_simSch2(t_start, T_s, finalIndex, sig_r_ext):

    #-----------------------------------------

    par_L = 161.0
    par_K_0 = -3.86
    par_tau_10 = 5.66
    # par_v = 5.0

    par_K = par_K_0 * (par_v/par_L)
    par_tau_1 = par_tau_10 * (par_L/par_v)

    par_b_0 = par_K/par_tau_1
    par_a_1 = 1.0/par_tau_1



    A = np.array([[0, 1], [0, -par_a_1]])
    b = np.array([[0], [par_b_0]])
    c = np.array([[1], [0]])



    A_m = np.array([[0, 1], [-0.0025, -0.1]])
    b_m = np.array([[0], [0.0025]])

    #-----------------------------------------
    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    x_m_0 = np.zeros(b_m.shape[0])

    x_m_log = np.zeros([finalIndex, len(x_m_0)])
    x_m_log[0,:] = x_m_0

    #-------------------------
    x_0 = np.zeros(b.shape[0])

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    y_log = np.zeros([finalIndex, 1])
    y_log[0,:] = np.dot(c.T, x_0.reshape(-1,1))


    #-------------------------
    u_log = np.zeros([finalIndex, 1])
    u_log[0,:] = 0

    xf1_log = np.zeros([finalIndex, b_m.shape[0]])
    xf2_log = np.zeros([finalIndex, b_m.shape[0]])


    Theta_log = np.zeros([finalIndex, 2])
    Theta_log[0,:] = np.array([-3.8009, -143.6921])*0



    #-----------------------------------------
    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        t_log[idx,:] = timespan[-1]

        # ------------

        odeOut = odeint(plantFcns.fcn_LTIS,
                        x_log[idx-1,:],
                        timespan,
                        args=(A, b, u_log[idx-1,:])
                        )

        x_log[idx,:] = odeOut[-1,:]

        y_log[idx,:] = np.dot(c.T, x_log[idx,:].reshape(-1,1))

        # -------------------------

#


        # ------------

        # dxm = np.matmul(A_m, x_m_log[idx-1,:]) + np.matmul(b_m, [sig_r_ext[idx-1,:]])
        dxm = np.add(np.matmul(A_m, x_m_log[idx-1,:].reshape(-1,1)),
                     b_m * sig_r_ext[idx-1,:]
                     )

        x_m_log[idx,:] = x_m_log[idx-1,:] + dxm.reshape(1,-1)[0] * T_s

        # ------------

        alpha_1 = -0.025
        alpha_2 = -25


        # print -x_log[idx-1,1]

        omega = np.array([sig_r_ext[idx-1,:] - y_log[idx-1,:], [-x_log[idx-1,1]]])
        adaptErr = (y_log[idx-1, 0] - x_m_log[idx-1, 0])



        # dxf1 = np.matmul(A_m, xf1_log[idx-1,:]) + np.matmul(b_m, [omega[0,0]])
        dxf1 = np.add(np.matmul(A_m, xf1_log[idx-1,:].reshape(-1,1)),
                     (b_m/b_m[1]) * omega[0,0]
                     )
        xf1_log[idx,:] = xf1_log[idx-1,:] + dxf1.reshape(1,-1)[0] * T_s
        dTheta_1 = -alpha_1 * adaptErr * np.dot([1, 0], xf1_log[idx-1,:].reshape(-1,1))


        dxf2 = np.add(np.matmul(A_m, xf2_log[idx-1,:].reshape(-1,1)),
                     (b_m/b_m[1]) * omega[1,0]
                     )
        xf2_log[idx,:] = xf2_log[idx-1,:] + dxf2.reshape(1,-1)[0] * T_s
        dTheta_2 = -alpha_2 * adaptErr * np.dot([1, 0], xf2_log[idx-1,:].reshape(-1,1))


        Theta_log[idx,:] = np.array([
            Theta_log[idx-1, 0] + dTheta_1 * T_s,
            Theta_log[idx-1, 1] + dTheta_2 * T_s,
        ]).T





        u_log[idx,:] = np.dot(Theta_log[idx-1,:], omega)


        # ------------



        # ------------

    return [t_log, x_m_log, x_log, y_log, u_log, Theta_log, xf1_log, xf2_log]



# %% ---------------------------------------------------------------------------


sim_t_start = 0
sim_t_final = 3000
sim_T_s = 0.5
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)



# %% ---------------------------------------------------------------------------




#--------------------

# Preddefinovane signaly

period_time = 1000
period_tab = np.array([
                      [0, 5.0*np.pi/180],
                      [250, 0],
                      [500, -5.0*np.pi/180],
                      [750, 0],
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

sig_r_ext = sig_vysl








# %% ---------------------------------------------------------------------------




par_v = 5.0



# Spustenie simulacie

t_log, x_m_log, x_log, y_log, u_log, Theta_log, xf1_log, xf2_log = fcn_simSch2(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_r_ext,
    )






# %% ---------------------------------------------------------------------------

figNameNum = 1
exec(open('misc/fig_tex_03.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------

figNameNum = 2
exec(open('misc/fig_tex_04.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------



























# %% ---------------------------------------------------------------------------


sim_t_start = 0
sim_t_final = 6000
sim_T_s = 0.5
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)



# %% ---------------------------------------------------------------------------




#--------------------

# Preddefinovane signaly

period_time = 1000
period_tab = np.array([
                      [0, 5.0*np.pi/180],
                      [250, 0],
                      [500, -5.0*np.pi/180],
                      [750, 0],
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

sig_r_ext = sig_vysl

# %% ---------------------------------------------------------------------------




par_v = 2



# Spustenie simulacie

t_log, x_m_log, x_log, y_log, u_log, Theta_log, xf1_log, xf2_log = fcn_simSch2(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_r_ext,
    )






# %% ---------------------------------------------------------------------------

figNameNum = 3
exec(open('misc/fig_tex_03.py', encoding='utf-8').read())


figNameNum = 4
exec(open('misc/fig_tex_04.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------









































# %% ---------------------------------------------------------------------------


sim_t_start = 0
sim_t_final = 3000
sim_T_s = 0.5
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)



# %% ---------------------------------------------------------------------------




#--------------------

# Preddefinovane signaly

period_time = 1000
period_tab = np.array([
                      [0, 5.0*np.pi/180],
                      [250, 0],
                      [500, -5.0*np.pi/180],
                      [750, 0],
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

sig_r_ext = sig_vysl

# %% ---------------------------------------------------------------------------




par_v = 8



# Spustenie simulacie

t_log, x_m_log, x_log, y_log, u_log, Theta_log, xf1_log, xf2_log = fcn_simSch2(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_r_ext,
    )






# %% ---------------------------------------------------------------------------

figNameNum = 5
exec(open('misc/fig_tex_03.py', encoding='utf-8').read())


figNameNum = 6
exec(open('misc/fig_tex_04.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------
