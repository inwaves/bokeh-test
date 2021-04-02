# Providing and filtering data.

from bokeh.plotting import figure, show # typing: ignore
from bokeh.models import CDSView, ColumnDataSource, IndexFilter # typing: ignore

data = {
    "x_values": [1,2,3,4,5],
    "y_values": [6,7,2,3,6]
}

source = ColumnDataSource(data)

# Create a view using an Indexfilter on our source
view = CDSView(source=source, filters=[IndexFilter([0, 2, 4])])

p = figure()
p.circle(x="x_values", y="y_values", source=source)
p.circle(x="x_values", y="y_values", color="red", source=source, view=view)

show(p)