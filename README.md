# Stock Strategy Analyzer
This is an interactive Streamlit-based application that helps users analyze and visualize stock trading strategies, including Bollinger Bands and SMA Crossover, while simulating investment growth across different styles: Aggressive, Moderate, and Passive.

## Features
- <b>Real-time Stock Data Retrieval:</b> Fetch historical stock data using the Yahoo Finance API.
- <b>Strategy Analysis:</b>
  - <b>Bollinger Bands:</b> Visualize buy/sell signals based on price deviations from moving averages.
  - <b>SMA Crossover:</b> Identify trends by analyzing short-term and long-term simple moving averages.
- <b>Investment Simulation:</b> Calculate portfolio growth and ROI based on different trading styles.
- <b>Dynamic Visualizations:</b>
  - Interactive candlestick charts with buy/sell markers.
  - Investment growth comparison for multiple styles.
- Custom Input Options: Choose data source, strategy, investment style, and time range for analysis.

## Prerequisites
Ensure the following are installed:

Python 3.8 or higher 

- Required Python libraries:
  <b><u>pip install streamlit pandas plotly numpy yfinance</u></b>

Getting Started
- Clone the Repository
  git clone https://github.com/KartikeySharma30/Automated_Stock_Trade.git

  cd Automated_Stock_Trade
- Run the Application
Launch the Streamlit app:

  streamlit run <app_name>.py
  
- Explore the Application
  - Data Source: Upload a CSV or enter a stock ticker symbol (e.g., "AAPL").
  - Choose Strategy: Select between Bollinger Bands or SMA Crossover.
  - Set Parameters: Customize the investment style, time range, and initial capital.
  - Click Analyze Stock to visualize strategies and compare investment growth.

## Application Flow
- Select Data Source: Choose between uploading historical stock data or fetching it using a stock ticker.
- Choose Strategy:
  - <b>Bollinger Bands:</b> Displays upper and lower bands based on the moving average and standard deviation.
  - <b>SMA Crossover:</b> Shows short-term and long-term moving averages and crossover points.
- Simulate Investment Growth:
  - <b>Styles: Aggressive, Moderate, or Passive.</b>
  - <b>ROI and growth are calculated based on capital and price movement.</b>
- Visualize Results:
  - Interactive candlestick charts for strategy execution.
  - Line plots for investment growth comparison.

## Key Functions Overview

- Function	Description
  - fetch_stock_data	Retrieves historical stock data from Yahoo Finance API.
  - calculate_bollinger_bands	Computes moving average, upper, and lower bands.
  - apply_bollinger_strategy	Generates buy/sell signals based on Bollinger Band thresholds.
  - calculate_sma	Computes short-term and long-term moving averages.
  - apply_sma_strategy	Generates buy/sell signals based on SMA crossovers.
  - calculate_investment_growth	Simulates portfolio growth and calculates ROI based on investment style.
  - visualize_interactive	Displays interactive candlestick charts with buy/sell markers and growth trends.
  - plot_investment_comparison	Compares investment growth across styles.

## Screenshots

<img width="778" alt="Screenshot 2024-11-27 at 10 31 49 AM" src="https://github.com/user-attachments/assets/5ae37e7e-16ad-44e9-923e-97077c56d5da">

<img width="783" alt="Screenshot 2024-11-27 at 10 31 04 AM" src="https://github.com/user-attachments/assets/19e01700-635e-4eb2-9b9d-75f0cd9033fb">

<img width="743" alt="Screenshot 2024-11-27 at 10 31 34 AM" src="https://github.com/user-attachments/assets/a3ac34ab-c743-43be-83d0-993fc6891ddc">

<img width="729" alt="Screenshot 2024-11-27 at 10 32 28 AM" src="https://github.com/user-attachments/assets/643a4eb0-30cf-49c6-8c49-9625d98300eb">

<img width="741" alt="Screenshot 2024-11-27 at 10 33 21 AM" src="https://github.com/user-attachments/assets/5c49d284-22be-4ea4-8c3b-5f16be8697d2">

<img width="749" alt="Screenshot 2024-11-27 at 10 33 36 AM" src="https://github.com/user-attachments/assets/ba808b39-8a5c-48ec-b97a-689724244af1">

<img width="747" alt="Screenshot 2024-11-27 at 10 33 54 AM" src="https://github.com/user-attachments/assets/bcb83770-fc84-46d3-88ca-49f4289ea36c">

- Interactive Strategy Visualization

<img width="582" alt="Screenshot 2024-11-27 at 10 34 19 AM" src="https://github.com/user-attachments/assets/bb096165-ab0d-42c2-87ef-e5c560a8cc92">

<img width="357" alt="Screenshot 2024-11-27 at 10 34 31 AM" src="https://github.com/user-attachments/assets/7c1b7e74-31fd-4b94-9ccc-a28d6c529856">

- Investment Growth Comparison

<img width="591" alt="Screenshot 2024-11-27 at 10 35 06 AM" src="https://github.com/user-attachments/assets/d74b600c-82dd-469f-b078-6d78969da730">
