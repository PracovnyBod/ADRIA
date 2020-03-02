# -*- coding: utf-8 -*-


from figFcns_TeX import *




# %% ---------------------------------------------------------------------------





figNamePrefix = 'fig_tex_01_'

figPlotParam = fcnDefaultFigSize(7.5, 0.09, 0.92, 0.1, 0.4, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1,
                             height_ratios=[70, 30])






#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstupné signály', x=0.01, y=1.02, ha='left')


ax0.plot(t_log, sig_r_ext,
         '-', lw=0.5, dashes=[8,5], color='gray',
         label=u'$r(t)$',
         )

ax0.plot(t_log, x_m_log[:,0],
         '-k', lw=0.5, dashes=[6,3],
         label=u'$y_m(t)$',
         )


ax0.plot(t_log, y_log[:,0],
         '-k', lw=1.0,
         label=u'$y(t)$',
         )






#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Akčný zásah', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, u_log,
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
        ax.legend(handles_ax, labels_ax, loc=1, ncol=3, bbox_to_anchor=(0.98, 1.12))

    if ax == ax1:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------





#------------------

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
ax0.xaxis.set_minor_locator(AutoMinorLocator())
ax0.yaxis.set_minor_locator(AutoMinorLocator())

ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())

#------------------





# plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')
