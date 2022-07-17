#Help page info will come here
import streamlit as st

def helppage():
    st.title("Need Help?")
    st.write("**Welcome** viewer, Not sure what to do or where to be? We have the support you need.")
    st.title("Recommender System")
    
    r_vid = open('Recommend.mp4', 'rb')
    r_play = r_vid.read()

    st.video(r_play)
