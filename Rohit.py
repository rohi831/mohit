import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the data
@st.cache
def load_data():
    # Replace 'path_to_your_file.csv' with the path to your dataset
    df = pd.read_csv('path_to_your_file.csv')
    return df

# Display the app header
st.title('Property Sales Analysis')

# Load and display the data
data = load_data()
st.write('Data Preview:', data.head())

# Display a summary of the data
if st.checkbox('Show Data Summary'):
    st.write(data.describe())

# Allow the user to select features for analysis
features = st.multiselect(
    'Select features to include in the model:',
    options=data.columns.tolist(),
    default=['square_footage', 'num_bedrooms', 'num_bathrooms']
)

if features:
    # Prepare the data
    X = data[features]
    y = data['price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a model
    model = RandomForestRegressor()
    model.fit(X_train, y_train)

    # Make predictions
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    st.write(f'Mean Squared Error: {mse:.2f}')

    # Allow user input for prediction
    st.subheader('Predict Property Price')
    inputs = {feature: st.number_input(f'{feature}', value=0) for feature in features}
    if st.button('Predict'):
        input_data = pd.DataFrame([inputs])
        price_prediction = model.predict(input_data)[0]
        st.write(f'Predicted Property Price: ${price_prediction:,.2f}')

