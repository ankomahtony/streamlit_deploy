import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import extract
from extract import *
import matplotlib.pyplot as plt
import squarify

html_url = "https://finance.yahoo.com/quote/BTC-USD/history?p=APPLE"
load_data_csv(html_url)
df_web = pd.read_csv('dataset.csv', thousands=',')

st.title('Updating my first Deploying my first App')
st.write(df_web)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

if st.checkbox('Show Chart'):
    options = ['Open','High','Low','Close*','Adj Close**']
    option = st.selectbox("Select Price to display chart",['All','Open','High','Low','Close*','Adj Close**'])
    # df = df_web[['Price (Intraday)','Name']]
    # df = df.dropna()
    # prices = df["Price (Intraday)"]
    # df['Price (Intraday)'] = prices.apply(np.ceil)
    # prices = prices.apply(atof)
    # fig, ax = plt.subplots(figsize=(7,5))
    # ax=squarify.plot(sizes=df['Price (Intraday)'],label=df['Name'])
    # # plt.axis('off')
    # st.pyplot(fig)
    # st.write(df)
    if(option=='All'):
        st.line_chart(df_web[options])
    else:
        st.line_chart(df_web[option])


# if st.sidebar.checkbox('Show Map'):
#     map_data = pd.DataFrame(
#         np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#         columns=['lat', 'lon'])
#     st.map(map_data)


left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")

exp = st.beta_expander("Tag")
exp = exp.write("Here be now...")
