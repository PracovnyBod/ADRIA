# -*- coding: utf-8 -*-


from figFcns_TeX import *




# %% ---------------------------------------------------------------------------




figPlotParam = fcnDefaultFigSize(7.2, 0.16, 0.908, 0.084, 0.45, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1,
                             height_ratios=[65, 35]
                             )





#------------------------------------------------------
ax0 = plt.subplot(subPlots[0])
#-----------------------------







ax0.plot(t_log, sig_dummy_ext[:,0],
         '-k', lw=0.5, dashes=[8,3], color='gray',
         label=u'$r(t)$',
         )


ax0.plot(t_log, y_m_log[:,0],
         '-', lw=1.5, dashes=[3,1], color='gray',
         label=u'$y_m(t)$',
         )


ax0.plot(t_log, y_log[:,0],
         '-k', lw=1.0,
         label=u'$y(t)$',
         )






#-----------------------------
ax0.set_ylabel(u'$r(t)$, $y(t)$',
            ha='left',
            rotation='horizontal',
            )




#-------------------------------------
ax0t = ax0.twinx()
#-----------------------------

ax0t.set_ylabel(u'$e_1(t)$',
            ha='right',
            va='bottom',
            rotation='horizontal',
            )

ax0t.plot(t_log, y_log - y_m_log,
         '-', lw=1.0, color='Gray', alpha=0.5,
         label=u'$e_1(t)$',
         )











#------------------------------------------------------
ax1 = plt.subplot(subPlots[1])
#-----------------------------






ax1.plot(t_log, u_log,
         '-', lw=1.0, color='red', alpha=0.6,
         label=u'$u(t)$',
         )

#-----------------------------
ax1.set_ylabel(u'$u(t)$',
            ha='left',
            rotation='horizontal',
            )




#-------------------------------------
ax1t = ax1.twinx()
#-----------------------------

ax1t.set_prop_cycle( dashes=[ [5,0], [5,0],  [5,1], [5,1],  [5,3], [5,3] ],
                      color=[ 'k',   'gray', 'k',   'gray', 'k',   'gray',],
                    )

ax1t.plot(t_log, Theta_log[:,0],
         lw=1.0, alpha=0.9, color='k',
         label=u'$\Theta_3(t)$',
         )

ax1t.plot(t_log, Theta_log[:,1],
         lw=1.0, alpha=0.9, color='k', dashes=[5,1],
         label=u'$\Theta_1(t)$',
         )

ax1t.plot(t_log, Theta_log[:,2],
         lw=1.0, alpha=0.9, color='gray',
         label=u'$\Theta_2(t)$',
         )

ax1t.plot(t_log, Theta_log[:,3],
         lw=1.0, alpha=0.9, color='gray', dashes=[5,1],
         label=u'$\Theta_4(t)$',
         )


#-----------------------------
ax1t.set_ylabel(u'$\\Theta(t)$',
    ha='right',
    va='bottom',
    rotation='horizontal',
    )













#------------------------------------------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():



    #-----------------------------

    if ax in [ax0, ax1]:

        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())

        # ax.grid(which='minor', b=False)

    if ax in [ax0]:
        ax.set_xlabel(u'čas [s]', ha='left', va='top')
        ax.xaxis.set_label_coords(1.025, -0.07)
        ax.yaxis.set_label_coords(0.01, 1.07)


    if ax in [ax1]:
        ax.set_xlabel(u'čas [s]', ha='left', va='top')
        ax.xaxis.set_label_coords(1.025, -0.13)
        ax.yaxis.set_label_coords(0.01, 1.07)




    if ax in [ax0t, ax1t]:
        fcnDefaultTwinAxisStyle(ax)


    if ax in [ax0t]:

        ax.yaxis.set_label_coords(0.99, 1.07)

    if ax in [ax1t]:

        ax.yaxis.set_label_coords(0.99, 1.07)

        # ax.yaxis.set_minor_locator(AutoMinorLocator())





    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0]:
        # ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, handletextpad=0.2, loc=2, bbox_to_anchor=(1.07, 1.00))
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, markerfirst=False, loc=1, bbox_to_anchor=(-0.099, 1.00))

    if ax in [ax0t]:
        # ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, loc=4, bbox_to_anchor=(1, 1.05))
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, handletextpad=0.2, loc=2, bbox_to_anchor=(1.07, 1.00))


    if ax in [ax1]:
    #     ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.1, 1.00))
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, markerfirst=False, loc=4, bbox_to_anchor=(-0.099, 0.00))

    if ax in [ax1t]:
        # ax.legend(['1', '2', '3', '4', '5', '6'], ncol=1, handlelength=1.2, loc=4, bbox_to_anchor=(-0.1, 0.00))
        ax.legend(['1.', '2.', '3.', '4.', '5.', '6.'], ncol=1, handlelength=1.2, loc=4, bbox_to_anchor=(1.2, 0.00))


#------------------------------------------------------




#------------------------------------------------------



#------------------------------------------------------

plt.savefig(figSaveDir + figName + '_' + '{}'.format(figNameNum) +'.pdf')
