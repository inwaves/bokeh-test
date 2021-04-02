# A simple line example.

from bokeh.plotting import figure, show

x = [1, 2, 3, 4, 5]
y1 = [4, 5, 4, 5, 4]
y2 = [3, 4, 3, 4, 3]
y3 = [2, 3, 2, 3, 2]

# Create a plot
p = figure(title="Line example", x_axis_label="X axis", y_axis_label="Y axis")

# Add a "glyph" to it
p.line(x=x, y=y1, line_width=3, line_color="blue", legend_label="Temperature")
p.line(x=x, y=y2, line_width=3, line_color="green", legend_label="Temperature")
p.line(x=x, y=y3, line_width=3, line_color="red", legend_label="Temperature")

# Show the results
show(p)