# streamlit dependencies
import streamlit as st
# data dependencies
import pandas as pd
from PIL import Image

def data_professionals():
    st.info('Explained, Gathered, Analyzed & Unsupervised by The Dream Team')

    # define Github links for each team member
    link1 = "https://github.com/ThulaniNyama"
    link2 = "https://github.com/alnaschutte"
    link3 = "https://github.com/SiyandaMadlopha"
    link4 = "https://github.com/Shoki2"
    link5 = "https://github.com/ElelwaniTshikovhi"
    link6 = "https://github.com/SoulR95"
    dream_team = Image.open('./resources/imgs/DreamTeam.png')
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
            "Profession": ["Data Scientist", "Data Analyst", "Data Engineer", "Data Scientist", "Data Scientist", "Data Engineer"]
        }
        
    )
    
    members, team, = st.columns(2)

    with members:
        st.write("")
        st.write("")
        st.write(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    with team:
        st.write("")
        st.image(dream_team, caption='')
    st.write("")
    # footer display image with caption 
    image = Image.open('./resources/imgs/EDSA_logo.png')
    st.image(image, caption='© The Dream Team', use_column_width=True)