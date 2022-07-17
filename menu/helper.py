#Help page info will come here
import streamlit as st

def helppage():
    #Create the title and intro
    st.title("Need Help?")
    st.write("**Welcome** viewer, Not sure what to do or where to be? We have the support you need.")
    
    #Create the first help section. 
    st.title("Recommender System")
    
    #Add the recoomend video.
    r_vid = open('./resources/imgs/Recommend.mp4', 'rb')
    r_play = r_vid.read()

    st.video(r_play)
    
    #create the Step by step guide.
    st.write("*1. Choose Between Content based or Collaborative based filtering.")
    st.info("Content based is where we see what a user may like based on keywords/movies.")
    st.info("Collaborative based filtering is where we see what a user may like based on other users likes.")
    st.write("*2. Select 1st, 2nd & 3rd favourite movie.")
    st.write("*3. Press the Recommend button.")
    st.write("*4. Enjoy the selection of recommended films and their trailers.")
    
    
