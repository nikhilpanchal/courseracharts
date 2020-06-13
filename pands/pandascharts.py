import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def draw_hist():
    """
    Histogram plotted using a DataFrame and a Series, with a customized sizing for the
    bins
    """

    data = pd.DataFrame(
        data=[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 99.5, 99.8, 99.4, 99.75, 98.4, 97.5, 96, 94, 91, 92, 93, 89, 85, 84, 71, 68, 73, 72],
        index=["BU{}".format(i) for i in range(1, 25)],
        columns=["Match Rate"]
    )

    series_data = data["Match Rate"]

    ax = series_data.hist(bins=[65, 70, 75, 80, 85, 90, 95, 99, 100])
    customize_axis_and_show_chart(ax)

    ax_subplot = data.hist(bins=[65, 70, 75, 80, 85, 90, 95, 99, 100])
    customize_axis_and_show_chart(ax_subplot[0, 0])


def customize_axis_and_show_chart(ax):
    ax.set_xticks([65, 70, 75, 80, 85, 90, 95, 99, 100])
    ax.set_xlim(left=65, right=100)
    plt.show()


if __name__ == '__main__':
    draw_hist()