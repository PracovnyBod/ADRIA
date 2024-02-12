# -*- coding: utf-8 -*-


from figFcns_TeX import *




figPlotParam = fcnDefaultFigSize(4.5, 0.09, 0.87, 0.15, 0.4, 13)


print(figPlotParam[0:2])

fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

print(fig)

subPlots = gridspec.GridSpec(1, 1, )

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, x_log[:,0],
         '-', lw=0.75, color='k',
         label=u'$x(t)$',
         )

#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas', ha='left', va='bottom')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0]:
        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())


    if ax in [ax0]:
        ax.xaxis.set_label_coords(1.04, -0.155)


    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=1, bbox_to_anchor=(0.98, 1.12))




#------------------

plt.savefig(figSaveDir + figName + '_' + '{}'.format(figNameNum) +'.pdf')
