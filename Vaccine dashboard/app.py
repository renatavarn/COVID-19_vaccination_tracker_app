import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


app.layout = html.Div([
    html.Div('COVID-19 VACCINATION DASHBOARD',
             style = {'fontSize': 40, 'textAlign':'center','color': 'white'}),
    html.Div([
        dcc.Link(children=page['name']+"  |  ", href=page['path'],
                 refresh=False, style={'font-family': 'Avenir',
                                        'fontSize': 25, 'color': 'white',
                                       'font-variant-caps': 'small-caps'})
        for page in dash.page_registry.values()
    ], style = {'textAlign':'center'}),
    html.Br(),
    # Contents of each page
    dash.page_container
], style={'backgroundColor': '#111111', 'border': 'thin lightgrey', 'padding': '8px 0px 0px 8px'}
)


if __name__ == '__main__':
    app.run(debug=True)
