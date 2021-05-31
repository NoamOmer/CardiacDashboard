import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input

data = pd.read_csv("cardiacData.csv")
data = data.query("type == 'conventional' and region == 'Albany'")
#data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
        "family=Lato:ital,wght@2000display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = "Cardiac Dashboard"

app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.P(children="BSP Medical", className="header-emoji"),
                html.H1(
                    children="Cardiac Dashboard", className="header-title"
                ),
                html.P(
                    children="Your Personalized Cardiac Health Report",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        html.Div(
            children=[
                html.Div(
                    children=dcc.Graph(
                        id="price-chart",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["Date"],
                                    "y": data["AveragePrice"],
                                    "type": "lines",
                                },
                            ],
                           'layout':{
                                'title':'Heart Rate Trend',
                                'xaxis':{
                                    'title':'Test Duration [minutes]'
                                },
                                'yaxis':{
                                    'title':'[BPM]'
                    }
            }
                        },
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="volume-chart",
                        config={"displayModeBar": True},
                        figure={
                            "data": [
                                {
                                    "x": data["Total Bags"],
                                    "y": data["Total Volume"],
                                    "type": "lines",
                                },
                            ],
                            'layout':{
                                'title':'Heartbeat Pattern',
                                'xaxis':{
                                    'title':'Time [seconds]'
                                },
                                'yaxis':{
                                    'title':'[mV]'
                                }
                        }
                        }, 
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)