import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objects as go
import yfinance as yf

# Download stock data for Tesla and Ford from Yahoo Finance
tesla_data = yf.download("TSLA", start="2021-01-01", end="2021-12-31")
ford_data = yf.download("F", start="2021-01-01", end="2021-12-31")

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1('Stock Data Dashboard'),
    dcc.Dropdown(
        id='stock-dropdown',
        options=[
            {'label': 'Tesla', 'value': 'Tesla'},
            {'label': 'Ford', 'value': 'Ford'}
        ],
        value='Tesla'
    ),
    dcc.Dropdown(
        id='month-dropdown',
        options=[
            {'label': month, 'value': month} for month in tesla_data.index.month_name().unique()
        ],
        value=tesla_data.index.month_name().unique()[0],
        clearable=False
    ),
    dcc.Graph(id='stock-graph'),
    html.Div(id='statistics')
])

# Define the callbacks
@app.callback(
    Output('stock-graph', 'figure'),
    Output('statistics', 'children'),
    Input('stock-dropdown', 'value'),
    Input('month-dropdown', 'value')
)
def update_graph(stock, month):
    data = tesla_data if stock == 'Tesla' else ford_data
    # Filter the data for the selected month
    filtered_data = data[data.index.month_name() == month]
    # Create a candlestick chart
    figure = go.Figure(data=[
        go.Candlestick(
            x=filtered_data.index,
            open=filtered_data['Open'],
            high=filtered_data['High'],
            low=filtered_data['Low'],
            close=filtered_data['Close']
        )
    ])
    # Set the chart title
    figure.update_layout(
        title=f'{stock} Stock Data ({month})',
        xaxis_rangeslider_visible=False
    )
    # Calculate statistics
    stats = filtered_data.describe().loc[['mean', 'std', 'min', '25%', '50%', '75%', 'max']]
    # Generate HTML table for statistics
    table = html.Table(
        # Header
        [html.Tr([html.Th(col) for col in stats.columns])] +
        # Rows
        [html.Tr([html.Td(stats.loc[row, col]) for col in stats.columns]) for row in stats.index]
    )
    return figure, table

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
