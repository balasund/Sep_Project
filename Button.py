
import streamlit as st

# Create a button

button_clicked = st.button("Click me!")



# Check if the button is clicked

if button_clicked:

    st.write("Button is clicked!")

else:

    st.write("Button is not clicked yet.")