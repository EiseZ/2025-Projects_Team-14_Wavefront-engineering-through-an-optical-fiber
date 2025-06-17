# verschillende soorten heatmaps maken om de data in te plotten

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

algorithm = 3

# def heatmap(data, row_labels, col_labels, ax=None,
#             cbar_kw=None, cbarlabel="", **kwargs):
#     """
#     Create a heatmap from a numpy array and two lists of labels.

#     Parameters
#     ----------
#     data
#         A 2D numpy array of shape (M, N).
#     row_labels
#         A list or array of length M with the labels for the rows.
#     col_labels
#         A list or array of length N with the labels for the columns.
#     ax
#         A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
#         not provided, use current Axes or create a new one.  Optional.
#     cbar_kw
#         A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
#     cbarlabel
#         The label for the colorbar.  Optional.
#     **kwargs
#         All other arguments are forwarded to `imshow`.
#     """

#     if ax is None:
#         ax = plt.gca()

#     if cbar_kw is None:
#         cbar_kw = {}

#     # Plot the heatmap
#     im = ax.imshow(data, **kwargs)

#     # Create colorbar
#     cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
#     cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

#     # Show all ticks and label them with the respective list entries.
#     ax.set_xticks(range(data.shape[1]), labels=col_labels,
#                   rotation=-30, ha="right", rotation_mode="anchor")
#     ax.set_yticks(range(data.shape[0]), labels=row_labels)

#     # Let the horizontal axes labeling appear on top.
#     ax.tick_params(top=True, bottom=False,
#                    labeltop=True, labelbottom=False)

#     # Turn spines off and create white grid.
#     ax.spines[:].set_visible(False)

#     ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
#     ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
#     ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
#     ax.tick_params(which="minor", bottom=False, left=False)

#     return im, cbar
# def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
#                      textcolors=("black", "white"),
#                      threshold=None, **textkw):
#     """
#     A function to annotate a heatmap.

#     Parameters
#     ----------
#     im
#         The AxesImage to be labeled.
#     data
#         Data used to annotate.  If None, the image's data is used.  Optional.
#     valfmt
#         The format of the annotations inside the heatmap.  This should either
#         use the string format method, e.g. "$ {x:.2f}", or be a
#         `matplotlib.ticker.Formatter`.  Optional.
#     textcolors
#         A pair of colors.  The first is used for values below a threshold,
#         the second for those above.  Optional.
#     threshold
#         Value in data units according to which the colors from textcolors are
#         applied.  If None (the default) uses the middle of the colormap as
#         separation.  Optional.
#     **kwargs
#         All other arguments are forwarded to each call to `text` used to create
#         the text labels.
#     """

#     if not isinstance(data, (list, np.ndarray)):
#         data = im.get_array()

#     # Normalize the threshold to the images color range.
#     if threshold is not None:
#         threshold = im.norm(threshold)
#     else:
#         threshold = im.norm(data.max())/2.

#     # Set default alignment to center, but allow it to be
#     # overwritten by textkw.
#     kw = dict(horizontalalignment="center",
#               verticalalignment="center")
#     kw.update(textkw)

#     # Get the formatter in case a string is supplied
#     if isinstance(valfmt, str):
#         valfmt = mpl.ticker.StrMethodFormatter(valfmt)

#     # Loop over the data and create a `Text` for each "pixel".
#     # Change the text's color depending on the data.
#     texts = []
#     for i in range(data.shape[0]):
#         for j in range(data.shape[1]):
#             kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
#             text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
#             texts.append(text)

#     return texts
# if algorithm == 0:
#     vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
#                 "potato", "wheat", "barley"]
#     farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
#             "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

#     harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
#                         [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
#                         [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
#                         [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
#                         [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
#                         [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
#                         [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

#     fig, ax = plt.subplots()

#     im, cbar = heatmap(harvest, vegetables, farmers, ax=ax,
#                     cmap="YlGn", cbarlabel="harvest [t/year]")
#     texts = annotate_heatmap(im, valfmt="{x:.1f} t")

#     fig.tight_layout()
#     plt.show()

# def heatmap_lmao(data, row_labels, col_labels, ax=None,
#             cbar_kw=None, cbarlabel="", **kwargs):
#     if ax is None:
#         ax = plt.gca()

#     if cbar_kw is None:
#         cbar_kw = {}

#     # Plot the heatmap
#     im = ax.imshow(data, **kwargs)

#     # Create colorbar
#     cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
#     cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

#     ax.spines[:].set_visible(False)

#     ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
#     ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
#     ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
#     ax.tick_params(which="minor", bottom=False, left=False)

#     return im #, cbar

# def annotate_heatmap_lmao(im, data=None, valfmt="{x:.2f}",
#                      textcolors=("black", "white"),
#                      threshold=None, **textkw):

#     if not isinstance(data, (list, np.ndarray)):
#         data = im.get_array()

#     # Normalize the threshold to the images color range.
#     if threshold is not None:
#         threshold = im.norm(threshold)
#     else:
#         threshold = im.norm(data.max())/2.

# if algorithm == 1:
#     vegetables = ["cucumber", "tomato", "lettuce", "asparagus"]
#     farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
#             "Agrifun", "Organiculture", "BioGoods Ltd."]

