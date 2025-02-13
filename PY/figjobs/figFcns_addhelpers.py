# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


###############################################################################

from matplotlib.ticker import (AutoMinorLocator,
                               MultipleLocator,
                               FormatStrFormatter,
                               )

import matplotlib.dates as mdates



###############################################################################


from figFcns_TeX import *

###############################################################################


###############################################################################






def fcn_panelformat_variant01(fig):

    for ax in fig.get_axes():

        fcnDefaultAxisStyle(ax)

        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.xaxis.set_minor_locator(AutoMinorLocator())



        ax.ticklabel_format(axis='y', useOffset=False)

        ax.set_xlabel('čas', ha='left', va='top')
        ax.xaxis.set_label_coords(1.05, -0.08)


        ax.yaxis.set_label_coords(-0.02, 1.08)


        #-----------------------------


        #-----------------------------

        handles_ax, labels_ax = ax.get_legend_handles_labels()


        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.0, markerfirst=True, loc=2, bbox_to_anchor=(1.02, 1.00))








###############################################################################











def fcn_panelformat_variant02(fig):

    for ax in fig.get_axes():

        fcnDefaultAxisStyle(ax)

        ax.yaxis.set_minor_locator(AutoMinorLocator())
        ax.xaxis.set_minor_locator(AutoMinorLocator())



        ax.ticklabel_format(axis='y', useOffset=False)

        ax.set_xlabel('čas', ha='left', va='top')
        ax.xaxis.set_label_coords(1.05, -0.08)


        ax.yaxis.set_label_coords(-0.02, 1.08)


        #-----------------------------


        #-----------------------------

        handles_ax, labels_ax = ax.get_legend_handles_labels()


        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=0.8, labelspacing=0.3, markerfirst=True, loc=2, bbox_to_anchor=(1.01, 1.00))








###############################################################################




