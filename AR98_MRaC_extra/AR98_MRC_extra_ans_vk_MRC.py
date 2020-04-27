import numpy as np

from scipy.integrate import odeint

def fcn_LTIS(x, t, A, b, u):
    dotx = np.matmul(A, x) + np.matmul(b, u)
    return dotx


def fcn_simSch2(t_start, T_s, finalIndex, sig_dummy_ext):

    #-----------------------------------------
    # Riadeny system

    A = np.array([[0, 1], [-2.6916, -2.7423]])
    b = np.array([[0], [1]])
    c = np.array([[3.5578], [0.1664]])

    #-------------------------
    # Referencny model

    A_m = np.array([[0, 1], [-3.0, -3.5]])
    b_m = np.array([[0], [1]])
    c_m = np.array([[3], [1]])

    #-------------------------
    # Pomocne filtre

    Lambda_pom = np.array([[-3]])
    q_pom = np.array([[1]])

    #----------------------------------------------------
    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    x_0 = np.zeros(b.shape[0])

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    y_log = np.zeros([finalIndex, 1])
    y_log[0,:] = np.dot(c.T, x_0.reshape(-1,1))

    #-------------------------
    x_m_0 = np.zeros(b_m.shape[0])

    x_m_log = np.zeros([finalIndex, len(x_m_0)])
    x_m_log[0,:] = x_m_0

    y_m_log = np.zeros([finalIndex, 1])
    y_m_log[0,:] = np.dot(c_m.T, x_m_0.reshape(-1,1))

    #-------------------------
    nu1_log = np.zeros([finalIndex, q_pom.shape[0]])
    nu2_log = np.zeros([finalIndex, q_pom.shape[0]])

    #-------------------------
    u_log = np.zeros([finalIndex, 1])
    u_log[0,:] = 0

    #----------------------------------------------------
    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        t_log[idx,:] = timespan[-1]

        # ------------

        odeOut = odeint(fcn_LTIS,
                        x_log[idx-1,:],
                        timespan,
                        args=(A, b, u_log[idx-1,:])
                        )

        x_log[idx,:] = odeOut[-1,:]
        y_log[idx,:] = np.dot(c.T, x_log[idx,:].reshape(-1,1))

        # -------------------------
        # Referencny model:

        ref_sig = sig_dummy_ext[idx-1, :]

        dotx_m = fcn_LTIS(x_m_log[idx-1,:], 0, A_m, b_m, ref_sig)

        x_m_log[idx,:] = x_m_log[idx-1,:] + dotx_m * T_s

        y_m_log[idx,:] = np.dot(c_m.T, x_m_log[idx,:].reshape(-1,1))

        # -------------------------
        # Pomocne filtre:

        dotnu1 = fcn_LTIS(nu1_log[idx-1,:], 0, Lambda_pom, q_pom, u_log[idx-1,:])
        nu1_log[idx,:] = nu1_log[idx-1,:] + dotnu1 * T_s

        dotnu2 = fcn_LTIS(nu2_log[idx-1,:], 0, Lambda_pom, q_pom, y_log[idx-1,:])
        nu2_log[idx,:] = nu2_log[idx-1,:] + dotnu2 * T_s

        # -------------------------
        # Vektor omega:

        omega = np.array([y_log[idx,:],
                          nu1_log[idx-1,:].reshape(-1,1),
                          nu2_log[idx-1,:].reshape(-1,1),
                          ref_sig,
                        ])

        # -------------------------
        # Vektor Theta:

        Theta = np.array([[-4.5535],
                          [-18.3809],
                          [11.8071],
                          [6.0096],
                        ])

        # -------------------------

        u_log[idx,:] = np.dot(Theta.T, omega)[0]

    return [t_log, x_log, y_log, u_log, y_m_log]

# --------------------------------------------------
# Nastavenie simulacie

sim_t_start = 0
sim_t_final = 40
sim_T_s = 0.01
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)

# Preddefinovany signal (pouzity ako referencny signal)

period_time = 20
period_tab = np.array([[0, 0.7],
                       [10, 0],
                      ])

sig_vysl = np.zeros([sim_finalIndex, 1])

for period in range(int(sim_t_final/period_time) + 1):
    for idx in range( int((period*period_time)/sim_T_s), int((period*period_time + period_time)/sim_T_s)):
        lastValue = period_tab[:,1][(period_tab[:,0] + (period*period_time))<=idx*sim_T_s ][-1]
        try:
            sig_vysl[idx] = lastValue
        except:
            break

sig_dummy_ext = sig_vysl

# Spustenie simulacie

t_log, x_log, y_log, u_log, y_m_log = fcn_simSch2(
    sim_t_start,
    sim_T_s,
    sim_finalIndex,
    sig_dummy_ext,
    )

# Tu by bolo kreslenie obrazkov...
