import yfinance as yf
import streamlit as st

st.write("""
## Simple Stock Price App by Surya(Vit Bhopal)
Shown are the ***stock closing*** price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
inputt = "Enter the share Company (clear this text, Stock Name (eg. 'GOOGL' for Google) and press  CTRL + Enter"
innp = st.text_area("Input",inputt,height=25)
#tickerSymbol = 'ITC'
#get data on this ticker
tickerData = yf.Ticker(innp)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2020-5-31', end='2021-9-25')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
