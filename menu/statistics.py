# visuals will come here
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
from streamlit_tags import st_tags
import base64
movies = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/movies.csv')

@st.cache(allow_output_mutation=True)

def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        body {
        background-image: url("data:image/gif;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

def visuals():
    
    set_png_as_page_bg('./resources/imgs/stats.gif')
    
    st.title("Xplore the Statistics")
    st.write("**Hi there**, you can explore some interesting stats about the movies.")

    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;} </style>', unsafe_allow_html=True)
    st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
    chart = st.radio("",("Bar Chart","Line Chart","Pie Chart"))
    
    if chart == "Bar Chart":
            with st.expander("Bar Chart"):
                options = st.multiselect('Select data', ['titles', 'genres'])
                st.write(options)
                
    elif chart == "Line Chart":
            with st.expander("Line Chart"):
                options = st.multiselect('Select data', ['Movies', 'Years'])
                st.write("Line")
    elif chart == "Pie Chart":
            with st.expander("Pie Chart"):
                options = st.multiselect('Select data', ['Movies', 'Genres', 'Ratings', 'Years'])
                st.write("Pie")
#     st.write("Due to the popularity of movies since 1974 we can definitely agree that there has been a influx of movies per annum.")
#     # st.image('./resources/imgs/stats.gif')
#     st.image('./resources/imgs/newplot2.png')
#     st.markdown("")
#     st.write("Below you can find the most popular genres rated for #appname") 
#     st.image('./resources/imgs/newplot3.png')
#     st.markdown("")
#     st.write("")
#     st.image('./resources/imgs/newplot4.png')
#     st.markdown("")
#     st.write("")
#     st.image('./resources/imgs/newplot5.png')
 # TODO: this should probably display visuals without returning anything