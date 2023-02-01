import pandas as pd
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
#import dash_daq as daq
from dash.dependencies import Input, Output, State

#import plotly.graph_objects as go
import plotly.graph_objs as go

from datetime import datetime, date
from data_preprocessing import data_preprocessing

df = data_preprocessing()

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    external_stylesheets=[dbc.themes.SANDSTONE],
)
server = app.server
app.title = "NYPD Shooting Incidents Dashboard"


def logo(app):
    title = html.H5(
        "NEW YORK POLICE DEPARTMENT SHOOTING INCIDENTS",
        style={"marginTop": 5, "marginLeft": "10px"},
    )

    info_about_app = html.H6(
        "List of every shooting incident that occurred in NYC going back to 2006 through\
        the end of the previous calendar year.",
        style={"marginLeft": "10px"},
    )

    logo_image = html.Img(
        src=app.get_asset_url("nypd.png"), style={"float": "right", "height": 100}
    )
    link = html.A(logo_image, href="https://data.cityofnewyork.us/Public-Safety/NYPD-Shooting-Incident-Data-Historic-/833y-fsy8")

    return dbc.Row(
        [dbc.Col([dbc.Row([title]), dbc.Row([info_about_app])]), dbc.Col(link)]
    )




app.layout = dbc.Container(
    fluid=True,
    children=[
        logo(app)
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True)
