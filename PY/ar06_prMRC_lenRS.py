# -*- coding: utf-8 -*-

# %% ---------------------------------------------------------------------------

# import rozneho potrebneho...

%load_ext autoreload
%autoreload


import numpy as np

import sys
sys.path.append('./misc/')

# %% ---------------------------------------------------------------------------

figSaveDir = './fig/'





# %% ---------------------------------------------------------------------------


# %% ---------------------------------------------------------------------------
                                                                ### cellB c01 ###

from scipy.integrate import odeint

# odeint je ODE solver a tu nim budeme riesit
# Linear Time Invariant System, a jeho zapis ako (maticova)
# sustava diferencialnych rovnic je - vid nasled. funkciu,
# pricom metoda "matmul" je samozrejme maticove nasobenie


def fcn_LTIS(x, t, A, b, u):

    dotx = np.matmul(A, x) + np.matmul(b, u)                    #|\label{fcn_LTIS}|

    return dotx

# Vytvorme teraz funkciu, ktora bude realizovat simulacnu schemu.
# Argumentami funkcie su parametre suvisiace s casom
# a vopred dane (zname) signaly.

def fcn_simSch1(t_start, T_s, finalIndex, sig_dummy_ext):       #|\label{fcn_simSch1}|

    #-----------------------------------------
    # Parametre riadeneho systemu

    A = np.array([[0, 1], [-2.6916, -2.7423]])
    b = np.array([[0], [1]])
    c = np.array([[3.5578], [0.1664]])

    #----------------------------------------------------
    # Do pola t_log sa bude logovat cas. Pole ma finalIndex
    # riadkov a 1 stlpec a je plne nul. Potom sa na prvu
    # poziciu (index 0) zapise hodnota t_start

    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    # Zaciatocne podmienky pre stavovy vektor nech su x_0
    # co je vektor rovnako velky ako vektor b

    x_0 = np.zeros(b.shape[0])

    # Stavovy vektor sa bude logovat do pola x_log s prislusnym
    # poctom stlpcov (detto y_log pre vyst. velicinu)

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    y_log = np.zeros([finalIndex, 1])
    y_log[0,:] = np.dot(c.T, x_0.reshape(-1,1))

    #-------------------------

    u_log = np.zeros([finalIndex, 1])
    u_log[0,:] = 0

    #----------------------------------------------------
    # Jedna iteracia for cyklu je posun v case o T_s.
    # ODE solver hlada riesenie pre casovy rozsah timespan.
    # Pred danou iteraciou pozname vsetko z predchadzajucej
    # iteracie (idx-1)
    # Pocas iteracie si _log-ujeme "vysledky"

    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        t_log[idx,:] = timespan[-1]
        # posledny prvok v poli je zapisany (logovany)

        # ------------
        # solver odeint pouzije fcn_LTIS, zaciatocne podmienky
        # stavu su z predch. iteracie (x_log[idx-1,:]), riesi
        # na casovom rozsahu timespan a dalej (do fcn_LTIS) sa
        # posunu uvedene parametre/hodnoty (args)

        odeOut = odeint(fcn_LTIS,
                        x_log[idx-1,:],
                        timespan,
                        args=(A, b, u_log[idx-1,:])
                        )

        x_log[idx,:] = odeOut[-1,:]
        # odeOut obsahuje hodnoty stavu x pre cely timespan,
        # ale zapisujeme len poslednu hodnotu stavu x

        y_log[idx,:] = np.dot(c.T, x_log[idx,:].reshape(-1,1))
        # okrem stavu (stavovych velicin) chceme aj
        # vystupnu velicinu y

        # -------------------------

        u_log[idx,:] = sig_dummy_ext[idx,:]
        # v tejto simulacii len citame "externy" signal
        # a pouzivame ho ako vstup do systemu


    return [t_log, x_log, y_log, u_log, ]



# Vytvorme teraz vsetko potrebne pre "spustenie" simulacie,
# teda pre zavolanie prave vytvorenej funkcie fcn_simSch1.
# Hovorme tomu "nastavenie simulacie". Casove nastavenie:

sim_t_start = 0
sim_t_final = 40
sim_T_s = 0.05
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1)


# Dalej je potrebne vytvorit (vopred znamy) signal.
# Co sa tu deje ponechajme bez komentara, ale vysledkom
# je proste "signal" pouzitelny v simulacii...

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


# Teraz mozme "spustit" simulaciu:

t_log, x_log, y_log, u_log, = fcn_simSch1(
                                    sim_t_start,
                                    sim_T_s,
                                    sim_finalIndex,
                                    sig_dummy_ext,
                                    )
                                                                ### cellE c01 ###

# %% ---------------------------------------------------------------------------
                                                                ### cellB c06 ###
# Obrazok

figName = 'figsc_ar06_MRC_lenRS'
figNameNum = 1

exec(open('./misc/' + figName + '.py', encoding='utf-8').read())
                                                                ### cellE c06 ###


# %% ---------------------------------------------------------------------------
