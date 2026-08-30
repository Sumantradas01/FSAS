import streamlit as st


def footer_home():
    st.markdown(f"""
        <div style="margin-top:3rem; display:flex; gap:6px; justify-content:center; align-items:center;">
        <p style="font-weight:500; color:rgba(255,255,255,0.75); font-family:'Outfit', sans-serif; font-size:0.85rem;"> Created with ❤️ by Sumantra</p>  
        </div>
                
                """, unsafe_allow_html=True)
    ##logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by Sumantra</p>  
        </div>
                
                """, unsafe_allow_html=True)
