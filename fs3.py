# Adding legends, text and annotations.
import random

import bokeh  # type: ignore
from bokeh.plotting import figure, show  # type: ignore
from bokeh.models import BoxAnnotation  # type: ignore


def set_legend_properties(figure: bokeh.plotting.Figure) -> None:
    # Set legend properties.
    figure.legend.location = "top_left"
    figure.legend.title = "Observations"
    figure.legend.label_text_font = "helvetica"
    figure.legend.label_text_font_style = "italic"
    figure.legend.label_text_color = "navy"
    figure.legend.border_line_width = 3
    figure.legend.border_line_color = "navy"
    figure.legend.border_line_alpha = 0.8
    figure.legend.background_fill_color = "navy"
    figure.legend.background_fill_alpha = 0.2


def set_heading_properties(figure: bokeh.plotting.Figure) -> None:
    figure.title_location = "above"
    figure.title.text_font_size = "25px"
    figure.title.align = "right"


def add_box_annotations(figure: bokeh.plotting.Figure) -> None:
    annotations = [
        BoxAnnotation(top=20, fill_alpha=0.1, fill_color="red"),
        BoxAnnotation(top=80, bottom=20, fill_alpha=0.1, fill_color="green"),
        BoxAnnotation(bottom=80, fill_alpha=0.1, fill_color="red"),
    ]
    for annotation in annotations:
        figure.add_layout(annotation)


x = list(range(0, 51))
y = random.sample(range(0, 100), 51)

# Create a new figure.
p = figure(title="fs3 figure")

# Add a line and a circle glyph.
line = p.line(x, y, legend_label="Temp.", line_color="blue", line_width=3)

# Setting properties with sensible defaults.
set_heading_properties(p)
set_legend_properties(p)

# Adding box annotations to the plot.
add_box_annotations(p)

show(p)