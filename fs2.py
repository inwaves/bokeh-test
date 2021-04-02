# Using different glyphs.

from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y1 = [4, 5, 4, 5, 4]
y2 = [3, 4, 3, 4, 3]
y3 = [2, 3, 2, 3, 2]

p = figure(title="Testing circles", x_axis_label="x", y_axis_label="y")

p.vbar(x=x, top=y1, legend_label="Rate", width=0.5, bottom=0, color="green")
circle = p.circle(x, y1, legend_label="Objects", line_color="yellow", size=12)

# If I want to modify this glyph later...
circle.glyph.fill_color = "blue"

show(p)