# visuals will come here
import streamlit as st

def visuals():
    
    st.title("Explore the Statistics")
    st.write("**Welcome** viewer, here you can find some interesting stats about our progress.")
    st.markdown("")
    st.write("Due to the popularity of movies since 1974 we can definitely agree that there has been a influx of movies per annum.")
    st.image('./resources/imgs/newplot2.png')
    st.markdown("")
    st.write("Below you can find the most popular genres rated for #appname") 
    st.image('./resources/imgs/newplot3.png')
    st.markdown("")
    st.write("")
    st.image('./resources/imgs/newplot4.png')
    st.markdown("")
    st.write("")
    st.image('./resources/imgs/newplot5.png')
    
 # TODO: this should probably display visuals without returning anything