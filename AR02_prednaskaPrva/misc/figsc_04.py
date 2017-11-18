# coding: utf-8


# Obrazok
figNameNum = 4
figNamePrefix = 'cv00_fig_'

figPlotParam = fcnDefaultFigSize(14, 0.09, 0.91, 0.1, 0.4, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(3, 1, )

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, x_log[:,0],
         '-k',
         label = u'$x(t)$'
         )

#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Akčný zásah', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, -param_k*x_log[:,0],
         '--k',
         label = u'$u(t)$'
         )

#------------------
ax2 = plt.subplot(subPlots[2])

ax2.set_title(u'Adaptovaný parameter', x=0.01, y=1.02, ha='left')

ax2.plot(t_log, x_log[:,1],
         '-r',
         label = u'$k(t)$'
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
    else:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------

plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')
