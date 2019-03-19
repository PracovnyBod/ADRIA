# -*- coding: utf-8 -*-


from figFcns_TeX import *




# %% ---------------------------------------------------------------------------





figNamePrefix = 'fig_tex_02_'

figPlotParam = fcnDefaultFigSize(7.5, 0.09, 0.92, 0.1, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1,
                             height_ratios=[50, 50])






#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Adaptované parametre', x=0.01, y=1.02, ha='left')


ax0.plot(t_log, Theta_log[:,0],
         '-k', lw=1.0,
         label=u'$\Theta_1(t)$',
         )

ax0.plot(t_log, Theta_log[:,1],
         '-k', lw=1.0, dashes=[6,1],
         label=u'$\Theta_2(t)$',
         )


# ax0.plot(t_log, y_log[:,0],
#          '-k', lw=1.0,
#          label=u'$y(t)$',
#          )






#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Adaptačná odchýlka', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, (y_log[:, 0] - x_m_log[:, 0]),
         '-k', lw=1.0,
         label=u'$e(t)$',
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
        ax.legend(handles_ax, labels_ax, loc=1, ncol=2, bbox_to_anchor=(0.98, 1.15))

    if ax == ax1:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.15))

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
