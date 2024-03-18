# -*- coding: utf-8 -*-


from figFcns_TeX import *




# %% ---------------------------------------------------------------------------




figPlotParam = fcnDefaultFigSize(7.0, 0.16, 0.908, 0.084, 0.4, 13)
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
         '-', lw=2.0, dashes=[3,1], color='Gray',
         label=u'$y_m(t)$',
         )


ax0.plot(t_log, y_log[:,0],
         '-k', lw=1.0,
         label=u'$y(t)$',
         )












#------------------------------------------------------
ax1 = plt.subplot(subPlots[1])
#-----------------------------



ax1.plot(t_log, u_log,
         'k-', lw=1.0,
         label=u'$u(t)$',
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
        ax.yaxis.set_label_coords(-0.015, 1.07)


    if ax in [ax1]:
        ax.set_xlabel(u'čas [s]', ha='left', va='top')
        ax.xaxis.set_label_coords(1.025, -0.13)
        ax.yaxis.set_label_coords(-0.015, 1.07)







    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, handletextpad=0.2, loc=2, bbox_to_anchor=(1.07, 1.00))


    if ax in [ax1]:
    #     ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.1, 1.00))
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, markerfirst=False, loc=4, bbox_to_anchor=(-0.099, 0.00))



#------------------------------------------------------




#------------------------------------------------------



#------------------------------------------------------

plt.savefig(figSaveDir + figName + '_' + '{}'.format(figNameNum) +'.pdf')
