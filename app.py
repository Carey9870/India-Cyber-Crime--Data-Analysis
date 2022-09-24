import streamlit as st
import pandas as pd
import preprocessor, helper
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# load and read both datasets
cyber_C = pd.read_table('cyber_crimes.csv')

# load preprocessor.py
df = preprocessor.preprocess(cyber_C)

# sidebar ui
st.sidebar.title('Cyber Crime Analysis in India')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Rate of total cyber crimes per state', 'Category per rate of total cyber crimes per state', 'Mid Year Projected Population per State',
        'Percentage Crime Share per State', 'Crimes per State in 2016 2017 2018'
))

if user_menu == 'Rate of total cyber crimes per state':
    st.subheader('Rate of Total Cyber Crimes per State')
    rate_of_total_cyber_crimes_per_state = helper.RateOfTotalCyberCrimes(cyber_C)
    st.table(rate_of_total_cyber_crimes_per_state)
    
    # A Bar Graph Displaying rate of total cyber crimes per state
    st.subheader('A Bar Graph Displaying rate of total cyber crimes per state')
    fig = px.bar(cyber_C.groupby('State/UT')['Rate of Total Cyber Crimes (2018)++'].sum(), color=cyber_C['State/UT'])
    st.plotly_chart(fig)

if user_menu == 'Category per rate of total cyber crimes per state':
    st.subheader('Category per rate of total cyber crimes per state')
    category_Per_Rate_Of_Total_Cyber_Crimes_Per_State = helper.categoryPerRateOfTotalCyberCrimesPerState(cyber_C)
    st.table(category_Per_Rate_Of_Total_Cyber_Crimes_Per_State)
    
    # A Bar Graph Displaying category per rate of total cyber crimes per state
    st.subheader('A Bar Graph Displaying category per rate of total cyber crimes per state')
    fig = px.bar(cyber_C.groupby('Category')['Rate of Total Cyber Crimes (2018)++'].sum())
    st.plotly_chart(fig)

if user_menu == 'Mid Year Projected Population per State':
    st.subheader('Mid Year Projected Population per State')
    Mid_Year_Projected_Population_per_State = helper.Mid_Year_Projected_Population_per_State(cyber_C)
    st.table(Mid_Year_Projected_Population_per_State)
    
    # A Bar Graph Displaying Mid Year Projected Population per State
    st.subheader('A Bar Graph Displaying Mid Year Projected Population per State')
    fig = px.bar(cyber_C.groupby(['State/UT'])['Mid-Year Projected Population (in Lakhs) (2018)+'].sum(), color=cyber_C['State/UT'])
    st.plotly_chart(fig)

if user_menu == 'Percentage Crime Share per State':
    st.subheader('Percentage Crime Share per State')
    Percentage_Crime_Share_per_State = helper.PercentageCrimeSharePerState(cyber_C)
    st.table(Percentage_Crime_Share_per_State)
    
    # A Bar Graph Displaying Mid Year Projected Population per State
    st.subheader('A Bar Graph Displaying Mid Year Projected Population per State')
    fig = px.bar(cyber_C.groupby(['State/UT'])['Percentage Share of State/UT (2018)'].sum(), color=cyber_C['State/UT'])
    st.plotly_chart(fig)

if user_menu == 'Crimes per State in 2016 2017 2018':
    st.subheader('Crimes per State in the years 2016, 2017, 2018')
    Crimes_Per_State_in_2016_2017_2018 = helper.Crimes_Per_State_in_2016_2017_2018(cyber_C)
    st.table(Crimes_Per_State_in_2016_2017_2018)
    
    # A Bar Graph Displaying Crimes per State in 2016 2017 2018
    st.subheader('A Bar Graph Displaying Crimes per State in 2016 2017 2018')
    fig =px.bar(cyber_C.groupby(['State/UT'])[['2016', '2017', '2018']].sum(), color=cyber_C['State/UT'])
    st.plotly_chart(fig)

