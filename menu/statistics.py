# visuals will come here
import streamlit as st
import base64

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
    choose=st.radio("",("Bar Chart","Line Chart","Pie Chart"))
    
    
    
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