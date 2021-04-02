# Displaying and exporting.

from bokeh.plotting import figure, output_file, save  # typing: ignore

x = [1, 2, 3, 4, 5]
y = [4, 5, 5, 7, 2]

# Set a specific output file.
output_file(filename="fs7_Andrei.html", title="Static HTML file")

# Create a plot.
p = figure(sizing_mode="stretch_width", max_width=500, plot_height=250)

# Add a glyph.
circle = p.circle(x, y, fill_color="red", size=15)

save(p)