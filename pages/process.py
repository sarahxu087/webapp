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
        dcc.Markdown(
            """
        
            ## Modeling Process
            --------------------------------------------------------------

              * ### Dataset:
              This data set contains more than 7000 Apple iOS mobile application details
              (e.g. size, price, genre, rating_count, description, etc.) 
              The data was extracted from the iTunes Search API at the Apple Inc website. From the profile report we can see the
              brief information about the dataframe.  (see photo on the right)
              &emsp;


               * ### Goal/Baseline:
              
              The goal is to predict whether the overall rating for the app is more than 4 stars, 
              which we consider to be a very good app.
              The majority class occurs with 57% frequency, so this is not too imbalanced.I could just use the accuracy score as my evaluation metric.
              So my model needs to `beat 57%`.(see photo on the right)

              &emsp;
              
              * ### Fit a linear model:
              Because it is a binary classification problem, I used `logistic Regression` for my model.
              After tuning and prepping the data with `LogisticRegressionCV`, `SimpleImputer`,  `OneHotEncoder` and `StandardScaler`,the model was tested
              on the validation data. My accuracy score improves a little; now the score is 63%.

              &emsp;

              * ### Fit a tree model:
              I used `RandomForest`.
              After tuning and prepping the data with `RandomForestClassifier`, `SimpleImputer`,  and `OrdinalEncoder`, the model was tested
              on the validation data. My accuracy score improves a little; now the score is 70%.

              I used this model to fit my test dataset. The score is 72%.
              
              
              
              

               &emsp;
               
               
              





            """
        ),

    ],
)
column2 = dbc.Col(
    [
        html.Div(html.Img(src='assets/df_profile_report.png', style={"width":"400px","height":"300px","margin-top":"60px","margin-left":"110px"} )),
        html.Br(),
        html.Div(html.Img(src='assets/baseline.png',style={"width":"400px","margin-left":"110px","margin-top":"20px"} )),
       
    ]
)

layout = dbc.Row([column1,column2])