import streamlit as st


def header_home():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:20px; margin-top:20px">
            <img src='{logo_url}' style='height:100px; filter: drop-shadow(0 8px 20px rgba(0,0,0,0.25));' />
            <h1 style='text-align:center; color:#E0E3FF; margin-top:0.5rem;'>SNAP<br/>CLASS</h1>
            <p style='color:rgba(255,255,255,0.8); font-family:"Outfit", sans-serif; font-size:1rem; margin-top:-0.3rem;'>Making Attendance Faster Using AI</p>
        </div>   
                
                """, unsafe_allow_html=True)



def header_dashboard():

    logo_url = "https://i.ibb.co/YTYGn5qV/logo.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>SNAP<br/>CLASS</h1>
        </div>   
                
                """, unsafe_allow_html=True)
