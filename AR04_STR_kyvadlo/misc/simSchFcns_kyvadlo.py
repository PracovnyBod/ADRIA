# -*- coding: utf-8 -*-

import numpy as np

from scipy.integrate import odeint
from scipy.signal import cont2discrete


import kyvadloFcns





def fcn_simSch_STR(t_start, T_s, finalIndex, init_cond, sig_u_ext, sig_u_pb, sig_r):

    sig_y_pb = kyvadloFcns.fcn_PrevodChar(sig_u_pb)

    #-----------------------------------------
    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    x_0 = init_cond

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    #-----------------------------------------

    u_log = np.zeros([finalIndex, 1])

    #-----------------------------------------

    RMNS_theta_0 = np.array([[-1.9],
                             [ 9e-1],
                             [ 2e-5],
                             [ 2e-5]])

    RMNS_theta_log = np.zeros([finalIndex, len(RMNS_theta_0)])
    RMNS_theta_log[0,:] = RMNS_theta_0.reshape(1,-1)


    RMNS_P_0 = np.diag([10e3, 10e3, 10e3, 10e3])*0.1

    RMNS_P_log = np.zeros([finalIndex, RMNS_P_0.size])
    RMNS_P_log[0,:] = RMNS_P_0.reshape(1,-1)

    RMNS_y_predict_log = np.zeros([finalIndex, 1])

    #-----------------------------------------
    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        u = sig_u_ext[idx-1,:] + u_log[idx-1,:]

        odeOut = odeint(kyvadloFcns.fcn_difRovnice,
                        x_log[idx-1,:],
                        timespan,
                        args=(u,)
                        )

        x_log[idx,:] = odeOut[-1,:]
        t_log[idx,:] = timespan[-1]



        #--------------------
        # ALGORITMUS RMNS
        y_k = (x_log[idx,0] - sig_y_pb[idx,0])


        # osetrenie citania zo starych zapisanych (_log) hodnot:

        if idx-2 >= 0:
            h_k = np.array([[-(x_log[idx-1,0] - sig_y_pb[idx-1,0]) ],
                            [-(x_log[idx-2,0] - sig_y_pb[idx-2,0]) ],
                            [u_log[idx-1,0] - sig_u_pb[idx-1,0]],
                            [u_log[idx-2,0] - sig_u_pb[idx-2,0]],
                            ])
        else:
            h_k = np.array([[-(x_log[idx-1,0] - sig_y_pb[idx-1,0]) ],
                            [-(x_log[idx-1,0] - sig_y_pb[idx-1,0]) ],
                            [u_log[idx-1,0] - sig_u_pb[idx-1,0]],
                            [u_log[idx-1,0] - sig_u_pb[idx-1,0]],
                            ])

        theta_km1 = RMNS_theta_log[idx-1,:].reshape(4,-1)
        P_km1 = RMNS_P_log[idx-1,:].reshape(4,4)

        #----------
        e_k = y_k - np.matmul(h_k.T, theta_km1)

        # e_k = 0

        # lambdaKoef = 1
        lambdaKoef = 0.9999


        Y_k =  np.matmul(P_km1, h_k) / (lambdaKoef + np.matmul(np.matmul(h_k.T, P_km1), h_k))

        P_k = (1/lambdaKoef) * (P_km1 - np.matmul(np.matmul(Y_k, h_k.T), P_km1))
        theta_k = theta_km1 + Y_k * e_k

        #----------

        RMNS_theta_log[idx,:] = theta_k.reshape(1,-1)
        RMNS_P_log[idx,:] = P_k.reshape(1,-1)

        RMNS_y_predict_log[idx,:] = np.matmul(h_k.T, theta_km1)

        #--------------------
        # POLE PLACEMENT

        # zelany polynom:

        tmp_z, tmp_r, tmp_ts = cont2discrete(([1], np.polymul([1, 1.0/0.5], [1, 1.0/0.5])), 0.02)

        par_p1 = tmp_r[1]
        par_p2 = tmp_r[2]

        par_a1 = RMNS_theta_log[idx-1,0]
        par_a2 = RMNS_theta_log[idx-1,1]
        par_b1 = RMNS_theta_log[idx-1,2]
        par_b2 = RMNS_theta_log[idx-1,3]

        matrix_A = np.array([[     1, par_b1,      0],
                             [par_a1, par_b2, par_b1],
                             [par_a2,      0, par_b2],
                             ])

        matrix_b = np.array([[par_p1 - par_a1],
                             [par_p2 - par_a2],
                             [0],
                             ])

        # Parametre RST regulatora

        par_r1, par_s0, par_s1, = np.linalg.solve(matrix_A, matrix_b)

        par_t0 = (1 + par_p1 + par_p2)/(par_b1 + par_b2)

        par_RST = np.array([par_r1, par_s0, par_s1, par_t0])

        #--------------------
        # vypocita sa akcny zasah u(k)

        delt_y_k = (x_log[idx,0] - sig_y_pb[idx,:])
        delt_y_k1 = (x_log[idx-1,0] - sig_y_pb[idx-1,:])

        vekt_omega = np.array([-u_log[idx-1,:], -delt_y_k, -delt_y_k1, sig_r[idx,:]])

        u_akcnyZasah = np.dot(par_RST, vekt_omega)


        # osetrenie ak bolo u pocitane pre nestabil pol
        if np.any(np.absolute(np.roots([1, par_a1, par_a2]))>1):
            u_akcnyZasah = u_log[idx-1,0]

        # osetrenie ak bolo u pocitane pre nestabil nulu
        if np.any(np.absolute(np.roots([par_b1, par_b2]))>1):
            u_akcnyZasah = u_log[idx-1,0]

        # obmedzenie velkosti akcneho zasahu
        akcnyZasah_max = 9.81*2
        if u_akcnyZasah > akcnyZasah_max:
            u_akcnyZasah = akcnyZasah_max
        elif u_akcnyZasah < -akcnyZasah_max:
            u_akcnyZasah = -akcnyZasah_max


        u_log[idx,:] = u_akcnyZasah


    return [t_log, x_log, u_log, RMNS_y_predict_log, RMNS_theta_log]
