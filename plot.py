import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


def pie_chart(df, xlabel, ylabel, color=False, title=None, figsize=None):
    """
    color to assign:
        colors = {
        'PA': (1.0, 0.0, 0.0),  # red
        'FL': (1.0, 0.5, 0.0),  # orange
        'LA': (1.0, 1.0, 0.0),  # yellow
        'TN': (0.0, 1.0, 0.0),  # green
        'MO': (0.0, 0.0, 1.0),  # blue
        'IN': (0.5, 0.0, 0.5),  # purple
        'AZ': (1.0, 0.75, 0.8),  # pink
        'NV': (0.647, 0.165, 0.165),  # brown
        'NJ': (0.827, 0.827, 0.827),  # light gray
        'ID': (0.0, 0.0, 0.0),  # black
        'DE': (1.0, 1.0, 1.0),  # white
        'AB': (0.5, 0.5, 0.0),  # olive
        'IL': (0.0, 0.5, 0.5),  # teal
        'WA': (0.0, 1.0, 1.0),  # cyan
        'TX': (1.0, 0.843, 0.0),  # goldenrod
        'CO': (1.0, 0.498, 0.314),  # coral
        'CA': (0.294, 0.0, 0.51),  # indigo
        'UT': (0.0, 0.0, 0.545),  # dark blue
        'SD': (0.0, 0.392, 0.0),  # dark green
        'MT': (0.663, 0.663, 0.663)  # gray
        }
    """

    # set xlabel as the index of dataframe
    df.set_index(xlabel, inplace=True)
    # sort dataframe by ylabel
    df.sort_values(by=ylabel, ascending=False, inplace=True)
    print(df)

    if color:
        # assign colors to each index if needed
        colors = [(1.0, 0.0, 0.0),  # red
                  (1.0, 0.5, 0.0),  # orange
                  (1.0, 1.0, 0.0),  # yellow
                  (0.0, 1.0, 0.0),  # green
                  (0.0, 0.0, 1.0),  # blue
                  (0.5, 0.0, 0.5),  # purple
                  (1.0, 0.75, 0.8),  # pink
                  (0.647, 0.165, 0.165),  # brown
                  (0.827, 0.827, 0.827),  # light gray
                  (0.0, 0.0, 0.0),  # black
                  (1.0, 1.0, 1.0),  # white
                  (0.5, 0.5, 0.0),  # olive
                  (0.0, 0.5, 0.5),  # teal
                  (0.0, 1.0, 1.0),  # cyan
                  (1.0, 0.843, 0.0),  # goldenrod
                  (1.0, 0.498, 0.314),  # coral
                  (0.294, 0.0, 0.51),  # indigo
                  (0.0, 0.0, 0.545),  # dark blue
                  (0.0, 0.392, 0.0),  # dark green
                  (0.663, 0.663, 0.663)  # gray
                ]
        ordered_colors = [colors[i] for i in range(len(df))] # assume that len(df) <= 15
        df.plot.pie(y=ylabel, colors=ordered_colors, legend=False, figsize=(9, 9), title=title)
        plt.show()
    else:
        df.plot.pie(y=ylabel, legend=False, figsize=(9, 9), title=title)
        plt.show()


def CDF(data, xlabel):
    res_freq = stats.relfreq(data, numbins=100)
    cdf_value = np.cumsum(res_freq.frequency)
    cdf_value = cdf_value * 100
    x = res_freq.lowerlimit + np.linspace(0, res_freq.binsize * res_freq.frequency.size, res_freq.frequency.size)
    plt.xlabel(xlabel)
    plt.ylabel("CDF(%)")
    plt.ylim(0, 100)
    plt.plot(x, cdf_value)
    plt.show()
