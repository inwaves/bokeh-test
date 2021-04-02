# Using widgets.

from bokeh.plotting import figure, show, output_file
from bokeh.layouts import layout
from bokeh.models import Div, RangeSlider, Spinner  # typing: ignore

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

output_file("fs9.html")

# Set up figure and renderer/glyph.
p = figure(x_range=(1, 9), plot_width=500, plot_height=250)
points = p.circle(x=x, y=y, size=30, fill_color="#21a7df")

# Widget to display some text.
div = Div(
    text="""
    <p> Select the circle's size using this control element:</p>
    """,
    width=200,
    height=30,
)

# Dropdown list-like widget to adjust glyph size.
spinner = Spinner(
    title="Circle size",
    low=0,
    high=60,
    step=5,
    value=points.glyph.size,  # Initial size.
    width=200,
)

# Link the spinner to the size property of `points`.
spinner.js_link("value", points.glyph, "size")

range_slider = RangeSlider(
    title="Adjust x-axis range",
    start=0,
    end=10,
    step=1,
    value=(p.x_range.start, p.x_range.end),
)

range_slider.js_link("value", p.x_range, "start", attr_selector=0)
range_slider.js_link("value", p.x_range, "end", attr_selector=1)

layout = layout(
    [
        [div, spinner],
        [range_slider],
        [p],
    ]
)

show(layout)