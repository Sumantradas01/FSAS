import streamlit as st
import time
from src.database.db import check_student_username_exists, update_student_credentials


@st.dialog("Add Login Credentials")
def add_credentials_dialog():
    student_id = st.session_state.student_data['student_id']

    st.write('Set a username and password so you can log in without FaceID next time.')

    username = st.text_input('Choose a username', placeholder='e.g. akash123')
    password = st.text_input('Choose a password', type='password')
    password_confirm = st.text_input('Confirm password', type='password')

    if st.button('Save Credentials', type='primary', width='stretch'):
        if not username or not password:
            st.warning('Please fill all fields')
            return
        if password != password_confirm:
            st.warning("Passwords don't match")
            return
        if check_student_username_exists(username):
            st.error('Username already taken')
            return

        update_student_credentials(student_id, username, password)
        st.session_state.student_data['username'] = username
        st.success('Credentials saved!')
        time.sleep(1)
        st.rerun()