#     harvest = np.array([[100, 150, 200, 350, 370, 400],[210, 300, 370, 450, 600, 1000],[500, 700, 1000, 1500, 2000, 2700],[650, 1050, 1390, 1900, 2500, 3600]])

#     fig, ax = plt.subplots()

#     im = heatmap_lmao(harvest, vegetables, farmers, ax=ax,
#                     cmap="gist_rainbow", cbarlabel="time in seconds")
#     #texts = annotate_heatmap(im, valfmt="{x:.1f} t")

#     fig.tight_layout()
#     plt.show()

# if algorithm == 2:
#     import numpy as np
#     import matplotlib.pyplot as plt
#     from matplotlib.colors import Normalize, FuncNorm
#     from matplotlib.cm import ScalarMappable

#     # Nonlinear function: emphasize low values
#     def forward(x):
#         return np.sqrt(x)  # sqrt stretches low values

#     def inverse(x):
#         return x**2  # inverse of sqrt

#     # Create custom normalization
#     norm = FuncNorm((forward, inverse), vmin=0, vmax=3600)

#     # Create a colormap
#     cmap = "gist_rainbow"  # or any other

#     # Plot example
#     gradient = np.linspace(0, 1, 256).reshape(-1, 1)

#     vegetables = ["cucumber", "tomato", "lettuce", "asparagus"]
#     farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
#             "Agrifun", "Organiculture", "BioGoods Ltd."]

#     harvest = np.array([[100, 150, 200, 350, 370, 400],[210, 300, 370, 450, 600, 1000],[500, 700, 1000, 1500, 2000, 2700],[650, 1050, 1390, 1900, 2500, 3600]])

#     fig, ax = plt.subplots()

#     im = heatmap_lmao(harvest, vegetables, farmers, ax=ax,
#                     cmap= gradient, cbarlabel="time in seconds")
#     #texts = annotate_heatmap(im, valfmt="{x:.1f} t")

#     fig.tight_layout()
#     plt.show()


if algorithm == 3:
    

    def heatmap_lmao(data, row_labels, col_labels, ax=None,
                cbar_kw=None, cbarlabel="", time=False, **kwargs):
        if ax is None:
            ax = plt.gca()

        if cbar_kw is None:
            cbar_kw = {}

        # Plot the heatmap
        im = ax.imshow(data, **kwargs)
        for (i, j), z in np.ndenumerate(data):
            if not time:
                ax.text(j, i, '{:0.3f}'.format(z), ha='center', va='center', size="small")
            else:
                ax.text(j, i, '{:0.0f}'.format(z), ha='center', va='center', size="small")

        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        #cbar.ax.set_yticks(np.geomspace(1, 3000, num=10))
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        ax.set_xticks(range(data.shape[1]), labels=col_labels,
        rotation=0, ha="center", rotation_mode="anchor")
        ax.set_xlabel("Number of segments")
        ax.set_yticks(range(data.shape[0]), labels=row_labels)
        ax.set_ylabel("Number of phases")

        ax.spines[:].set_visible(False)

        # White grid
        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True) # 
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True) # #[50, 100, 150, 200, 300, 400, 500, 700, 1000, 2000, 3000]
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)

        return im, cbar


    # Main code
    from matplotlib.colors import PowerNorm, Normalize  # <-- important

    phases = ["2", "3", "4", "5"]
    segments = ["100", "300", "500",
            "700", "900"]

    time = np.array([
        [103.10, 288.86, 482.78,  673.28,  895.31],
        [165.62, 470.16, 791.73,  1098.36, 1000],
        [227.13, 653.82, 1084.39, 1528.44, 1000],
        [292.03, 840.75, 1404.38, 1952.23, 1000]
    ])

    power_ratio = np.array([
        [0.0164, 0.030,  0.0648, 0.0625, 0.1129],
        [0.0310, 0.0998, 0.171,  0.193,  0.1],
        [0.0399, 0.144,  0.151,  0.219,  0.1],
        [0.0470, 0.144,  0.172,  0.193,  0.1]
    ])

    ratio = (power_ratio / time) * 1000

    fig, ax = plt.subplots()
    # Use PowerNorm to emphasize lower values (gamma < 1)
    norm_time = PowerNorm(gamma=0.35, vmin=0, vmax=(time.max()+ 100))
    im , cbar= heatmap_lmao(
        time, phases, segments, ax=ax, time=True,
        cmap="rainbow", cbarlabel="Time in seconds", norm=norm_time
    )
    fig.tight_layout()
    plt.show()


    fig, ax = plt.subplots()
    norm_power_ratio = PowerNorm(gamma=0.35, vmin=0, vmax=(power_ratio.max() + 0.1))
    im , cbar= heatmap_lmao(
        power_ratio, phases, segments, ax=ax,
        cmap="rainbow", cbarlabel="Power ratio", norm=norm_power_ratio
    )
    fig.tight_layout()
    plt.show()


    fig, ax = plt.subplots()
    norm_ratio = Normalize(vmin=(ratio.min() * 0.9), vmax=(ratio.max() * 1.1))
    im , cbar= heatmap_lmao(
        ratio, phases, segments, ax=ax,
        cmap="rainbow", cbarlabel="Time - power ratio ratio * 100", norm=norm_ratio
    )
    fig.tight_layout()
    plt.show()
