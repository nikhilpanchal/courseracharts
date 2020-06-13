import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pands as pd

from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure


def draw_axes():
    """
    Draws a graph with a pair of axes and a single point
    :return:
    """
    fig = Figure()
    canvas = FigureCanvasAgg(fig)
    ax = fig.add_subplot(111)
    ax.plot(3, 2, '.')
    canvas.print_png('test.png')


def draw_pyplot():
    # pyplot is part of the scripting layer which offers a convenient plot() function to produce a full plot
    # and takes care of creating a figure and other objects for you
    plt.plot(3, 2, '.')
    plt.show()


def draw_pyplot_axes():
    """
    Drawing a chart using pyplot
    :return:
    """
    plt.plot(3, 2, 'o')

    ax = plt.gca()
    ax.axis([0,6,0,10])

    plt.plot(1, 1, 'o')
    plt.plot(2, 2, 'o')

    plt.show()


def scatter():
    x = np.array([1,2,3,4,5,6,7,8])
    y = x
    colors = ['green'] * (len(x) - 1)
    colors.append('red')

    plt.scatter(x, y, c=colors, s=100)
    plt.xlabel("X label")
    plt.ylabel("Y label")
    plt.title("Chart Title")
    plt.legend(loc=1, frameon=False, title='Legend')
    plt.show()


def line():
    linear_data = np.array([1,2,3,4,5,6,7,8])
    quadratic_data = linear_data ** 2

    # The plot function will use the index of the array as the x values for the points in the line plot
    # plt.plot(linear_data, '-o', quadratic_data, '-o')
    # plt.plot([22,35,29], '--r')

    # plt.fill_between(range(len(linear_data)), linear_data, quadratic_data, facecolor='red', alpha=0.1)

    # It will associate the legend strings to the lines in the order in which they were plotted
    plt.legend(['Baseline', 'Competion', 'Us'])

    plt.figure()
    observation_dates = np.arange('2020-01-01', '2020-01-09', dtype='datetime64[D]')
    observation_dates = list(map(pd.to_datetime, observation_dates))
    plt.plot(observation_dates, linear_data, '-o', observation_dates, quadratic_data, '-o')
    plt.fill_between(observation_dates, linear_data, quadratic_data, facecolor='red', alpha=0.1)

    [item.set_rotation(45) for item in plt.gca().xaxis.get_ticklabels()]

    plt.title('Quadratic ($x^2$) and Linear $x$')
    plt.show()


def bar():
    linear_data = np.array([1,2,3,4,5,6,7,8])
    quadratic_data = linear_data ** 2
    x_vals = range(len(linear_data))
    new_x_vals = []
    [new_x_vals.append(x+0.3) for x in x_vals]

    plt.bar(x_vals, linear_data, width=0.3)
    plt.bar(new_x_vals, quadratic_data, width=0.3, color='red')
    plt.show()


def zippy():
    zip_generator = zip([1,2,3,4,5], [6,7,8,9,0])
    print(list(zip_generator))

    zip_generator = zip([1, 2, 3, 4, 5], [6, 7, 8, 9, 0])
    x, y = zip(*zip_generator)
    print(x)
    print(y)


if __name__ == '__main__':
    bar()