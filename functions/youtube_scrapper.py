import urllib.request
import requests
import unicodedata
import re
from streamlit_player import st_player
# import os
# import streamlit as st
# import googleapiclient.discovery

def youtubeScrapper(top_10):
    search_string = unicodedata.normalize('NFKD', top_10).encode('ascii', 'ignore').decode()
    youtube_str = re.sub("[ ]", "+", search_string)
    html = urllib.request.urlopen('https://www.youtube.com/results?search_query=' + youtube_str + '+trailer')
    vid_id = re.findall(r'watch\?v=(\S{11})', html.read().decode())
    
    # Below we verify that the video contains nudity or not
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
    # api_service_name = "youtube"
    # api_version = "v3"
    # youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = 'AIzaSyCLfeDKMIRoTZ9JsDGALP3gbNnTb-3DLTQ')
    # request = youtube.videos().getRating(id=str(vid_id[0]))
    # response = request.execute()
    # st.write(str(response))
    
    trailer_res = 'https://www.youtube.com/watch?v=' + vid_id[0]
    st_player(trailer_res)