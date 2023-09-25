import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit import components
#########################################################################################################################



df = pd.read_csv('average_hourly_earnings_of_female_and_male_employees_(managers)_local_currency1.csv')





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

elif selected_tab == "":
    st.header("Charts")

    st.set_option('deprecation.showPyplotGlobalUse', False)
##################################################################################################################################

 # Create a dictionary to store the session state
session_state = st.session_state


st.subheader("Bar Chart - Monthly wages by Gender")
bar_fig = px.bar(df, x='year', y='amount_local_currency', color='gender',
                 labels={'amount_local_currency': 'Amount (Local Currency)'})
st.plotly_chart(bar_fig)


# Filter data for France
france_df = df[df['country'] == 'France']

# Line Chart - Trend over Time in France
st.subheader("Line Chart - Trend over Time in France")
line_fig = px.line(france_df, x='year', y='amount_local_currency', color='gender',
                   labels={'amount_local_currency': 'Amount (Local Currency)'})
st.plotly_chart(line_fig)
