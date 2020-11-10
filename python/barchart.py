import plotly.graph_objects as go
import numpy as np
import pandas as pd
import os
# Change Scatter Plot To Histogram
# Then Save Graph As Image To Images Folder

df = pd.read_csv('StateEducationData.csv', error_bad_lines=False)

State = df['State'].head()

OverallRank = df['overallRank']

CostPerStudent = df['amountPerPupil']

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x = State,
        y = OverallRank,
        name="Top 5 Rank By State"
    ))

fig.add_trace(
    go.Bar(
        x = State,
        y = CostPerStudent,
        name="Cost Per Student"
    ))

fig.update_layout(
    title="Top 5 EDU State Rank and Cost",
    xaxis_title="Overall State Ranking",
    yaxis_title="Cost Per Student",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

fig.show()

if not os.path.exists("graphs"):
    os.mkdir("graphs")
    
    fig.write_image("graphs/barchart.svg")