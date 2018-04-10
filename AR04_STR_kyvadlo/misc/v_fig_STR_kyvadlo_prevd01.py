# -*- coding: utf-8 -*-




figNamePostfix = 'prevodovka'
figNamePrefix = 'Obr_'
figPlotParam = fcnDefaultFigSize(14, 0.15, 0.92, 0.08, 0.4, 13)
fig = plt.figure(figNumNb, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1, )

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Prevodová charakteristika', x=0.01, y=1.02, ha='left')

ax0.set_ylabel(u'výstup [deg]', y=1.02, ha='right', va='bottom', rotation='vertical', )
ax0.set_xlabel(u'vstup\n[kg m2 s−2]', x=1.03, ha='left', va='bottom')

ax0.plot(u_pb_vals, y_pb_vals * (180/np.pi),
         '-k',
         )




#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()
    ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------

plt.savefig('fig/' + figNamePrefix + '{}'.format(figNumNb) + '_' +figNamePostfix +'.pdf')
