import plotly.graph_objects as go
import numpy as np
import os

# Change Scatter Plot To Histogram
# Then Save Graph As Image To Images Folder

x0 = np.random.randn(2000)
x1 = np.random.randn(2000) + 1

fig = go.Figure()
fig.add_trace(go.Histogram(x=x0))
fig.add_trace(go.Histogram(x=x1))

# The two histograms are drawn on top of another
fig.update_layout(barmode='stack')
fig.show()


if not os.path.exists("graphs"):
    os.mkdir("graphs")
    fig.write_image("graphs/histogram.png")
