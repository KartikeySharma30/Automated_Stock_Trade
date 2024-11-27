import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

# Helper functions
def fetch_stock_data(ticker, period  = 'max'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def calculate_bollinger_bands(data, window=20, no_of_std=2):
    data['SMA'] = data['Close'].rolling(window=window).mean()
    data['STD'] = data['Close'].rolling(window=window).std()
    data['Upper Band'] = data['SMA'] + (no_of_std * data['STD'])
    data['Lower Band'] = data['SMA'] - (no_of_std * data['STD'])
    return data

def calculate_sma(data, short_window=50, long_window=200):
    data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
    data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()
    return data

def apply_bollinger_strategy(data):
    data['Signal'] = 0
    data['Signal'][data['Close'] < data['Lower Band']] = 1  # Buy signal
    data['Signal'][data['Close'] > data['Upper Band']] = -1 # Sell signal
    return data

def apply_sma_strategy(data):
    data['Signal'] = 0
    data['Signal'][data['SMA_Short'] > data['SMA_Long']] = 1   # Buy signal
    data['Signal'][data['SMA_Short'] < data['SMA_Long']] = -1  # Sell signal
    return data

def adjust_strategy_parameters(style):
    if style == 'Aggressive':
        return {'bollinger_window': 10, 'bollinger_std': 1.5, 'sma_short': 20, 'sma_long': 50}
    elif style == 'Moderate':
        return {'bollinger_window': 20, 'bollinger_std': 2, 'sma_short': 50, 'sma_long': 200}
    elif style == 'Passive':
        return {'bollinger_window': 30, 'bollinger_std': 2.5, 'sma_short': 100, 'sma_long': 300}
    return {'bollinger_window': 20, 'bollinger_std': 2, 'sma_short': 50, 'sma_long': 200}

def calculate_investment_growth(data, amount, style):
    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]
    style_multipliers = {'Aggressive': 1.5, 'Moderate': 1.0, 'Passive': 0.75}
    if style not in style_multipliers:
        raise ValueError("Invalid investment style. Choose from 'Aggressive', 'Moderate', or 'Passive'.")
    multiplier = style_multipliers[style]
    growth = (end_price / start_price) * amount * multiplier
    roi = ((growth - amount) / amount) * 100
    investment_trend = (data['Close'] / start_price) * amount * multiplier
    data[f'{style} Growth'] = investment_trend
    return data, growth, roi

def plot_investment_comparison(data, styles):
    fig = go.Figure()
    for style in styles:
        if f'{style} Growth' in data:
            fig.add_trace(go.Scatter(
                x=data.index, y=data[f'{style} Growth'],
                mode='lines', name=f"{style} Investment",
                line=dict(width=2)
            ))
    fig.update_layout(
        title="Investment Growth Comparison",
        xaxis_title="Date",
        yaxis_title="Investment Value",
        template="plotly_white",
        height=600,
        width=900
    )
    st.plotly_chart(fig)

def visualize_interactive(data, strategy_name, initial_capital, target_currency='INR'):
    fig1 = go.Figure()

    # Plot Close Price
    fig1.add_trace(go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close'],
        name='Price'
    ))

    if strategy_name == 'Bollinger Bands':
        fig1.add_trace(go.Scatter(x=data.index, y=data['Upper Band'], mode='lines', name='Upper Band', line=dict(dash='dash', color='red')))
        fig1.add_trace(go.Scatter(x=data.index, y=data['Lower Band'], mode='lines', name='Lower Band', line=dict(dash='dash', color='green')))
    
    elif strategy_name == 'SMA Crossover':
        fig1.add_trace(go.Scatter(x=data.index, y=data['SMA_Short'], mode='lines', name='Short-term SMA', line=dict(color='orange')))
        fig1.add_trace(go.Scatter(x=data.index, y=data['SMA_Long'], mode='lines', name='Long-term SMA', line=dict(color='purple')))

    # Add Buy and Sell signals
    fig1.add_trace(go.Scatter(x=data[data['Signal'] == 1].index, y=data[data['Signal'] == 1]['Close'], mode='markers', name='Buy Signal', marker=dict(symbol='triangle-up', color='green', size=8)))
    fig1.add_trace(go.Scatter(x=data[data['Signal'] == -1].index, y=data[data['Signal'] == -1]['Close'], mode='markers', name='Sell Signal', marker=dict(symbol='triangle-down', color='red', size=8)))

    fig1.update_layout(title=f'{strategy_name} Strategy - Buy/Sell Signals', xaxis_title='Date', yaxis_title='Price', showlegend=True, height=800, width=1200)
    st.plotly_chart(fig1)

# Main function for the Streamlit app
def main():
    st.title("Stock Strategy Analyzer")

    # Data source
    data_source = st.selectbox("Select Data Source", ["Upload CSV", "Enter Ticker Symbol"])
    data = None

    if data_source == "Upload CSV":
        uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
        if uploaded_file is not None:
            data = pd.read_csv(uploaded_file, parse_dates=['Date'])
            data.set_index('Date', inplace=True)
            st.write(data)  # Display the first few rows of the data

    elif data_source == "Enter Ticker Symbol":
        ticker = st.text_input("Enter Ticker Symbol", "AAPL")
        if ticker:
            data = fetch_stock_data(ticker, period="max")
            st.write(data)  # Display the first few rows of the data

    if data is not None:
        # 3. Choose Strategy
        strategy = st.selectbox("Choose Strategy", ["Bollinger Bands", "SMA Crossover"])
        
        # 4. Select Investment Style
        investment_style = st.selectbox("Select Investment Style", ["Aggressive", "Moderate", "Passive"])
        
        # 5. Initial Capital
        initial_capital = st.number_input("Enter Initial Capital", min_value=1000, value=10000)
        
        # 6. Enter Start and End Date
        start_date = st.text_input("Enter Start Date (YYYY-MM-DD)", "2020-01-01", key="start_date")
        end_date = st.text_input("Enter End Date (YYYY-MM-DD)", "2021-01-01", key="end_date")
        
        # Convert to datetime format
        try:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
            if end_date < start_date:
                st.error("End date must be later than start date")
        except Exception as e:
            st.error(f"Invalid date format: {e}")
        
        # 7. Analyze Stock Button
        if st.button("Analyze Stock"):
            if data is not None:
                # Apply the chosen strategy
                if strategy == "Bollinger Bands":
                    data = calculate_bollinger_bands(data)
                    data = apply_bollinger_strategy(data)
                elif strategy == "SMA Crossover":
                    data = calculate_sma(data)
                    data = apply_sma_strategy(data)
                
                # Adjust strategy parameters based on investment style
                params = adjust_strategy_parameters(investment_style)
                
                # Visualize strategy execution and investment growth
                st.subheader("Visualizing investment growth")


                # Display the interactive plot for the chosen strategy
                visualize_interactive(data, strategy, initial_capital)


                styles = ["Aggressive", "Moderate", "Passive"]
                results = {}
                for style in styles:
                    data, growth, roi = calculate_investment_growth(data, initial_capital, style)
                    results[style] = (growth, roi)
                    st.write(f"{style} Style Results:")
                    st.write(f"Final Investment Value: {growth:.2f}")
                    st.write(f"ROI: {roi:.2f}%")
                    st.write('\n')

                # Visualize the growth comparison of all investment styles
                plot_investment_comparison(data, styles)
                                             

if __name__ == "__main__":
    main()
