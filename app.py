import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

df_web = pd.read_html('https://www.bog.gov.gh/treasury-and-the-markets/treasury-bill-rates/')



st.title('Updating my first Deploying my first App')
st.write(df_web)
# st.write("Here's our first attempt at using data to create a table:")
# st.write(pd.DataFrame({
# 'first column': [1, 2, 3, 4],
# 'second column': [10, 20, 30, 40]
# }))

# """
# # My first app
# Here's our first attempt at using data to create a table:
# """
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
# df

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

# st.line_chart(chart_data)

if st.sidebar.checkbox('Show Map'):
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(map_data)

if st.sidebar.checkbox('Show Graph'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)

option = st.sidebar.selectbox('Which number do you like best?', df['second column'])
st.write('You selected: ', option)

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")
    expander = st.beta_expander("FAQ")
    expander.write("Here you could put in some really, really long explanations...")

exp = st.beta_expander("Tag")
exp = exp.write("Here be now...")
