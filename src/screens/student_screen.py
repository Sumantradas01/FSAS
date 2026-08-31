import streamlit as st

from src.ui.base_layout import style_background_dashboard, style_base_layout

from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import (
    get_all_students, create_student, get_student_subjects, get_student_attendance,
    unenroll_student_to_subject, student_login, check_student_username_exists,get_all_subjects,
    enroll_student_to_subject
)
import time

from src.components.dialog_enroll import enroll_dialog
from src.components.dialog_add_credentials import add_credentials_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""Welcome, {student_data['name']} """)
        if st.button("Logout", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['is_logged_in'] = False
            del st.session_state.student_data
            st.rerun()

    if not student_data.get('username'):
        with st.container(border=True):
            c1, c2 = st.columns([3, 1], vertical_alignment='center')
            with c1:
                st.write('🔐 Youre currently signed in with FaceID only. Add a username & password for quicker login.')
            with c2:
                if st.button('Add Credentials', type='primary', width='stretch'):
                    add_credentials_dialog()

    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.header('Your Enrolled Subjects')
    with c2:
        if st.button('Enroll in Subject', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    with st.spinner('Loading your enrolled subjects..'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)
        all_subjects = get_all_subjects()

        stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]['total'] += 1

        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    cols = st.columns(2)

    for i, sub_node in enumerate(subjects):
        sub = sub_node['subjects']
        sid = sub['subject_id']

        stats = stats_map.get(
            sid,
            {"total": 0, "attended": 0}
        )

        def unenroll_button(sid=sid, subject_name=sub['name'], index=i):
            if st.button(
                "Unenroll from this course",
                type='tertiary',
                width='stretch',
                icon=':material/delete_forever:',
                key=f"unenroll_{student_id}_{index}"
            ):
                unenroll_student_to_subject(student_id, sid)

                st.toast(
                    f"Unenrolled from {subject_name} successfully!"
                )

                st.rerun()

        with cols[i % 2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📅', 'Total', stats['total']),
                    ('✅', 'Attended', stats['attended']),
                ],
                footer_callback=unenroll_button
            )

    st.space()
    c1, c2 = st.columns(2)
    with c1:
        st.header('Available Courses')
    with c2:
        if st.button('Enroll via Code', type='primary', width='stretch'):
            enroll_dialog()

    st.divider()

    enrolled_ids = {sub_node['subjects']['subject_id'] for sub_node in subjects}
    available_subjects = [s for s in all_subjects if s['subject_id'] not in enrolled_ids]

    if not available_subjects:
        st.info('No new courses available to enroll in right now.')
    else:
        avail_cols = st.columns(2)
        for i, sub in enumerate(available_subjects):
            def enroll_button(sid=sub['subject_id'], subject_name=sub['name'], index=i):
                if st.button(
                    "Enroll Now",
                    type='primary',
                    width='stretch',
                    icon=':material/add_circle:',
                    key=f"enroll_avail_{student_id}_{index}"
                ):
                    enroll_student_to_subject(student_id, sid)
                    st.toast(f"Enrolled in {subject_name} successfully!")
                    st.rerun()

            with avail_cols[i % 2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=[('🫂', 'Students', sub['total_students'])],
                    footer_callback=enroll_button
                )

    footer_dashboard()


def student_screen_password_login():
    st.header('Login using Username & Password', text_alignment='center')
    st.space()

    username = st.text_input("Username", placeholder='e.g. akash123')
    password = st.text_input("Password", type='password', placeholder='Enter your password')

    if st.button('Login', type='primary', icon=':material/passkey:', shortcut='control+enter', width='stretch'):
        if not username or not password:
            st.warning('Please enter both username and password')
        else:
            student = student_login(username, password)
            if student:
                st.session_state.is_logged_in = True
                st.session_state.user_role = 'student'
                st.session_state.student_data = student
                st.toast(f"Welcome Back {student['name']}", icon="👋")
                time.sleep(1)
                st.rerun()
            else:
                st.error('Invalid username or password')


def student_screen_face_login():
    st.header('Login using FaceID', text_alignment='center')
    st.space()
    st.space()

    show_registration = False
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner('AI is scanning..'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('Face not found!')
            elif num_faces > 1:
                st.warning('Multiple faces found')
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s['student_id'] == student_id), None)

                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.toast(f'Welcome Back {student['name']}')
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info('Face not recognized! You might be a new student!')
                    show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header('Register new Profile')
            new_name = st.text_input("Enter your name", placeholder='E.g. Hamza Rizvi')

            st.subheader('Optional : Voice Enrollment')
            st.info("Enroll your for voice only attendance")

            audio_data = None

            try:
                audio_data = st.audio_input('Record a short phrase like I am present, My name is Akash.')
            except Exception:
                st.error('Audio Data failed!')

            st.subheader('Optional : Username & Password')
            st.info("Set these up now so you can log in later without using FaceID")

            reg_username = st.text_input("Choose a username", placeholder='e.g. akash123', key='reg_username')
            reg_password = st.text_input("Choose a password", type='password', key='reg_password')
            reg_password_confirm = st.text_input("Confirm password", type='password', key='reg_password_confirm')

            if st.button('Create Account', type='primary'):
                if new_name:
                    reg_username_clean = reg_username.strip() if reg_username else None
                    if reg_username_clean or reg_password:
                        if not reg_username_clean or not reg_password:
                            st.warning('Please fill both username and password, or leave both blank')
                            return
                        if reg_password != reg_password_confirm:
                            st.warning("Passwords don't match")
                            return
                        if check_student_username_exists(reg_username_clean):
                            st.error('Username already taken')
                            return

                    with st.spinner('Creating profile..'):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()

                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(
                                new_name,
                                face_embedding=face_emb,
                                voice_embedding=voice_emb,
                                username=reg_username_clean,
                                password=reg_password if reg_username_clean else None
                            )

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.toast(f'Profile Created! Hi {new_name}!')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Couldnt capture your facial features for registration')
                else:
                    st.warning('Please enter your name!')


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xxlarge')
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None
            st.rerun()

    if 'student_login_type' not in st.session_state:
        st.session_state.student_login_type = 'face'

    tab1, tab2 = st.columns(2)
    with tab1:
        type1 = "primary" if st.session_state.student_login_type == 'face' else "tertiary"
        if st.button('Login with FaceID', type=type1, width='stretch', icon=':material/face:'):
            st.session_state.student_login_type = 'face'
            st.rerun()
    with tab2:
        type2 = "primary" if st.session_state.student_login_type == 'password' else "tertiary"
        if st.button('Login with Username & Password', type=type2, width='stretch', icon=':material/password:'):
            st.session_state.student_login_type = 'password'
            st.rerun()

    st.divider()

    if st.session_state.student_login_type == 'face':
        student_screen_face_login()
    else:
        student_screen_password_login()

    footer_dashboard()