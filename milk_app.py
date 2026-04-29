import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Milk Production Dashboard", layout="wide")

st.markdown("<h1 style='text-align: center;'>🥛 Milk Production Dashboard</h1>", unsafe_allow_html=True)

# -----------------------------
# Load Data
# -----------------------------
df = pd.read_csv("cleaned_milk_production.csv")
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Filters")

year = st.sidebar.selectbox("Select Year", sorted(df['Year'].unique()))

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['Date'].min(), df['Date'].max()]
)

filtered_df = df[
    (df['Year'] == year) &
    (df['Date'] >= pd.to_datetime(date_range[0])) &
    (df['Date'] <= pd.to_datetime(date_range[1]))
]

# -----------------------------
# KPI Cards
# -----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Production", f"{filtered_df['Milk_Production'].sum():,.0f}")
col2.metric("Average Production", f"{filtered_df['Milk_Production'].mean():,.0f}")
col3.metric("Max Production", f"{filtered_df['Milk_Production'].max():,.0f}")

# -----------------------------
# Trend Chart (Plotly)
# -----------------------------
st.subheader("📈 Production Trend")

fig1 = px.line(df, x='Date', y='Milk_Production', title="Milk Production Over Time")
st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# Year-wise Production
# -----------------------------
st.subheader("📅 Year-wise Production")

yearly = df.groupby('Year')['Milk_Production'].sum().reset_index()
fig2 = px.bar(yearly, x='Year', y='Milk_Production', title="Year-wise Production")
st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# Monthly Seasonality
# -----------------------------
st.subheader("📊 Monthly Seasonality")

monthly = df.groupby('Month')['Milk_Production'].mean().reset_index()
fig3 = px.bar(monthly, x='Month', y='Milk_Production', title="Monthly Average Production")
st.plotly_chart(fig3, use_container_width=True)

# -----------------------------
# Heatmap
# -----------------------------
st.subheader("🔥 Heatmap (Year vs Month)")

pivot = df.pivot_table(values='Milk_Production', index='Year', columns='Month')

fig4 = px.imshow(pivot, title="Production Heatmap")
st.plotly_chart(fig4, use_container_width=True)

# -----------------------------
# Year Comparison
# -----------------------------
st.subheader("⚖️ Year Comparison")

year1 = st.selectbox("Select Year 1", df['Year'].unique(), key="y1")
year2 = st.selectbox("Select Year 2", df['Year'].unique(), key="y2")

df1 = df[df['Year'] == year1]
df2 = df[df['Year'] == year2]

fig5 = px.line()
fig5.add_scatter(x=df1['Month'], y=df1['Milk_Production'], mode='lines', name=str(year1))
fig5.add_scatter(x=df2['Month'], y=df2['Milk_Production'], mode='lines', name=str(year2))

st.plotly_chart(fig5, use_container_width=True)

# -----------------------------
# Forecasting (Linear Regression)
# -----------------------------
st.subheader("🔮 Milk Production Forecast")

df['Time'] = np.arange(len(df))

X = df[['Time']]
y = df['Milk_Production']

model = LinearRegression()
model.fit(X, y)

future_days = 24
future_time = np.arange(len(df), len(df) + future_days).reshape(-1, 1)
predictions = model.predict(future_time)

future_dates = pd.date_range(df['Date'].iloc[-1], periods=future_days, freq='M')

forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Milk_Production': predictions
})

fig6 = px.line()
fig6.add_scatter(x=df['Date'], y=y, mode='lines', name='Actual')
fig6.add_scatter(x=forecast_df['Date'], y=forecast_df['Milk_Production'],
                 mode='lines', name='Forecast')

st.plotly_chart(fig6, use_container_width=True)

# -----------------------------
# Download Button
# -----------------------------
st.subheader("📥 Download Data")

st.download_button(
    label="Download Clean Data",
    data=df.to_csv(index=False),
    file_name='milk_production_cleaned.csv',
    mime='text/csv'
)