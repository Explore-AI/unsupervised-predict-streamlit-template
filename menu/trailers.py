import streamlit as st
from streamlit_player import st_player
import streamlit as st
import functions.comments as coms

def vids():
    year = st.slider('Select Release Year Period', 2022, 2018, 2022)
    st.write('You selected movies released between', str(2018), 'and', str(year))
    # embed a youtube video
    if year == 2022:
        with st.expander('Top 10 Best Movies 2022'):
            st_player('https://youtu.be/ZTv5lBU6qQ0')
            st.write('**Which movies did you like?**')
            coms.commenter('Top 10 Best Movies 2022')
    if year >= 2021:
        with st.expander('Top 10 Best Movies 2021'):
            # 2021
            st.write('**Which movies did you like?**')
            st_player('https://youtu.be/QKN-YwYwI_I')
            coms.commenter('Top 10 Best Movies 2021')
    if year >= 2020:
        with st.expander('Top 10 Best Movies 2020'):
            # 2020
            st_player('https://youtu.be/rGfbhugP1NI')
            coms.commenter('Top 10 Best Movies 2020')
    if year >= 2019:
        with st.expander('Top 10 Best Movies 2019'):
            # 2019
            st_player('https://youtu.be/48NL3N6KMFo?t=9')
            coms.commenter('Top 10 Best Movies 2019')
    if year >= 2018:
        with st.expander('Top 10 Best Movies 2018'):
            # 2017
            st_player('https://youtu.be/FkUtWUy77fQ?t=9')
            coms.commenter('Top 10 Best Movies 2018')