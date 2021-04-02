# Customising the plot itself.

import bokeh  # type: ignore
from bokeh.io import curdoc  # type: ignore
from bokeh.plotting import figure, show  # type: ignore


def set_axes_properties(figure: bokeh.plotting.Figure) -> None:
    figure.xaxis.axis_label = "Temp"
    figure.xaxis.axis_line_width = 2
    figure.xaxis.axis_line_color = "red"


def set_grid_properties(figure: bokeh.plotting.Figure) -> None:
    figure.ygrid.grid_line_alpha = 0.8
    figure.ygrid.grid_line_dash = [6, 4]


def set_bands_properties(figure: bokeh.plotting.Figure) -> None:
    figure.ygrid.band_fill_color = "olive"
    figure.ygrid.band_fill_alpha = 0.1
    p.xgrid.bounds = (2, 4)  # Define vertical bounds.


x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 6, 2]

# Bokeh has five built-in themes.
# Note that applying a theme affects other changes
# you may have made, for example to the axes.
# curdoc().theme = "dark_minimal"

# Customisation on the plot goes here.
p = figure(sizing_mode="stretch_width", max_width=500, plot_height=250)

p.line(x, y)

# Customisation of the axes.
set_axes_properties(p)

# Customisation of the grid.
set_grid_properties(p)

# Add bands.
set_bands_properties(p)

# Autohide the toolbar, reappears on hover.
# You can also decide what tools are on it.
p.toolbar.autohide = True
p.toolbar.logo = None

show(p)