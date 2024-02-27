from matplotlib import pyplot as plt

from logger import Logger



class Plotter():
    """
    Just a plotting object.
    """
    def __init__(self) -> None:
        self._fig: plt.figure = None

    
    def plot(self, data: Logger) -> None:
        self._fig = plt.figure(figsize=[7, 5])
        axes = self.fig.subplots(2)
        self._fig.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, hspace=0.3)

        axes[0].plot(data.t_log, data.y_log)
        axes[0].step(data.t_log, data.ym_log)
        axes[0].plot(data.t_log, data.u_log)
        axes[0].set_xlabel(r"$t$")
        axes[0].legend([r"$y$", r"$y_m$", r"$u$"])
        axes[0].grid()
        axes[0].minorticks_on()
        axes[0].spines['right'].set_visible(False)
        axes[0].spines['top'].set_visible(False)

        axes[1].step(data.t_log, data.c_log)
        axes[1].set_xlabel(r"$t$")
        axes[1].legend([r"$a_1$", r"$a_2$", r"$b_1$", r"$b_2$"])
        axes[1].grid()
        axes[1].minorticks_on()
        axes[1].spines['right'].set_visible(False)
        axes[1].spines['top'].set_visible(False)

        plt.show(block=True)


    @property
    def fig(self):
        return self._fig
