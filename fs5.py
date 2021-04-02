# Vectorising glyph properties.

import random

import bokeh  # typing: ignore
from bokeh.plotting import figure, show  # typing: ignore

x = list(range(0, 26))
y = random.sample(range(0, 100), 26)

# Could I use f-strings instead of % here? How?
colours = ["#%02x%02x%02x" % (255, int(round(value * 255 / 100)), 255) for value in y]
print(len(colours))


p = figure(
    title="Vectorised colours example",
    sizing_mode="stretch_width",
    max_width=500,
    plot_height=250,
)

# Add two glyphs.
line = p.line(x, y, line_color="blue", line_width=1)
circle = p.circle(x, y, fill_color=colours, line_color="blue", size=15)

show(p)