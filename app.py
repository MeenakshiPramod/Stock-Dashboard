import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

# Set up the Streamlit app title
st.title('StockLens: Stock Analysis Dashboard')

# Sidebar inputs for ticker and date range
ticker = st.sidebar.text_input('Ticker', 'AAPL')
start_date = st.sidebar.date_input('Start Date', value=pd.to_datetime('2022-01-01'))
end_date = st.sidebar.date_input('End Date', value=pd.to_datetime('2025-01-01'))

# Download stock data using yfinance
data = yf.download(ticker, start=start_date, end=end_date)

# Check if data is downloaded successfully
if not data.empty:
    # Convert the 'Close' column to a 1D array
    close_prices = data['Close'].values.flatten()  # Convert to 1D array

    # Plot the closing price using Plotly
    fig = px.line(data, x=data.index, y=close_prices, title=f'{ticker} Stock Price')
    st.plotly_chart(fig)
else:
    st.error("No data found for the given ticker and date range.")

# Create tabs for Pricing Data, Fundamental Data, and News
pricing_data, fundamental_data, news = st.tabs(["Pricing Data", "Fundamental Data", "Top 10 News"])

with pricing_data:
    st.header('Price Movements')
    data2 = data.copy()

    # Add the 'Daily % Change' column to data2
    #data2['%Change'] = data['Close'].pct_change() * 100
    data2['% Change']=data['Close']/data['Close'].shift(1)-1
    data2.dropna(inplace=True)

    # Display the modified DataFrame
    st.dataframe(data2)
    annual_return=data2['% Change'].mean()*252*100
    st.write('Annual Return:',annual_return,'%')
    stdev=np.std(data2['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is ',stdev*100,'%')
    st.write('Risk Adjusted Return is ',annual_return/(stdev*100))



from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
    key='QCGWAAZWR2TK1Z02'
    fd=FundamentalData(key,output_format='pandas')
    st.subheader('Balance Sheet')
    balance_sheet=fd.get_balance_sheet_annual(ticker)[0]
    bs=balance_sheet.T[2:]
    bs.columns=list(balance_sheet.T.iloc[0])
    st.write(bs)
    st.subheader('Income Statement')
    income_statement=fd.get_income_statement_annual(ticker)[0]
    is1=income_statement.T[2:]
    is1.colums=list(income_statement.T.iloc[0])
    st.write(is1)
    st.subheader('Cash Flow Statement')
    cash_flow=fd.get_cash_flow_annual(ticker)[0]
    cf=cash_flow.T[2:]
    cf.colums=list(cash_flow.T.iloc[0])
    st.write(cf)


from stocknews import StockNews
with news:
    st.header(f'News of {ticker}')
    sn=StockNews(ticker,save_news=False)
    df_news=sn.read_rss()
    for i in range(10):
        st.subheader(f'News {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])
        title_sentiment=df_news['sentiment_title'][i]
        st.write(f'Title Sentiment {title_sentiment}')
        news_sentiment=df_news['sentiment_summary'][i]
        st.write(f'News Sentiment {news_sentiment}')
    