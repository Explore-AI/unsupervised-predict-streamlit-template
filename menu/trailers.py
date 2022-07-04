import streamlit as st
from streamlit_player import st_player
import streamlit as st
import functions.comments as coms

def vids():
    end_year, start_year = st.select_slider('Select Release Year Period',
                                            options=[ 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012],
                                            value=(2022, 2012))
    st.write('You selected movies released between', str(start_year), 'and', str(end_year))
    # Embed a youtube video
    if start_year <= 2022 & end_year == 2022:
        with st.expander("Top 10 Best Movies 2022"):
            st_player('https://youtu.be/ZTv5lBU6qQ0')
            # coms.commenter()
    if start_year <= 2021 & end_year == 2021:
        with st.expander("Top 10 Best Movies 2021"):
            # 2021
            st_player('https://youtu.be/QKN-YwYwI_I')
    if start_year <= 2020 & end_year == 2020:
        with st.expander("Top 10 Best Movies 2020"):
            # 2020
            st_player('https://youtu.be/rGfbhugP1NI')
    if start_year <= 2019 & end_year == 2019:
        with st.expander("Top 10 Best Movies 2019"):
            # 2019
            st_player('https://youtu.be/48NL3N6KMFo?t=9')
    if start_year <= 2018 & end_year == 2018:
        with st.expander("Top 10 Best Movies 2018"):
            # 2017
            st_player('https://youtu.be/smO82hO1BZ0?t=3')
    # elif start_year >= 2017:
        # with st.expander("Top 10 Best Movies 2017"):
        #     # 2016
        #     st_player('https://youtu.be/QKN-YwYwI_I')
    # elif start_year >= 2016:        
        # with st.expander("Top 10 Best Movies 2016"):
        #     # 2014
        #     st_player('https://youtu.be/QKN-YwYwI_I')
    # elif start_year >= 2015:        
        # with st.expander("Top 10 Best Movies 2015"):
        #     # 2014
        #     st_player('https://youtu.be/QKN-YwYwI_I')
    # elif start_year >= 2014:
        # with st.expander("Top 10 Best Movies 2014"):
        #     # 2013
        #     st_player('https://youtu.be/QKN-YwYwI_I')
    # elif start_year >= 2013:
        # with st.expander("Top 10 Best Movies 2013"):
        #     # 2012
        #     st_player('https://youtu.be/QKN-YwYwI_I')
    # elif start_year >= 2012:
        # with st.expander("Top 10 Best Movies 2013"):
        #     # 2012
        #     st_player('https://youtu.be/QKN-YwYwI_I')