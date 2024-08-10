import streamlit as st

# Set up the Streamlit app
st.title('Simple Calculator')

# Create a form to get user input
with st.form(key='calculator_form'):
    # Define the inputs
    num1 = st.number_input('Enter first number', value=0.0)
    num2 = st.number_input('Enter second number', value=0.0)
    
    # Define the operations
    operation = st.selectbox('Select operation', options=['Add', 'Subtract', 'Multiply', 'Divide'])
    
    # Create a submit button
    submit_button = st.form_submit_button('Calculate')

# Perform the calculation when the button is pressed
if submit_button:
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = 'Error: Division by zero is not allowed'
    
    # Display the result
    st.write(f'The result of {operation} is: {result}')

