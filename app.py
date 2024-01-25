from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

sales_data = pd.read_csv('pink_morsel_sales.csv')

app.layout = html.Div([
    html.Div(children='Hello Dash Show Me Pink Morsel Sales'),
    dash_table.DataTable(data=sales_data.to_dict('records'), page_size=10),
    dcc.Graph(figure=px.line(sales_data, x='Date', y='Sales', title='Pink Morsel Sales In All Regions', color='Region'))
])

if __name__ == '__main__':
    app.run_server(debug=True)