import streamlit as st
from send_email import send_emailll

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: Email nou de la: {user_email}

From: {user_email}
{raw_message}
"""

    button = st.form_submit_button("Submit")
 #   print(button) # initial e False
    if button:
        send_emailll(message)
        st.info("Your email was sent succesfully")
#        print(button) # dupa apasare e True
#       print("I was pressed!")
