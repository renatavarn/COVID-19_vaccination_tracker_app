import dash
from dash import dcc, html, callback, Output, Input
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


dash.register_page(__name__, path='/')


df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv')

layout = html.Div([
    html.Label('COUNTRY: ', style={'textAlign': 'left',
                                   'fontSize': 20,
                                   'color': 'white'}),
    dcc.Dropdown(options = [x for x in df.location.unique()], id='location-choice',
                 value = 'Sweden', style={'backgroundColor': '#111111', 'borderColor': 'white','width':'50%'}),
    dcc.Graph(id='Incidence', figure={})
])



@callback(
    Output('Incidence', 'figure'),
    Input('location-choice', 'value')
)
def update_graph1(selected_country):
    countries = df.loc[df.location == selected_country].copy()
    countries['date'] = pd.to_datetime(countries['date'])
    resampled = countries.set_index('date').resample('7D').mean()

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # from smoothed data for new cases per million
    fig.add_trace(go.Scatter(x=resampled.index, y=resampled.new_cases_per_million, name='Cases',
                             line=dict(width=2.5)), secondary_y=False)
    # from original data
    fig.add_trace(go.Scatter(x=countries.date, y=countries.new_vaccinations_smoothed, name='Vaccinations',
                             line=dict(color='#9b59b6', width=2.5)), secondary_y=True)

    fig.update_layout(title=f"New COVID-19 cases and vaccinations",
                      template='plotly_dark', width=1300, height=550, title_font=dict(size=20),
                      xaxis={'showgrid': False}, yaxis={'showgrid': False},
                      legend_font_size=16)

    # Set x-axis title
    fig.update_xaxes(title_text="Date", title_font=dict(size=16), tickfont=dict(size=14))

    # Set y-axes titles
    fig.update_yaxes(title_text="No. of new cases/million", secondary_y=False, title_font=dict(size=16),
                     tickfont=dict(size=14))
    fig.update_yaxes(title_text="No. of new vaccinations", secondary_y=True, title_font=dict(size=16),
                     tickfont=dict(size=14))

    return fig




