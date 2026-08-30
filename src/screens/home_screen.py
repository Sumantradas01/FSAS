import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():

    style_background_home()
    style_base_layout()
    header_home()

    st.markdown(
        """
        <div class="hero-badge">
            <span>✨ AI-Powered Attendance, Zero Hassle</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown(
            """
            <div class="portal-icon">🎓</div>
            <h2 style="color:#0a0a0a;">I'm a Student</h2>
            <p class="portal-sub">Scan your face, mark attendance, and track your classes — no passwords needed.</p>
            """,
            unsafe_allow_html=True
        )
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown(
            """
            <div class="portal-icon">🧑‍🏫</div>
            <h2 style="color:#0a0a0a;">I'm a Teacher</h2>
            <p class="portal-sub">Run instant AI face & voice attendance for your whole classroom in seconds.</p>
            """,
            unsafe_allow_html=True
        )
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', width='stretch'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()