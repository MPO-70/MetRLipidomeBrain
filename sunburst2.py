import plotly.express as px
import pandas as pd
import numpy as np
import dash
from dash import dcc
from dash import html

df = pd.read_csv("Libro2.csv")
df2 = pd.read_csv("Libro3.csv")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
fig = px.sunburst(
        data_frame=df,
        path=["Meaning", 'Class', "ID"],  # Root, branches, leaves
    #color="Class",
    #color_discrete_sequence=px.colors.qualitative.Pastel,
        color="p-value",
        color_continuous_scale=px.colors.diverging.Picnic,
        color_continuous_midpoint=0.025,
    #tile="Distribution of differential features",
                        )

fig2 = px.sunburst(
        data_frame=df2,
        path=["Meaning", 'Class', "ID"],  # Root, branches, leaves
        color="p-value",
        color_continuous_scale=px.colors.diverging.Picnic,#amb aixo posem una escala de -1 a +1 (divergent
        color_continuous_midpoint=0.025,#amb aixo declarem quin es el punt mig de la escala
    #tile="Distribution of differential features",
        )

app.layout = html.Div([
    html.H6("Changes induced by MetR and Aging"),
    html.Div([dcc.Markdown("Cerebellum"),
                    dcc.Graph(id='prob',figure=fig),
              dcc.Markdown(" Frontal Cortex"),
                    dcc.Graph(id='foldch',figure=fig2)],style={'columnCount': 2},
    ),dcc.Markdown("All compounds are putatively annotated compounds based upon physicochemical properties and/or spectral similarity with public/commercial spectral libraries (Ref 28 in text). ((a) Identity (ID) based on exact mass, retention time (RT), and MS/MS spectrum; (b) ID based on exact mass and RT; (c) ID based on MS/MS spectrum; (d) ID based on exact mass. Relative migration time means the differences between class representative internal standard RT and compound RT. FA: fatty acyls, GL: glycerolipids, GP: glycerophospholipids, SP: sphingolipids, SL: sterol lipids.")])

if __name__ == '__main__':
    app.run_server(debug=True)
