import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: radial-gradient(circle at 15% 20%, #6c5ce7 0%, #5865F2 45%, #4752c4 100%) !important;
                    background-attachment: fixed !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background: rgba(255, 255, 255, 0.88) !important;
                    backdrop-filter: blur(16px) !important;
                    -webkit-backdrop-filter: blur(16px) !important;
                    padding: 2.5rem !important;
                    border-radius: 2rem !important;
                    border: 1px solid rgba(255, 255, 255, 0.4) !important;
                    box-shadow: 0 20px 45px rgba(20, 20, 60, 0.25) !important;
                    transition: transform 0.3s ease, box-shadow 0.3s ease !important;
                }

                .stApp div[data-testid="stColumn"]:hover {
                    transform: translateY(-6px) !important;
                    box-shadow: 0 28px 55px rgba(20, 20, 60, 0.32) !important;
                }

                .hero-badge {
                    display: flex;
                    justify-content: center;
                    margin: 0 0 2rem 0;
                }

                .hero-badge span {
                    background: rgba(255, 255, 255, 0.15);
                    border: 1px solid rgba(255, 255, 255, 0.35);
                    color: white;
                    padding: 8px 20px;
                    border-radius: 999px;
                    font-family: 'Outfit', sans-serif;
                    font-size: 0.9rem;
                    font-weight: 600;
                    backdrop-filter: blur(6px);
                }

                .portal-icon {
                    font-size: 2.5rem;
                    margin-bottom: 0.25rem;
                }

                .portal-sub {
                    color: #64748b;
                    font-size: 0.95rem;
                    line-height: 1.4;
                    margin-bottom: 1rem;
                }
        </style>  

                """
            ,unsafe_allow_html=True)

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)