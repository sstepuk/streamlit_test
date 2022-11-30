import yfinance as yf
import streamlit as st
import pandas as pd
st.write("""
# Стоимость акций Apple
Цены закрытия и объем торгов акций Apple
""")
ticsymbl = 'AAPL'
ticdata = yf.Ticker(ticsymbl)
ticdf = ticdata.history(period = 'id', start = '2001-01-01', end = '2011-01-01')

st.line_chart(ticdf.Volume)
st.line_chart(ticdf.Close)

