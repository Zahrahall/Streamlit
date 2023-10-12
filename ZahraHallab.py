import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('monthly wages.csv')

st.set_page_config(
    page_title='Zahra Dashboard',
    page_icon=':bar_chart:',
    layout='wide'
)

def front_page():
    st.header("Average monthly wages for working male and female over the years")
    st.image('https://www.suzannevenker.com/wp-content/uploads/2019/09/menandwomen.jpeg', use_column_width=True)
    st.write('Throughout the years, it is widely known that female monthly wages are less than male monthly wages. What about today?')
    st.write('The data reveals a pattern of inequality, with female monthly wages consistently trailing behind those of their male counterparts. Despite ongoing efforts to address gender wage disparities, this study finds that a gender pay gap still persists, raising questions about the root causes and potential solutions. It is evident that economic and societal factors continue to influence the wage differential between genders in European countries.The research employs statistical analysis and visualization techniques to provide insights into the wage gaps, illustrating how they vary across countries and over the years.')

def page_1():
    st.header("Page 1 - Animated Scatter Plot")
    
    # Create an animated scatter plot
    scatter_fig = px.scatter(
        df, x='year', y='amount_adj_usd_currency', color='country', size='amount_adj_usd_currency',
        hover_name='gender', animation_frame='year', animation_group='country',
        log_x=True, range_x=[2010, 2025], range_y=[0, 400]
    )
    
    # Display the animated scatter plot
    st.plotly_chart(scatter_fig)
    st.write('in this graph we can see the changes that occured through out the above years, iceland have majorly increased wages, yet we can still spot the gap between female wages and male wages')
def page_2():
    st.header("Compare monthly wages by country by gender ")
    st.subheader("Bar Chart - Monthly wages by Gender")
    st.sidebar.header("Select a country")
    selected_countries = st.sidebar.multiselect("Select Countries:", df['country'].unique())
    selected_genders = st.sidebar.multiselect("Select Genders:", df['gender'].unique())
    filtered_df = df[(df['country'].isin(selected_countries)) & (df['gender'].isin(selected_genders))]
    bar_fig = px.scatter(filtered_df, x='country', y='amount_adj_usd_currency', color='gender', hover_name='gender')
    st.plotly_chart(bar_fig)
    st.write('in this graph we can compare wages in these different 5 europeoan countries and check femaleand male monthly salaries in each different countries.again we can spot that Iceland have a significant increase in wages in the last couple of years yet male wage is still significantly higher than female monthly wage')
    st.write('why?')
    st.write('This may be due to several factors economical or societal')

page = st.sidebar.radio("Select a Page", ['Front Page', 'Page 1', 'Page 2'])
if page == 'Front Page':
    front_page()
elif page == 'Page 1':
    page_1()
elif page == 'Page 2':
    page_2()
