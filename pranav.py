import streamlit as st
import pandas as pd

# Load the data
@st.cache
def load_data():
    # Replace 'path_to_your_file.csv' with the path to your dataset
    df = pd.read_csv('countries.csv')
    return df

# Display the app header
st.title('World Country Information')

# Load and display the data
data = load_data()
st.write('Available Countries:', data['Country'].tolist())

# Allow the user to select a country
selected_country = st.selectbox('Select a country', data['Country'])

# Display information about the selected country
if selected_country:
    country_info = data[data['Country'] == selected_country].iloc[0]
    st.subheader(selected_country)
    st.write(f"**Capital:** {country_info['Capital']}")
    st.write(f"**Population:** {country_info['Population']:,}")
    st.write(f"**Area (sq km):** {country_info['Area']:,}")

