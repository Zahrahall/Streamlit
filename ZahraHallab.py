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
    st.image("https://th.bing.com/th/id/OIP.6PWkkI1Gr4rgGL62sfH-fgHaE8?w=246&h=180&c=7&r=0&o=5&pid=1.7", use_column_width=True)
    st.write('Throughout the years, it is widely known that female monthly wages are less than male monthly wages. What about today?')
    st.write('The data reveals a pattern of inequality, with female monthly wages consistently trailing behind those of their male counterparts. Despite ongoing efforts to address gender wage disparities, this study finds that a gender pay gap still persists, raising questions about the root causes and potential solutions. It is evident that economic and societal factors continue to influence the wage differential between genders in European countries.The research employs statistical analysis and visualization techniques to provide insights into the wage gaps, illustrating how they vary across countries and over the years.')

def page_1():
    st.header("monthly wages from 2009-2022")
    st.sidebar.subheader("Year Playback")
    
    # Year slicer in the sidebar
    selected_year = st.sidebar.slider("Select Year", min_value=df['year'].min(), max_value=df['year'].max(), value=df['year'].min())
    
    # Playback control
    play = st.sidebar.checkbox("Auto-play Years")
    
    # Filter the data based on the selected year
    filtered_df = df[df['year'] == selected_year]
    
    line = px.scatter(filtered_df, x='year', y='amount_adj_usd_currency', color='country', size='amount_adj_usd_currency', hover_name='gender')
    
    st.plotly_chart(line)
    
    if play:
        # Auto-play through the years
        while selected_year < df['year'].max():
            time.sleep(1)  # Pause for 1 second between years
            selected_year += 1
            st.sidebar.slider("Select Year", min_value=df['year'].min(), max_value=df['year'].max(), value=selected_year)
            st.empty()  # Clear the plot to update it with the new year
            filtered_df = df[df['year'] == selected_year]
            line = px.scatter(filtered_df, x='year', y='amount_adj_usd_currency', color='country', size='amount_adj_usd_currency', hover_name='gender')
            st.plotly_chart(line)

def page_2():
    st.header("Compare monthly wages by country by gender ")
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
