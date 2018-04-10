# -*- coding: utf-8 -*-




figNamePostfix = ''
figNamePrefix = 'Obr_'
figPlotParam = fcnDefaultFigSize(20, 0.09, 0.95, 0.06, 0.25, 13)
fig = plt.figure(figNumNb, figsize=figPlotParam[0:2], dpi=97)

subPlots = gridspec.GridSpec(3, 4, height_ratios=[60, 10, 30])

#------------------
# ax0 = plt.subplot(subPlots[0])
ax0 = plt.subplot(subPlots[0, :])


ax0.set_title(u'Poloha kyvadla $\\varphi(t)$', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'uhol [°]', y=1.02, ha='right', va='bottom', rotation='vertical', )

ax0.plot(t_log, kyvadloFcns.fcn_PrevodChar(sig_u_pb)*180/np.pi,
         '--r', drawstyle='steps-post',
         label=u'$y_{PB}(t)$',
         )


ax0.plot(t_log, (sig_r +  (kyvadloFcns.fcn_PrevodChar(sig_u_pb)))*180/np.pi,
         '-b', lw=0.5, drawstyle='steps-post',
         label=u'$r(t)$',
         )

ax0.plot(t_log, x_log[:,0] *180/np.pi,
         '-k', lw=0.8,
         label=u'$y(t)$',
         )


# ax0.set_ylim([30-10, 30+25])
ax0.set_ylim([10, 90])

#------------------
ax1 = plt.subplot(subPlots[1, :])

ax1.set_title(u'Vstupný moment $u(t)$', x=0.01, y=1.02, ha='left')

ax1.plot(t_log, sig_u_pb,
         '--r', drawstyle='steps-post',
         label=u'$u_{PB}(t)$',
         )

ax1.plot(t_log, u_log + sig_u_ext,
         '-k', lw=0.8,  drawstyle='steps-post',
         label=u'$u(t)$',
         )


#------------------
ax20 = plt.subplot(subPlots[2, 0])

ax20.plot(t_log, RMNS_theta_log[:,0],
         '-g', lw=0.8,  drawstyle='steps-post',
         # label=u'$a_1$',
         )

ax20.set_title(u'$a_1$', x=0.01, y=1.02, ha='left')


#------------------
ax21 = plt.subplot(subPlots[2, 1])

ax21.plot(t_log, RMNS_theta_log[:,1],
         '-g', lw=0.8,  drawstyle='steps-post',
         # label=u'$a_2$',
         )

ax21.set_title(u'$a_2$', x=0.01, y=1.02, ha='left')

#------------------
ax22 = plt.subplot(subPlots[2, 2])

ax22.plot(t_log, RMNS_theta_log[:,2],
         '-g', lw=0.8,  drawstyle='steps-post',
         # label=u'$b_1$',
         )

ax22.set_title(u'$b_1$', x=0.01, y=1.02, ha='left')

#------------------
ax23 = plt.subplot(subPlots[2, 3])

ax23.plot(t_log, RMNS_theta_log[:,3],
         '-g', lw=0.8,  drawstyle='steps-post',
         # label=u'$b_2$',
         )

ax23.set_title(u'$b_2$', x=0.01, y=1.02, ha='left')


#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas [s]', x=1.03, ha='left', va='bottom')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()
    ax.legend(handles_ax, labels_ax, loc=2, bbox_to_anchor=(0.02, 0.98))

#------------------

plt.savefig('fig/' + figNamePrefix + '{}'.format(figNumNb) + '_' +figNamePostfix +'.pdf')
