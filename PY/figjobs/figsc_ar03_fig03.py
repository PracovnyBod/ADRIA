# -*- coding: utf-8 -*-


from figFcns_TeX import *



figPlotParam = fcnDefaultFigSize(11, 0.15, 0.94, 0.05, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(3, 1,
                            height_ratios=[40, 20, 40],
                            )


#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')

ax0.plot(t_log, y_log_noise[:,0],
         '-', lw=0.75, color='k',
         label=u'$y(t)$',
         )

ax0.plot(t_log, RMNS_y_predict_log[:,0],
         '-', color='r', lw=0.5, drawstyle='steps-post',
         label=u'$\hat y(t)$',
         )

#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Vstup', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, sig_u_ext,
         '-', lw=0.75, color='k', drawstyle='steps-post',
         label = u'$u(t)$'
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
    ax.set_xlabel(u'čas', ha='left', va='top')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0, ax1, ax2]:
        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())


    if ax in [ax0, ax2]:
        ax.xaxis.set_label_coords(1.04, -0.08)

    if ax in [ax1]:
        ax.xaxis.set_label_coords(1.04, -0.2)


    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0, ax1, ax2]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.04, 1.0))




#------------------

plt.savefig(figSaveDir + figName + '_' + '{}'.format(figNameNum) +'.pdf')
