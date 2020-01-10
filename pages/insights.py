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

            This model was created to take a look into the apple app overall rating and to test a base predictive model.
            However, we only predict whether the overall rating for the app is more than 4 stars.

            ROC curve is displayed to the right.
            ROC curve is created by plotting the true positive rate against the false positive rate at various threshod settings.It means 
            how well a classifier ranks predicted probabilities.


            Next one is Eli5 plot, It shows feature importance in predicting whether it is very good app. Feature rating_count_tot is more important than vpp_lic.


            The last one is SHAP Vaules plot. it is to explain why my prediction was different from the baseline.






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