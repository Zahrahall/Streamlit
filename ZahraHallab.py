import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit import components
#########################################################################################################################



df = pd.read_csv('monthly wages.csv')





st.set_page_config(page_title = 'Zahra Dashboard',
                    page_icon = 'bar_chart:',
                    layout = 'wide'
)
#Create a selectbox for tab selection
selected_tab = st.sidebar.radio("Select a tab:", ("Main page", "Visualizations"))
if selected_tab == "Main page":
    st.header("Average monthly wages for working male and female over the years")

    # You can add more content here, such as charts or images
    st.image("https://th.bing.com/th/id/OIP.6PWkkI1Gr4rgGL62sfH-fgHaE8?w=246&h=180&c=7&r=0&o=5&pid=1.7",use_column_width=True)
    st.write('throughout the years, it is widely known that female monthly wages are less than male monthly wages. what about today?')
elif selected_tab == "":
    st.header("Charts")

    st.set_option('deprecation.showPyplotGlobalUse', False)
##################################################################################################################################

 # Create a dictionary to store the session state
session_state = st.session_state


st.subheader("Bar Chart - Monthly wages by Gender")
# Create a sidebar for filters
st.sidebar.header("select a country")
selected_countries = st.sidebar.multiselect("Select Countries:", df['country'].unique())

# Filter the data based on selected countries
filtered_df = df[df['country'].isin(selected_countries)]


bar_fig = px.scatter(filtered_df,x='country',y='amount_adj_usd_currency',color='gender',hover_name='gender')
st.plotly_chart(bar_fig)


# Line Chart - Trend over Time in France
st.subheader("")
line =px.scatter(df,x='year',y='amount_adj_usd_currency',color='country',size='amount_adj_usd_currency',hover_name='gender')

st.plotly_chart(line)
