# -*- coding: utf-8 -*-








figNameNum = 1
figNamePrefix = 'v_fig_lenSystem_'

figPlotParam = fcnDefaultFigSize(10, 0.09, 0.92, 0.10, 0.4, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1,
                             height_ratios=[70, 30])

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, x_log[:,0],
         '-k', lw=1.0,
         label=u'$y(t)$',
         )

#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Vstup', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, sig_u_ext,
         '-k', lw=1.0,
         label=u'$u(t)$',
         )

#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas', x=1.05, ha='left', va='bottom')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax == ax0:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------

# plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')
