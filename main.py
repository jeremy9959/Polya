from functools import partial
import numpy as np
from bokeh.plotting import figure, curdoc
from bokeh.models.sources import ColumnDataSource
from bokeh.layouts import column, row, layout
from bokeh.models.widgets import  Button, Spinner
from bokeh.models.widgets.markups import Div
from urn import PolyaUrn
from explanation import explanation_text, explanation_text_2

a, b, n, s = 5, 2, 50, 10

doc = curdoc()
U = PolyaUrn(a, b, n)

WalkPanel_xrange = (0, a + n + 1)
WalkPanel_yrange = (0, n)
WalkPanel = figure(
    name="WalkPanel",
    width=325,
    height=325,
    x_range=WalkPanel_xrange,
    y_range=WalkPanel_yrange,
    toolbar_location=None,
    x_axis_label="Number of White Balls in the Urn",
    y_axis_label="Number of Draws from the Urn",
)
WalkSource = ColumnDataSource({"x": np.zeros(n + 1), "y": np.zeros(n + 1)})
WalkPanel.line(x="x", y="y", source=WalkSource)

DensityPanel_xrange = (0, a + n + 1)
DensityPanel_yrange = (0, 10)
DensityPanel = figure(
    name="DensityPanel",
    width=325,
    height=325,
    x_range=DensityPanel_xrange,
    y_range=DensityPanel_yrange,
    y_axis_location="left",
    y_axis_label = "Density",
    toolbar_location=None,
)
DensitySource = ColumnDataSource(
    {"x": np.array(range(a, a + n + 1)), "normalized": np.zeros(n + 1, dtype="int")}
)
DensityPanel.vbar(x="x", top="normalized", width=0.2, source=DensitySource)
DensityPanel.min_border, WalkPanel.min_border = 5, 5
DensityPanel.xaxis.visible = False
DensityPanel.yaxis.visible = True

start_button = Button(label="Go", button_type="success",width=100)
stop_button = Button(label="Stop", button_type="success",width=100)
stop_button.disabled = True


print("!!!!!!!!!")
a_field = Spinner(high=10.0, low=1.0, step=1.0, value=a, title="White Balls", width=100)
b_field = Spinner(high=10.0, low=1.0, step=1.0, value=b, title="Black Balls", width=100)


def update(U, source):

    n, a, b = U._n, U._a, U._b
    Walk, Density = U.draw()
    normalized = (n + a + b) * Density / Density.sum()
    DensitySource.data = {"x": np.array(range(a, a + n + 1)), "normalized": normalized}
    source.data = Walk


def start_callback():
    global callback

    U.reset()
    callback = doc.add_periodic_callback(partial(update, U, WalkSource), s)
    start_button.disabled = True
    stop_button.disabled = False
    a_field.disabled = True
    b_field.disabled = True
    return


def stop_callback():
    global callback

    stop_button.disabled = True
    start_button.label = "Reset and Go"
    start_button.disabled = False
    a_field.disabled = False
    b_field.disabled = False
    doc.remove_periodic_callback(callback)


def get_a_callback(attrs, old, new):
    global U

    a = int(new)
    U = PolyaUrn(a, U._b, U._n)


def get_b_callback(attrs, old, new):
    global U

    b = int(new)
    U = PolyaUrn(U._a, b, U._n)


a_field.on_change("value",get_a_callback)
b_field.on_change("value",get_b_callback)
stop_button.on_click(stop_callback)
start_button.on_click(start_callback)

#B = row(start_button, stop_button,name='B')
T = row(a_field, b_field, name="T")
S = column([DensityPanel, WalkPanel], name="S")
E = Div(text=explanation_text,name="E")
E2 = layout([Div(text=explanation_text_2),[start_button,stop_button]], name="E2")


doc.add_root(E)
doc.add_root(E2)
doc.add_root(S)
doc.add_root(T)
#doc.add_root(B)
