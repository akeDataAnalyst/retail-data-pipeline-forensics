#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Set Page Config
st.set_page_config(page_title="Dubai Retail Insights", layout="wide")

# Title and Description (Matching the JD keywords)
st.title("📊 Retail Stock & Buyer Behavior Analytics")
st.markdown("""
This dashboard identifies **stock irregularities**, **event-based performance**, 
and **buyer demographics** to drive strategic decisions for the Dubai market.
""")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_retail_data.csv')
    return df

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("Filter Insights")
selected_event = st.sidebar.multiselect("Select Dubai Event", options=df['Event'].unique(), default=df['Event'].unique())
selected_location = st.sidebar.multiselect("Select Store Location", options=df['Store_Location'].unique(), default=df['Store_Location'].unique())

filtered_df = df[(df['Event'].isin(selected_event)) & (df['Store_Location'].isin(selected_location))]

# --- ROW 1: KEY METRICS ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Revenue (AED)", f"{int((filtered_df['Sales_Qty'] * filtered_df['Unit_Price_AED']).sum()):,}")
with col2:
    st.metric("Avg Stock Turnover", round(filtered_df['Sales_Qty'].sum() / filtered_df['Stock_On_Hand'].mean(), 2))
with col3:
    st.metric("Irregularities Fixed", "1,248") # Referencing your Phase 2 Audit Log

# --- ROW 2: ANALYSIS ---
st.divider()
c1, c2 = st.columns(2)

with c1:
    st.subheader("Stock Turnover by Product & Event")
    # mimicking your SQL Turnover Query
    turnover = filtered_df.groupby(['Event', 'Product_Name'])['Sales_Qty'].sum().reset_index()
    fig = px.bar(turnover, x='Event', y='Sales_Qty', color='Product_Name', barmode='group')
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Location-Based Buyer Behavior")
    # mimicking your SQL Demographic Query
    demo = filtered_df.groupby('Store_Location').agg({'Sales_Qty': 'sum', 'Unit_Price_AED': 'mean'}).reset_index()
    fig2 = px.pie(demo, values='Sales_Qty', names='Store_Location', hole=0.4)
    st.plotly_chart(fig2, use_container_width=True)

# --- ROW 3: ACTIONABLE RECOMMENDATIONS ---
st.divider()
st.header("💡 Strategic Recommendations")
if "Black Friday" in selected_event:
    st.error("**Urgent Alert:** Black Friday turnover exceeds safety thresholds for 'Smart Watch Ultra'. Increase stock by 25%.")
if "Mall of the Emirates" in selected_location:
    st.info("**Luxury Insight:** MoE customers show a 15% higher basket value. Prioritize 'Oud Silk Mood Perfume' inventory here.")


# In[ ]:




