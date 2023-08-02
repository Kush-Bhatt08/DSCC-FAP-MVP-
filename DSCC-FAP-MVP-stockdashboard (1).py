import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import flask

# Define the Flask app
app = flask.Flask(__name__)

# Function to get stock data and create visualizations
def create_stock_dashboard(stock_ticker):
    # Fetch stock data from Yahoo Finance
    data = yf.download(stock_ticker, period="1y")

    # Create line charts for closing prices and volume
    line_chart_close = go.Scatter(x=data.index, y=data["Close"], mode="lines", name="Close Price")
    line_chart_open = go.Scatter(x=data.index, y=data["Open"], mode="lines", name="Open Price")
    bar_chart_volume = go.Line(x=data.index, y=data["Volume"], name="Volume")

    # Layout for the chart
    layout = go.Layout(title=f"{stock_ticker} Stock Data", xaxis=dict(title="Date"), yaxis=dict(title="Price"))

    # Create the figure
    fig = go.Figure(data=[line_chart_close, line_chart_open, bar_chart_volume], layout=layout)

    # Convert the figure to JSON
    chart_json = fig.to_json()

    return chart_json

# Define the route for the dashboard
@app.route("/")
def dashboard():
    # Default stock ticker (Apple)
    default_stock_ticker = "AAPL"

    # Get the selected stock ticker from the query parameters
    selected_stock_ticker = flask.request.args.get("stock_ticker", default_stock_ticker)

    # Fetch the stock data and create the dashboard
    chart_json = create_stock_dashboard(selected_stock_ticker)

    # Create HTML content for the dashboard
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stock Dashboard</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    </head>
    <body>
        <h1>Stock Dashboard</h1>
        <div>
            <form method="get">
                <label for="stock_ticker">Select Stock:</label>
                <select id="stock_ticker" name="stock_ticker" onchange="this.form.submit()">
                    <option value="AAPL" {'selected' if selected_stock_ticker == 'AAPL' else ''}>Apple</option>
                    <option value="005930.KS" {'selected' if selected_stock_ticker == '005930.KS' else ''}>Samsung</option>
                </select>
            </form>
        </div>
        <div id="chart"></div>
        <script>
            var chartData = {chart_json};
            Plotly.newPlot('chart', chartData.data, chartData.layout);
        </script>
    </body>
    </html>
    """

    return html_content

if __name__ == "__main__":
    app.run(debug=True)
