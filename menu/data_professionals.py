# streamlit dependencies
import streamlit as st
# data dependencies
import pandas as pd
import numpy as np
import base64
from PIL import Image

def data_professionals():
    st.info('Explained, Gathered, Analyzed & Unsupervised by The Dream Team')

    contact_form = """
    <form action="https://formsubmit.co/nyamathulani@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send mail</button>
    </form>
    """
    
    # define Github links for each team member
    link1 = "https://github.com/ThulaniNyama"
    link2 = "https://github.com/alnaschutte"
    link3 = "https://github.com/SiyandaMadlopha"
    link4 = "https://github.com/Shoki2"
    link5 = "https://github.com/ElelwaniTshikovhi"
    link6 = "https://github.com/SoulR95"
    # dream_team = Image.open('./resources/imgs/dream_works.gif')
    dream_works = open('./resources/imgs/dream_works.gif', 'rb')
    dream_team = dream_works.read()
    data_url = base64.b64encode(dream_team).decode("utf-8")
    dream_works.close()
    
    # define Pandas data frame with team members that developed the models, and the app
    df = pd.DataFrame(
        {
            "The Dream Team": [
                f'<a target="_blank" href="{link1}">Thulani Nyama</a>',
                f'<a target="_blank" href="{link2}">Alna Scutte</a>',
                f'<a target="_blank" href="{link3}">Siyanda Mandlopha</a>',
                f'<a target="_blank" href="{link4}">Reshoketswe Makgamatha</a>',
                f'<a target="_blank" href="{link5}">Elelwani Tshikovhi</a>',
                f'<a target="_blank" href="{link6}">Riaan James-Verwey</a>'
            ],
            "Profession": ["Data Scientist", "Data Analyst", "Data Scientist", "Data Analyst", "Data Scientist", "Data Engineer"]
        }
        
    )
    
    team, members, contact, = st.columns([2, 1.5, 1.5])

    with contact:
        st.header(":mailbox: Get in touch with us!")
        st.markdown(contact_form, unsafe_allow_html=True)
        local_css("./utils/style.css")
    with team:
        st.write("")
        st.write("")
        st.write("")
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    with members:
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="Dream Team">',unsafe_allow_html=True)
        
    st.write("")
    with st.expander("We are based at"):
        address, dream_map = st.columns([2, 3.5])
        with address:
            st.write('<style>div.st-bf{flex-direction:column;padding-top:12px;} div.st-ag{font-size:24px;font-weight:bold;text-align:center;}</style>', unsafe_allow_html=True)
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown("2ⁿᵈ floor")
            st.markdown("420 Milton Street")
            st.markdown("Marshaltown")
            st.markdown("Johannesburg 2000")
            st.markdown("Tel no: 011 668 4397(moviexp)")
        with dream_map:
            df = pd.DataFrame(
            np.random.randn(1, 2) / [50, 50] + [-26.204103, 28.047305],
            columns=['lat', 'lon'])
            st.map(df)
    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style >{f.read()}</style>", unsafe_allow_html=True)