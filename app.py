# 1. Import Dash
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import base64

import pandas as pd
# import statistics 
# from statistics import mode
import plotly.express as px

# 2. Create a Dash app instance
app = dash.Dash(
    external_stylesheets=[dbc.themes.LUX],
    name = 'DMS'
)

app.title = 'DMS Dashbord Analytics'

path_img = 'image3.jpeg'
encode = base64.b64encode(open(path_img, 'rb').read()).decode('ascii')

path_img2 = "data:image/jpeg;base64,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"


navbar = dbc.Navbar(
    dbc.Container(
        [
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=path_img2, height="50px")),
                        dbc.Col(
                            dbc.NavbarBrand ( "DMS Dashbord Analytics" ,className="g-2 fs-2", style={'color':'black', 'size':'100px', }),
                            ),
                    ],
                    align="left",
                    className="g-2 fs-2" 
                ),
        ]
        
    ),
    # color="#6fbf44",
    dark=True,
    style={
        'paddingRight':'370px',
    }
)

## --- Import Dataset DMS
df=pd.read_csv('DMS_dash4.csv',parse_dates=['Date'])


## --- CARD CONTENT
range_date = [
    dbc.CardHeader('Range of Date'),
    dbc.CardBody([
        html.H1(("Oct-Nov '22"))
    ]),
]

total_subject = [
    dbc.CardHeader('Type of Deviation'),
    dbc.CardBody([
        html.H1(df['Deviation'].nunique())
    ]),
]

total_shift = [
    dbc.CardHeader('Total Shift'),
    dbc.CardBody([
        html.H1(df['Shift'].nunique())
    ]),
]

total_deviasi = [
    dbc.CardHeader('Total Deviation'),
    dbc.CardBody([
        html.H1(df['Deviation'].count())
    ]),
]

## --- Visualization
### Line Chart
# Data Aggregation
all_subject = pd.crosstab(index=df['Date'],
            columns='Count Deviation',
            values=df['Deviation'],
            aggfunc='count').reset_index().sort_values('Date', ascending =True)

# Visualization
tren_all = px.line(
    all_subject,
    y = 'Count Deviation',
    x = 'Date',
    color_discrete_sequence=['green'])

### Pie Chart
# Data Aggregation
subject = pd.crosstab(
    index=df['Deviation'],
    columns='Type of Deviation',
    values=df['Deviation'],
    aggfunc='count').reset_index()

# Visualization
persentase_subject = px.pie(
    subject, 
    values='Type of Deviation', 
    names='Deviation', 
    title="Percentage of Type Deviation",
    hole=.3)
    
### Bar Chart
# Data Aggregation
abc = pd.crosstab(
    index=[df['Deviation'],df['Shift']],
    columns='Count Deviation', 
    values=df['Deviation'],
    aggfunc='count').reset_index()

df_bar_row = pd.DataFrame(data=abc, columns=(['Deviation','Shift','Count Deviation'])) 

df_bar_row[['Shift']] = df_bar_row[['Shift']].astype('object')

# Visualization
fig = px.bar(df_bar_row, x='Shift', y='Count Deviation', color='Deviation', text_auto=True, title="Proportion of Type Deviation")
fig.update_layout(
    xaxis={
        'type': 'category',
        'showgrid': False,
    })

### Line Chart
# Data Aggregation
line = pd.crosstab(index=[df['Date'],df['Deviation']],
            columns='Count Deviation',
            values=df['Deviation'],
            aggfunc='count').reset_index().sort_values('Date', ascending =True)


# Visualization
line_dev = px.line(line, 
              x="Date", 
              y="Count Deviation",
              color="Deviation",
              title = 'Trend of Type Deviation',
             )

# --------------------------------------------------------------------------

