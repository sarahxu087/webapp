# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown("## Insights",style={"margin-bottom":"40px"}),
        dcc.Markdown( 
            """ 

            This model was created to take a look into the Apple app overall rating and to test a base predictive model.
            However, we only predict whether the overall rating for the app is more than 4 stars.

            The ROC curve is displayed to the right.
            The ROC curve is created by plotting the true positive rating against the false positive rating at various threshod settings. It displays 
            how well a classifier ranks predicted probabilities.


            The next chart is the Eli5 plot. It shows the feature importance in predicting whether an app is "very good". The rating_count_tot feature is more important than vpp_lic.


            The last graphic is the SHAP Vaules plot. It explains why my prediction was different from the baseline.






          """
          ),

    ],
)

column2 = dbc.Col(
    [
        
        html.Div(html.Img(src='assets/ROC_curve.png', style={"width":"400px","margin":"auto","display":"block"} )),
        html.Br(),
        html.Div(html.Img(src='assets/weight.png',style={"width":"400px","margin":"auto","display":"block"} )),
        html.Br(),
        html.Div(html.Img(src='assets/shap.png', className='img-fluid')),
    ]
)

layout = dbc.Row([column1,column2])