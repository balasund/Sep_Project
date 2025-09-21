
import streamlit as st

st.title("Checkbox Example")

checked = st.checkbox("Check me")



if checked:

    st.write("Checkbox is selected!")

else:

    st.write("Checkbox is not selected.")