## --- Layout
app.layout = html.Div([
    # jumbotron,
    navbar,
    
    html.Br(),

    ## --Component Main Page---

    html.Div([
        ## --ROW1--
        dbc.Row([
            ## --COL SATU--
            dbc.Col([
                ## --ROW SATU--
                dbc.Row([
                    dbc.Card(
                        dbc.CardBody([
                            html.H4('Driving Monitoring System (DMS)', style={'textAlign': 'center'}),
                            html.Br(),
                            html.Div(html.Img(src='data:image3/jpeg;base64,{}'.format(encode)), style={'imageAlign': 'center'}),
                            html.Br(),
                            html.P(
                                '''A driving assistance system platform with dual cameras in front and in the cabin that can monitor the status of the driver while operating the vehicle, issuing a warning if an abnormality or deviation is detected. If during the observation process the driver often commits violations, the driver will be intervened or given direct warning through the speakers in the cabin.''',
                                className="card-text"),
                        ]), color='lightgrey'
                    )
                ]),
                html.Br(),
            ], width=6),

            ## --COL DUA--
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H4('Trend of Deviation', style={'textAlign': 'center'}),
                        dcc.Graph(figure=tren_all)
                    ]), color='lightgrey'
                )
            ], width=6)
        ]),

        ## --ROW2--
        dbc.Row([
            dbc.Col([
                dbc.Card(range_date, color='lightgreen')
            ]),
            dbc.Col([
                dbc.Card(total_subject, color='lightgreen')
            ]),
            dbc.Col([
                dbc.Card(total_deviasi, color='lightgreen')
            ]),
            dbc.Col([
                dbc.Card(total_shift, color='lightgreen')
            ]),
        ]), 

html.Br(),
        ## --ROW3--
        dbc.Row([
            ## --COL SATU--
            dbc.Col
            ([
                dbc.Card(
                    dbc.CardBody([
                        html.H4('Deviation Category Analysis', style={'textAlign': 'center'}),
                        dbc.CardHeader('Select Tab'),
                        html.Br(),
                        dbc.Tabs
                        ([
                            ## --- TAB 1: Percentage
                            dbc.Tab
                            (
                                dcc.Graph
                                (
                                    id='persentase_subject_dev',
                                    figure=persentase_subject,
                                ),
                                label='Percentage'),

                            ## --- TAB 2: Trend
                            dbc.Tab
                            (
                                dcc.Graph
                                (
                                    id='trend_deviation',
                                    figure=line_dev,
                                ),
                                label='Trend of Deviation'),
                        ]),
                    ]), color='lightgrey'
                )
                
            ], width=6),

            ## --COL DUA--
            dbc.Col([
                dbc.Card(
                    dbc.CardBody([
                        html.H4('Deviation Analysis for Each Operator', style={'textAlign': 'center'}),
                        dbc.CardHeader('Select Operator'),
                        dbc.CardBody(
                            dcc.Dropdown(
                                id='choose_operator',
                                options=df['Operator'].unique(),
                                value='Candra Halim',
                            ),
                        ),
                    dcc.Graph(
                    id='bar_dev_operator',
                    figure=fig,
                    ),
                    ]), color='lightgrey'
                )
            ], 
            width=6),
        ]),
        ## --ROW4--
        dbc.Row([
            html.H5('Created By : tyasrindhu')
        ])
    ]),
])    

### Callback Plot Distribution
@app.callback(
    Output(component_id='bar_dev_operator', component_property='figure'),
    Input(component_id='choose_operator', component_property='value')
)
def update_output2(operator_name):
    df_Operator=df[df['Operator']== operator_name]
    
    # Data Aggregation
    abc = pd.crosstab(
    index=[df_Operator['Deviation'],df_Operator['Shift']],
    columns='Count Deviation', 
    values=df_Operator['Deviation'],
    aggfunc='count').reset_index()

    df_bar_row = pd.DataFrame(data=abc, columns=(['Deviation','Shift','Count Deviation'])) 

    df_bar_row[['Shift']] = df_bar_row[['Shift']].astype('object')

    # Visualization
    fig = px.bar(df_bar_row, x='Shift', y='Count Deviation', color='Deviation', text_auto=True, title=f'Proportion of Type Deviation {str(operator_name)}')
    fig.update_layout(
    xaxis={
        'type': 'category',
        'showgrid': False,
    })

    return fig

# 3. Start the Dash server
if __name__ == "__main__":
    app.run_server()