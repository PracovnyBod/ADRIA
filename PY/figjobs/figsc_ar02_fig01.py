# -*- coding: utf-8 -*-


from figFcns_TeX import *



figPlotParam = fcnDefaultFigSize(12, 0.15, 0.95, 0.06, 0.5, 13)

print(figPlotParam[0:2])

fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

print(fig)

subPlots = gridspec.GridSpec(3, 1, )


#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, x_log[:,0],
         '-', lw=0.75, color='k',
         label = u'$x(t)$'
         )

#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Akčný zásah', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, -x_log[:,1]*x_log[:,0],
         '-', lw=0.75, color='k',
         label = u'$u(t)$'
         )

#------------------
ax2 = plt.subplot(subPlots[2])

ax2.set_title(u'Adaptovaný parameter', x=0.01, y=1.02, ha='left')

ax2.plot(t_log, x_log[:,1],
         '-', lw=0.75, color='k',
         label = u'$k(t)$'
         )

#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas', ha='left', va='bottom')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0, ax1, ax2]:
        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())


    if ax in [ax0, ax1, ax2]:
        ax.xaxis.set_label_coords(1.04, -0.2)


    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0, ax1, ax2]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.04, 1.0))




#------------------

plt.savefig(figSaveDir + figName + '_' + '{}'.format(figNameNum) +'.pdf')
