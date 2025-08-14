import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email_forms"):

    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message here")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: Email from {user_email}

From: {user_email}
{raw_message}
    """
    if button:
        send_email(message)
        st.info("Email sent successfully")