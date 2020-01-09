# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Which app conside a good app

            With million of apps around nowadays, mobile app analytics is a great way to understand the existing strategy to drive growth and retention of future user.

            Use this app to see how we predict whether the overall rating for the app is more than 4 stars, which we think it a very good app.
            """
        ),
        dcc.Link(dbc.Button('Try it', color='primary'), href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        html.Img(src='assets/pic1.png', className='img-fluid ml-5')
        
    ]
)

layout = dbc.Row([column1, column2])