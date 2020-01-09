# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
# Imports from this application
from app import app
#load pipeline
pipeline = load('assets/pipeline.joblib')
print('Pipeline loaded')
# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Predictions

            If this app will be a very good app, means it will be more than 4 stars.

            Content Rating:
            Rated 4+: Contains no objectionable material.
            Rated 9+: May contain content unsuitable for children under the age of 9.
            ated 12+: May contain content unsuitable for children under the age of 12.
            Rated17+: May contain content unsuitable for children under the age of 17.

            """
            
        ),
        
    ],
        

    md=4,
)

column2 = dbc.Col(
    
    [
        dcc.Markdown('#### Content Rating'),
       
        dcc.Dropdown(
            id="cont_rating",
            style={"width":'280px'},
            options=[
                {'label': '9+', 'value': '9+'},
                {'label': '4+', 'value': '4+'},
                {'label': '12+', 'value': '12+'},
                {'label': '17+', 'value': '17+'},
            ],
            value='4+'
        ),
        
        dcc.Markdown('#### Primary Genre',className='mt-3'),  
        dcc.Dropdown(
            id="prime_genre",
            style={"width":'280px'},
            options=[
                {'label': 'Games', 'value': 'Games'},
                {'label': 'Finance', 'value': 'Finance'},
                {'label': 'Entertainment', 'value': 'Entertainment'},
                {'label': 'Music', 'value': 'Music'},
                {'label': 'Education', 'value': 'Education'},
                {'label': 'News', 'value': 'News'},
                {'label': 'Health & Fitness', 'value': 'Health & Fitness'},
                {'label': 'Utilities', 'value': 'Utilities'},
                {'label': 'Photo & Video', 'value': 'Photo & Video'},
                {'label': 'Sports', 'value': 'Sports'},
                {'label': 'Weather', 'value': 'Weather'},
                {'label': 'Food & Drink', 'value': 'Food & Drink'},
                {'label': 'Productivity', 'value': 'Productivity'},
                {'label': 'Book', 'value': 'Book'},
                {'label': 'Shopping', 'value': 'Shopping'},
                {'label': 'Social Networking', 'value': 'Social Networking'},
                {'label': 'Navigation', 'value': 'Navigation'},
                {'label': 'Travel', 'value': 'Travel'},
                {'label': 'Reference', 'value': 'Reference'},
                {'label': 'Lifestyle', 'value': 'Lifestyle'},
                {'label': 'Business', 'value': 'Business'},
                {'label': 'Medical', 'value': 'Medical'},
                {'label': 'Catalogs', 'value': 'Catalogs'},
               
            ],
            value='Games'
        ),
        html.H4('Expected App Rating',style={"margin-top":"20px"}),
        html.Div(id='prediction-content', style={"font-size":"20px","margin-top":"15px"}),
    ],
    style={"margin-left":"370px"}
)

import pandas as pd

@app.callback(
    Output('prediction-content', 'children'),
    [Input('cont_rating', 'value'), Input('prime_genre', 'value')],
)
def predict(cont_rating, prime_genre):
    df = pd.DataFrame(
        columns=['cont_rating', 'prime_genre'], 
        data=[[cont_rating, prime_genre]]
    )
    y_pred = pipeline.predict(df)[0]
    if y_pred == 0:
        return "It has less than a 4-star rating."
    else:
        return "It has more than a 4-star rating"

layout = dbc.Row([column1, column2])