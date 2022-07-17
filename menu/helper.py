#Help page info will come here
import streamlit as st

def helppage():
    st.title("Need Help?")
    st.write("**Welcome** viewer, Not sure what to do or where to be? We have the support you need.")
    st.title("Recommender System")
<<<<<<< Updated upstream
<<<<<<< Updated upstream
    st.image('./resources/imgs/Rtest1.gif')
=======
    Recommend = open('././resources/imgs/Recommend.mp4', 'rb')
    R_play = Recommend.read()

    st.video(R_play)
    
    
>>>>>>> Stashed changes
=======
    
    Recommend = open('Recommend.mp4', 'rb')
    r_read = Recommend.read()

    st.video(r_read)
    
>>>>>>> Stashed changes
