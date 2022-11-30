import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
st.write("""
## Чек и чаевые
Динамика цен на заказы и размер чаевых
""")
tipsdf = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')
#ticsymbl = 'AAPL'
#ticdata = yf.Ticker(ticsymbl)
#ticdf = ticdata.history(period = 'id', start = '2001-01-01', end = '2011-01-01')
#st.line_chart(ticdf.Volume)
st.line_chart(tipsdf[['total_bill','tip']])

st.write("""
## Зависимость чаевых от суммы заказа

""")

figplt = px.scatter(tipsdf, x='total_bill', y='tip')

st.write(figplt)

#plt.xlabel("Сумма заказа")
#plt.ylabel("Чаевые")
#plt.scatter(tipsdf['total_bill'], tipsdf['tip'], 
#            c=tipsdf['total_bill'], 
#            s=tipsdf['total_bill']*tipsdf['tip'],
#            alpha=0.95,
#            cmap='jet')
#plt.colorbar(); 
#plt.show()
#st.write(plt)