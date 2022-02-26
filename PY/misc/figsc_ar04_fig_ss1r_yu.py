# -*- coding: utf-8 -*-


from figFcns_TeX import *



figPlotParam = fcnDefaultFigSize(7, 0.15, 0.91, 0.1, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1,
                             height_ratios=[60, 40],
                            )


#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstupné signály', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, sig_r_ext,
        '-', lw=0.5, dashes=[8,5], color='gray', drawstyle='steps-post',
         label=u'$r(t)$',
         )

ax0.plot(t_log, x_m_log[:,0],
         '-k', lw=0.5, dashes=[6,3],
         label=u'$y_m(t)$',
         )


ax0.plot(t_log, y_log[:,0],
         '-k', lw=.75,
         label=u'$y(t)$',
         )


#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Akčný zásah', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, u_log,
         '-', lw=0.5, color='k', drawstyle='steps-post',
         label = u'$u(t)$'
         )


#------------------
# ax2 = plt.subplot(subPlots[2])
#
# ax2.set_title(u'Identifikované parametre $\Theta$', x=0.01, y=1.02, ha='left')






#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas', ha='left', va='top')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0, ax1]:
        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())


    if ax in [ax0]:
        ax.xaxis.set_label_coords(1.04, -0.08)

    if ax in [ax1]:
        ax.xaxis.set_label_coords(1.04, -0.15)


    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0, ax1]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.04, 1.0))




#------------------

plt.savefig(figSaveDir + figName + '_' + '{}'.format(figNameNum) +'.pdf')
