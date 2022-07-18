#Help page info will come here
import streamlit as st

def helppage():
    #Create the title and intro
    st.title("Need Help?")
    st.write("**Welcome** viewer, Not sure what to do or where to be? We have the support you need.")
    
    with st.expander("Home"):
            
    
    #Create the help section for home page. 
        st.title("Home")
    
    #Add the recoomend video.
        r_vid = open('./resources/vids/Recommend.mp4', 'rb')
        r_play = r_vid.read()

        st.video(r_play)
            
    
    #create the Step by step guide for the Home page.
        st.write("1. Choose Between Content based or Collaborative based filtering.")
        
        st.info(
            """
        - Content based is where we see what a user may like based on keywords/movies.
        
        - Collaborative based filtering is where we see what a user may like based on other users likes.
        
        """
        )
        
        st.write(
            """
        2. Select 1st, 2nd & 3rd favourite movie.
        3. Press the Recommend button.
        4. Enjoy the selection of recommended films and their trailers.
        """
                )
    
    #create the About help section.
    with st.expander("About"):
        st.title("About")
    
    #Add About help video
    #a_vid = open('./resources/vids/.mp4', 'rb')
    #a_play = a_vid.read()
    #st.video(a_play)
    
    #create the Step by step guide for the About Page.
        st.write("")
    
    #create help section for trailers page.    
    with st.expander("Trailers"):
        st.title("Trailers")
        
    #Add trailer help video.    
        t_vid = open('./resources/vids/trailers.mp4', 'rb')
        t_play = t_vid.read()
        st.video(t_play)
    
    #create the Step by step guide for the Trailers Page.
        st.write(
            """ 
            - 1. Move the slider to select years.
            - 2. Choose which years drop down to select and click it.
            - 3. Play the vid.
            - 4. Feel free to read the comments or leave a comment.
            - 5. To leave comment type name in the name box.
            - 6. Leave your comment in comment section.
            - 7. Press the share comment button to upload your comment.
            """
                )
        
    #create the About help section.
    with st.expander("Statistics"):
        st.title("Statistics")
    
    #Add Stats help video
    #s_vid = open('./resources/vids/.mp4', 'rb')
    #s_play = s_vid.read()
    #st.video(s_play)
    
    #create the Step by step guide for the About Page.
        st.write("")
        
    #create the Contact Us help section.
    with st.expander("Contact Us"):
        st.title("Contact Us")
    
    #Add Contact help video
    #a_vid = open('./resources/vids/.mp4', 'rb')
    #a_play = a_vid.read()
    #st.video(a_play)
    
    #create the Step by step guide for the Contact Us Page.
        st.write("")
    
        
    
    
