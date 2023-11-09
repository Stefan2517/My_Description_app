import streamlit as st

st.header("Contact us")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    print(button) # initial e False
    if button:
        print(button) # dupa apasare e True
        print("I was pressed!")
