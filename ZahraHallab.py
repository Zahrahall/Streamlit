import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('monthly_wages.csv')

st.set_page_config(
    page_title='Zahra Dashboard',
    page_icon=':bar_chart:',
    layout='wide'
)

def front_page():
    st.header("Average monthly wages for working male and female over the years")
    st.image("https://th.bing.com/th/id/OIP.6PWkkI1Gr4rgGL62sfH-fgHaE8?w=246&h=180&c=7&r=0&o=5&pid=1.7", use_column_width=True)
    st.write('Throughout the years, it is widely known that female monthly wages are less than male monthly wages. What about today?')

def page_1():
    st.header("Page 1")
    st.subheader("")
    line = px.scatter(df, x='year', y='amount_adj_usd_currency', color='country', size='amount_adj_usd_currency', hover_name='gender')
    st.plotly_chart(line)

def page_2():
    st.header("Page 2")
    st.subheader("Bar Chart - Monthly wages by Gender")
    st.sidebar.header("Select a country")
    selected_countries = st.sidebar.multiselect("Select Countries:", df['country'].unique())
    selected_genders = st.sidebar.multiselect("Select Genders:", df['gender'].unique())
    filtered_df = df[(df['country'].isin(selected_countries)) & (df['gender'].isin(selected_genders))]
    bar_fig = px.scatter(filtered_df, x='country', y='amount_adj_usd_currency', color='gender', hover_name='gender')
    st.plotly_chart(bar_fig)

page = st.sidebar.radio("Select a Page", ['Front Page', 'Page 1', 'Page 2'])
if page == 'Front Page':
    front_page()
elif page == 'Page 1':
    page_1()
elif page == 'Page 2':
    page_2()
