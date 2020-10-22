import plotly.graph_objects as go
import numpy as np
import os

# Create Scatter Plot
# Then Save Graph As Image To Images Folder

np.random.seed(1)

N = 100
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
sz = np.random.rand(N) * 30

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers",
    marker=go.scatter.Marker(
        size=sz,
        color=colors,
        opacity=0.6,
        colorscale="Viridis"
    )
))

if not os.path.exists("graphs"):
    os.mkdir("graphs")
    fig.write_image("graphs/histogram.png")
