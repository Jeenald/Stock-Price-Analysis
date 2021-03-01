#pip install yfinance
#pip install stteamlit
#for running this app.... streamlit run StockPrice.py


import yfinance as yf
import streamlit as st
#import panda as pd

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of APPLE..!!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'AAPL' # ticker symbol for google, is GOOGL... for apple AAPL

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2021-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Vloume price
""")
st.line_chart(tickerDf.Volume)

#mark down cheat sheet for additional stuff