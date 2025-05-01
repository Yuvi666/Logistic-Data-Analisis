import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

# Set page config
st.set_page_config(page_title="📦 Logistics Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('logistics_shipments_5000.csv')
    df['pickup_date'] = pd.to_datetime(df['pickup_date'])
    df['delivery_date'] = pd.to_datetime(df['delivery_date'])
    df['delivery_days'] = (df['delivery_date'] - df['pickup_date']).dt.days
    return df

df = load_data()

# Sidebar
st.sidebar.title("📍 Filter Options")
origin = st.sidebar.selectbox("Origin City", ["All"] + sorted(df['origin_city'].unique()))
filtered_df = df if origin == "All" else df[df['origin_city'] == origin]

# Main Header
st.title("📦 Logistics Delivery Performance Dashboard")

# KPIs
total_shipments = len(filtered_df)
avg_days = filtered_df['delivery_days'].mean()
success_pct = (filtered_df['delivery_status'] == 'Delivered').mean() * 100
delay_pct = (filtered_df['delivery_status'] == 'Delayed').mean() * 100

st.markdown("### 🔢 Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("📦 Total Shipments", f"{total_shipments}")
kpi2.metric("⏱️ Avg Delivery Days", f"{avg_days:.2f}")
kpi3.metric("✅ Success Rate", f"{success_pct:.2f}%")
kpi4.metric("⚠️ Delay Rate", f"{delay_pct:.2f}%")

st.markdown("---")

# Delivery Status Pie Chart
st.subheader("📊 Delivery Status Distribution")
status_counts = filtered_df['delivery_status'].value_counts().reset_index()
status_counts.columns = ['delivery_status', 'count']  

fig_pie = px.pie(
    status_counts,
    names='delivery_status',
    values='count',
    color='delivery_status',
    color_discrete_map={
        "Delivered": "green",
        "Delayed": "orange",
        "Failed": "red"
    },
    hole=0.4
)
st.plotly_chart(fig_pie, use_container_width=True)

# Scatter Plots
st.subheader("📈 Cost Relationships")
scatter1, scatter2 = st.columns(2)

with scatter1:
    fig_weight = px.scatter(
        filtered_df,
        x='weight_kg',
        y='cost',
        color='delivery_status',
        title="Weight vs Cost",
        color_discrete_sequence=px.colors.qualitative.Set1
    )
    st.plotly_chart(fig_weight, use_container_width=True)

with scatter2:
    fig_dist = px.scatter(
        filtered_df,
        x='distance_km',
        y='cost',
        color='delivery_status',
        title="Distance vs Cost",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_dist, use_container_width=True)

# Heatmap
st.subheader("🌐 Average Delivery Time Heatmap (Origin → Destination)")
pivot = filtered_df.pivot_table(
    values='delivery_days',
    index='origin_city',
    columns='destination_city',
    aggfunc='mean'
)

fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(pivot, annot=True, cmap="YlGnBu", fmt=".1f", linewidths=0.5, cbar=True)
plt.title("Average Delivery Days Heatmap")
st.pyplot(fig)
