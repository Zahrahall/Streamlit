import pandas as pd
import streamlit as st
import pandas as pd
import plotly.express as px

from streamlit import components
#########################################################################################################################



df = pd.read_csv('average_hourly_earnings_of_female_and_male_employees_(managers)_local_currency.csv')

st.set_page_config(page_title = 'Zahra Dashboard',
                    page_icon = 'bar_chart:',
                    layout = 'wide'
)

st.set_option('deprecation.showPyplotGlobalUse', False)
##################################################################################################################################

# Create a dictionary to store the session state
session_state = st.session_state


st.subheader("Bar Chart - Amount by Gender")
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
