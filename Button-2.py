
import streamlit as st
import pandas as pd

# Create a button

button_clicked = st.button("Click me!")


# Check if the button is clicked

if button_clicked:
    df = pd.read_excel("output1.xlsx")
    st.write(df)
    st.write("Button is clicked!")
    

else:

    st.write("Button is not clicked yet.")