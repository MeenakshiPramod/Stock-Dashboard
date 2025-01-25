# StockLens: Interactive Dashboard for Analysis and Insights

A comprehensive **Stock Dashboard** built using Streamlit to provide insightful stock market analysis and data visualization. This project integrates multiple features, allowing users to monitor stock prices, analyze fundamental financial data, and stay updated with the latest news for a selected ticker.

## Link to product walkthrough
![Screenshot (2)](https://github.com/user-attachments/assets/b37c827b-7272-4d82-8227-4abd6f7bbcb0)
![Screenshot (3)](https://github.com/user-attachments/assets/80c331a7-06f9-41f0-bcbe-9183f01d9188)
![Screenshot (4)](https://github.com/user-attachments/assets/cdce2132-56a7-489a-8711-2a1139a250f6)
![Screenshot (5)](https://github.com/user-attachments/assets/b04b63a3-a283-4d69-9f14-eaaeb4c2ecbe)


## Features
- **Interactive Stock Price Visualization:**  
  Real-time stock price data displayed using Plotly for an intuitive user experience.
  
- **Financial Data Analysis:**  
  Includes Balance Sheet, Income Statement, and Cash Flow data fetched via the Alpha Vantage API.
  
- **Performance Metrics:**  
  Calculates and displays Annual Return, Standard Deviation, and Risk-Adjusted Return for the selected stock.
  
- **News Sentiment Analysis:**  
  Displays the top 10 recent news articles with sentiment scores for titles and summaries, powered by StockNews API.

## Tech Stack
- **Frontend & Dashboard:** Streamlit
- **Data Visualization:** Plotly
- **APIs Used:** 
  - Alpha Vantage (Financial Data)  
  - StockNews (News and Sentiment Analysis)  
  - Yahoo Finance (Stock Price Data)
- **Libraries:** Pandas, NumPy, yFinance

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-dashboard.git
   ```
2.  Navigate to the project directory:
   ```bash
    cd stock-dashboard
   ```
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app:
```bash
streamlit run app.py
```

