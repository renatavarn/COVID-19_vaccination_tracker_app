import dash
from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px


dash.register_page(__name__)

df2 = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations-by-manufacturer.csv')

layout = html.Div([
    html.Label('VACCINE: ', style={'textAlign': 'left',
                                   'fontSize': 20,
                                   'color': 'white'}),
    dcc.Dropdown(options=[x for x in df2.vaccine.unique()], id='vaccine-choice',
                 value='Moderna', style={'width':'50%', 'backgroundColor': '#111111', 'borderColor': 'white'}),
    html.Br(),
    dbc.Row([
        dbc.Col(dcc.Graph(id='Countries', figure={})),
        dbc.Col(dcc.Graph(id='Map', figure={}))
    ])
])




@callback(
    Output('Countries', 'figure'),
    Input('vaccine-choice', 'value')
)
def update_graph2(selected_vaccine):
    vacc_minus_eu = df2.loc[(df2.location != 'European Union') & (df2.vaccine == selected_vaccine)].copy()

    vacc_totals = vacc_minus_eu.groupby(['location'])[['total_vaccinations', 'date']].max().nlargest(
        columns='total_vaccinations', n=10).sort_values(by='total_vaccinations', ascending=True)

    fig2 = px.bar(vacc_totals, y=vacc_totals.index, x='total_vaccinations', log_x=False,
                 template="plotly_dark", width=500, height=450,
                 orientation='h')
    fig2.update_layout(showlegend=False, title=f"Top countries for this manufacturer",
                      title_font=dict(size=18.5))
    fig2.update_traces(marker_color='#1562A9')
    fig2.update_xaxes(title_text="No. of vaccine doses (cumulative)", title_font=dict(size=16), tickfont=dict(size=14))
    fig2.update_yaxes(title_text="Country", title_font=dict(size=16), tickfont=dict(size=14))
    return fig2



@callback(
    Output('Map', 'figure'),
    Input('vaccine-choice', 'value')
)
def update_graph3(selected_vaccine):
    vacc_minus_eu = df2.loc[(df2.location != 'European Union') & (df2.vaccine == selected_vaccine)].copy()
    vacc_totals = vacc_minus_eu.groupby(['location'])[['total_vaccinations', 'date']].max()
    fig3 = px.choropleth(vacc_totals, locations=vacc_totals.index,
                        locationmode="country names", color='total_vaccinations',
                        scope="world",
                        width=900,
                        height=500,
                        template="plotly_dark",
                        projection='equirectangular',
                        labels={'total_vaccinations': 'No. of vaccine doses'},
                        color_continuous_scale=px.colors.sequential.Blues
                        )
    fig3.update_layout(coloraxis_colorbar=dict(
        thicknessmode="pixels", thickness=10,
        lenmode="pixels", len=340
    ))
    return fig3
