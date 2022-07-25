import urllib.request
import unicodedata
import re
from streamlit_player import st_player

def youtubeScrapper(top_10):
    search_string = unicodedata.normalize('NFKD', top_10).encode('ascii', 'ignore').decode()
    youtube_str = re.sub("[ ]", "+", search_string)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + youtube_str + "+trailer")
    vid_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    trailer_res = 'https://www.youtube.com/watch?v=' + vid_id[0]
    st_player(trailer_res)