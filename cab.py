import streamlit as st

# Set up the Streamlit app
st.title('Cab Booking App')

# Create a form for booking details
with st.form(key='booking_form'):
    st.header('Enter Booking Details')
    
    # Input fields
    name = st.text_input('Full Name')
    phone_number = st.text_input('Phone Number')
    pickup_location = st.text_input('Pickup Location')
    dropoff_location = st.text_input('Drop-off Location')
    pickup_time = st.time_input('Pickup Time', value=pd.Timestamp.now().time())
    date = st.date_input('Date of Pickup', value=pd.Timestamp.now().date())

    # Create a submit button
    submit_button = st.form_submit_button('Book Cab')
    
# Process the booking when the button is pressed
if submit_button:
    if name and phone_number and pickup_location and dropoff_location:
        # In a real application, you would send this data to a backend service
        st.success(f'Cab booked successfully!\n\n'
                   f'**Name:** {name}\n'
                   f'**Phone Number:** {phone_number}\n'
                   f'**Pickup Location:** {pickup_location}\n'
                   f'**Drop-off Location:** {dropoff_location}\n'
                   f'**Pickup Time:** {pickup_time}\n'
                   f'**Date:** {date}')
    else:
        st.error('Please fill in all the required fields.')
