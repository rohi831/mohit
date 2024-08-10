import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
@st.cache
def load_data():
    # Replace 'path_to_your_file.csv' with the path to your dataset
    df = pd.read_csv('oxygen_levels.csv', parse_dates=['timestamp'])
    return df

# Display the app header
st.title('Oxygen Level Monitoring')

# Load and display the data
data = load_data()
st.write('Oxygen Level Data:', data.head())

# Show a line plot of the oxygen levels over time
st.subheader('Oxygen Level Over Time')
fig, ax = plt.subplots()
ax.plot(data['timestamp'], data['oxygen_level'], marker='o', linestyle='-', color='b')
ax.set_xlabel('Timestamp')
ax.set_ylabel('Oxygen Level (%)')
ax.set_title('Oxygen Level Trends')
plt.xticks(rotation=45)
st.pyplot(fig)

# Show basic statistics
st.subheader('Basic Statistics')
st.write(f"**Maximum Oxygen Level:** {data['oxygen_level'].max()}%")
st.write(f"**Minimum Oxygen Level:** {data['oxygen_level'].min()}%")
st.write(f"**Average Oxygen Level:** {data['oxygen_level'].mean():.2f}%")

# Optionally, allow users to filter data by date range
st.subheader('Filter Data by Date Range')
start_date = st.date_input('Start Date', data['timestamp'].min().date())
end_date = st.date_input('End Date', data['timestamp'].max().date())

if start_date and end_date:
    filtered_data = data[(data['timestamp'].dt.date >= start_date) & (data['timestamp'].dt.date <= end_date)]
    st.write(f"Filtered Data from {start_date} to {end_date}:")
    st.write(filtered_data)
    if not filtered_data.empty:
        fig, ax = plt.subplots()
        ax.plot(filtered_data['timestamp'], filtered_data['oxygen_level'], marker='o', linestyle='-', color='g')
        ax.set_xlabel('Timestamp')
        ax.set_ylabel('Oxygen Level (%)')
        ax.set_title('Filtered Oxygen Level Trends')
        plt.xticks(rotation=45)
        st.pyplot(fig)
