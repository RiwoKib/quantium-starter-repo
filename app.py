from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)

sales_data = pd.read_csv('pink_morsel_sales.csv')

app.layout = html.Div([
    html.Div(children='Hello Dash Show Me Pink Morsel Sales'),
    dash_table.DataTable(data=sales_data.to_dict('records'), page_size=10),

    html.Label('Select Region'),
    dcc.RadioItems(options=[{'label': 'North', 'value':'north'}, 
                            {'label':'South:', 'value':'south'}, 
                            {'label':'East:', 'value':'east'}, 
                            {'label':'West', 'value':'west'},
                            {'label':'All', 'value':'all'}],
                    value='all', 
                    id='region_filter',
                    labelStyle={'display':'inline-block'}),

    dcc.Graph(id='graph_display')
])


#controls for regions
@callback(
    Output(component_id='graph_display', component_property='figure'),
    Input(component_id='region_filter', component_property='value')
)

def update_graph(region_chosen):
    if region_chosen == 'all':
        regional_sales = sales_data
    else:
        regional_sales = sales_data[sales_data['Region'] == region_chosen]

    fig = px.line(regional_sales, x='Date', y='Sales', title='Pink Morsel Sales', color='Region')

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)