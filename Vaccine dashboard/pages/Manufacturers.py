import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


dash.register_page(__name__)

df2 = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv')

layout = html.Div([
    html.Label('COUNTRY: ', style={'textAlign': 'left',
                                   'fontSize': 20,
                                   'color': 'white'}),
    dcc.Dropdown(options = [x for x in df2.location.unique()], id='location-choice',
                 value = 'European Union', style={'width': '50%', 'backgroundColor': '#111111', 'borderColor': 'white'}),
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Graph(id='Manufacturers', figure={})),
        dbc.Col(dcc.Graph(id='Percentage_manuf', figure={}))
    ])
])


@callback(
    Output('Manufacturers', 'figure'),
    Input('location-choice', 'value')
)
def update_graph4(selected_country):
    countries = df2.loc[df2.location == selected_country].copy()
    fig4 = px.line(countries, x="date", y="total_vaccinations",
                  color='vaccine',
                  template="plotly_dark",
                   width=800, height=500,
                   color_discrete_sequence=px.colors.sequential.Plasma
                   )
    fig4.update_layout(
        legend_font=dict(size=14),
        title=f"Vaccine doses by manufacturer over time",
        legend_title='Manufacturer', title_font=dict(size=18.5),
        legend_font_size=14)
    fig4.update_traces(line=dict(width=3))
    fig4.update_xaxes(title_text="Date", title_font=dict(size=16), tickfont=dict(size=14))
    fig4.update_yaxes(title_text="No. of vaccine doses (cumulative)", title_font=dict(size=16), tickfont=dict(size=14))
    return fig4



@callback(
    Output('Percentage_manuf', 'figure'),
    Input('location-choice', 'value')
)
def update_graph5(selected_country):
    country = df2.loc[df2.location == selected_country].copy()
    country = country.groupby('vaccine')[['total_vaccinations', 'date']].max()
    fig5 = px.treemap(country, path=[country.index], values='total_vaccinations',
                     template="plotly_dark", width=550, height=500, hover_data=['total_vaccinations'],
                      color_discrete_sequence= px.colors.sequential.Plasma)
    fig5.update_traces(textinfo='label+value', textfont=dict(size=14))
    fig5.update_layout(title="Poportion of each vaccine manufacturer",
                      title_x=0.5, title_font=dict(size=18.5))
    return fig5




