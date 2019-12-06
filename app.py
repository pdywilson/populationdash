import collections
import dash
import pandas as pd

from dash.dependencies import Output, Input
from dash.exceptions import PreventUpdate

import dash_html_components as html
import dash_core_components as dcc
import dash_table

app = dash.Dash(__name__)

server = app.server

df = pd.read_csv('data/data1.csv') # data from: https://data.worldbank.org/indicator/SP.POP.TOTL

countries = set(df['Country Name'])

app.layout = html.Div([
    dcc.Store(id='memory-output'),
    html.H1(
            children='Population',
            style={'textAlign': 'center'}
            ),
    dcc.Dropdown(id='memory-countries', options=[
        {'value': x, 'label': x} for x in countries
    ], multi=True, value=['Germany', 'Ireland', 'United Kingdom','Australia']),
    html.Div([
        dcc.Graph(id='memory-graph')
    ]),
    dcc.Markdown('''
        Data taken from [worldbank.org](https://data.worldbank.org/indicator/SP.POP.TOTL), License: CC BY-4.0.
        '''
    )
])

@app.callback(Output('memory-output', 'data'),
              [Input('memory-countries', 'value')])
def filter_countries(countries_selected):
    if not countries_selected:
        return {}

    filtered = df.loc[df['Country Name'].isin(countries_selected)]

    return filtered.to_dict('records')



@app.callback(Output('memory-graph', 'figure'),
              [Input('memory-output', 'data')])
def on_data_set_graph(data):
    if data is None:
        raise PreventUpdate

    result = []

    years = list(range(1960,2019))

    for row in data:
        x, y = [], []
        for year in years:
            population = row[str(year)]
            x.append(year)
            y.append(population)
        result.append({'name': row['Country Name'], 'mode': 'lines+markers', 'x': x, 'y': y})

    return {
        'data': result
    }

if __name__ == '__main__':
    app.run_server(debug=True, threaded=True, port=8050)