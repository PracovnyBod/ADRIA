# -*- coding: utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

###############################################################################
mpl.rcParams['figure.dpi'] = 120


# mpl.rcParams['mathtext.fontset'] = 'stix'


# mpl.rcParams['font.family'] = 'serif'

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['font.family'] ='Latin Modern Roman'

# mpl.rcParams['text.usetex'] = False
mpl.rcParams['text.usetex'] = True
# mpl.rcParams['text.latex.unicode'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage[T1]{fontenc} \usepackage{lmodern}'


mpl.rcParams['font.size'] = 10

mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['xtick.labelsize'] = mpl.rcParams['font.size']

mpl.rcParams['ytick.direction'] = 'out'
mpl.rcParams['ytick.labelsize'] = mpl.rcParams['font.size']

mpl.rcParams['axes.xmargin'] = 0.02
mpl.rcParams['axes.ymargin'] = 0.03

mpl.rcParams['axes.titlesize'] = mpl.rcParams['font.size']
mpl.rcParams['axes.labelsize'] = mpl.rcParams['font.size']
mpl.rcParams['legend.fontsize'] = mpl.rcParams['font.size']#'small'#
mpl.rcParams['legend.frameon'] = False
mpl.rcParams['legend.borderpad'] = 0.1
mpl.rcParams['legend.borderaxespad'] = 0.0
mpl.rcParams['legend.labelspacing'] = 0.2
mpl.rcParams['legend.numpoints'] = 1

###############################################################################

def fcnDefaultAxisStyle(ax):
    # ax.grid(color='#cccccc', alpha=1.0, linewidth=0.33, linestyle=':', dashes=[15,4])
    ax.grid(which='major', color='#cccccc', alpha=1.0, linewidth=0.33, linestyle='-', dashes=[7,0])
    ax.grid(which='minor', color='#dddddd', alpha=1.0, linewidth=0.33, linestyle=':', dashes=[4,3])
    ax.set_axisbelow(True)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()


def fcnDefaultTwinAxisStyle(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)




###############################################################################


def fcnDefaultFigSize(figSizeTotalHeight,
                      fig_lrPadding,
                      fig_top,
                      fig_bottom,
                      fig_hspace,
                      figSizePlotWidth
                      ):

    figSizeLeftAdj = fig_lrPadding
    figSizeRightAdj = 1.0 - fig_lrPadding

    figSizeTotalWidth = figSizePlotWidth / (figSizeRightAdj - figSizeLeftAdj)


    return [figSizeTotalWidth/2.54,
            figSizeTotalHeight/2.54,
            fig_lrPadding,
            fig_hspace,
            fig_top,
            fig_bottom,
            ]



def fcnDefaultLayoutAdj(fig, fig_lrPadding, fig_hspace, fig_top, fig_bottom):
    fig.tight_layout()

    fig.subplots_adjust(left=fig_lrPadding)
    fig.subplots_adjust(right=1-fig_lrPadding)

    fig.subplots_adjust(hspace=fig_hspace)
    fig.subplots_adjust(top=fig_top)
    fig.subplots_adjust(bottom=fig_bottom)



###############################################################################
