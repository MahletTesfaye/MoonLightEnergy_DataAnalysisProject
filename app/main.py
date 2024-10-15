import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('../data/benin-malanville.csv')

# Convert the 'Timestamp' column to datetime
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

st.title("Solar Energy Data Dashboard")

# Sidebar filters
ghi_range = st.sidebar.slider('Select GHI range', float(df['GHI'].min()), float(df['GHI'].max()), (100.0, 800.0))

# Filtered Data
filtered_data = df[(df['GHI'] >= ghi_range[0]) & (df['GHI'] <= ghi_range[1])]

# GHI over time
st.subheader("GHI Over Time")

# Plot line chart with time on the x-axis and GHI on the y-axis
st.line_chart(data=filtered_data.set_index('Timestamp')['GHI'])

# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr = filtered_data.corr()

# Display the correlation heatmap using matplotlib and seaborn
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
