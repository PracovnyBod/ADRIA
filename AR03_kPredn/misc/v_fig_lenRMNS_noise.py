# -*- coding: utf-8 -*-








# figNameNum = 1
figNamePrefix = 'v_fig_lenRMNS_noise_'

figPlotParam = fcnDefaultFigSize(13, 0.09, 0.95, 0.06, 0.45, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(3, 1,
                             height_ratios=[40, 30, 30])

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, y_log_noise[:,0],
         '-k', lw=1.0,
         label=u'$y(t)$',
         )


ax0.plot(t_log, RMNS_y_predict_log[:,0],
         # '-', color='#aaaaaa', lw=0.3, drawstyle='steps-post',
         '-', color='r', lw=0.8, drawstyle='steps-post',
         label=u'$\hat y(t)$',
         )

#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Vstup', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, sig_u_ext,
         '-k', drawstyle='steps-post', lw=1.0,
         label=u'$u(t)$',
         )


#------------------
ax2 = plt.subplot(subPlots[2])

ax2.set_title(u'Identifikované parametre $\Theta$', x=0.01, y=1.02, ha='left')

ax2.plot(t_log, RMNS_theta_log[:,0],
         '-k', drawstyle='steps-post', lw=0.5,
         label=u'$a_1$',
         )

ax2.plot(t_log, RMNS_theta_log[:,1],
         '--k', dashes=[5,1], drawstyle='steps-post', lw=0.5,
         label=u'$a_2$',
         )

ax2.plot(t_log, RMNS_theta_log[:,2],
         '-', color='#aaaaaa', drawstyle='steps-post', lw=0.5,
         label=u'$b_1$',
         )

ax2.plot(t_log, RMNS_theta_log[:,3],
         '--', color='#aaaaaa', dashes=[5,1], drawstyle='steps-post', lw=1.0,
         label=u'$b_2$',
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

# plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')
