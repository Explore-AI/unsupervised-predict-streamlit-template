#Help page info will come here
import streamlit as st

def helppage():
    #Create the title and intro
    st.title("Need Help?")
    st.write("**Welcome** Xplorer, Not sure what to do or where to be? We have the support you need.")
    
    with st.expander("Home"):
            
    
    #Create the help section for home page. 
        st.title("Home")
    
    #Add the recoomend video.
        st.video('https://youtu.be/hebG9vo5D0E')
            
    
    #create the Step by step guide for the Home page.
        st.title("Steps")
        st.write("- Choose Between Content based or Collaborative based filtering.")
        
        st.info(
            """
        - Content based is where we see what a user may like based on keywords/movies.
        
        - Collaborative based filtering is where we see what a user may like based on other users likes.
        
        """
        )
        
        st.write(
            """
        - Select 1st, 2nd & 3rd favourite movie.
        - Press the Recommend button.
        - Enjoy the selection of recommended films and their trailers.
        """
                )
    
    #create the About help section.
    with st.expander("About"):
        st.title("About")
    
    #Add About help video
    #st.video(a_play)
    
    #create the Step by step guide for the About Page.
        st.write("")
    
    #create help section for trailers page.    
    with st.expander("Trailers"):
        st.title("Trailers")
        
    #Add trailer help video.    
        st.video('https://youtu.be/AYgxUezGG1A')
    
    #create the Step by step guide for the Trailers Page.
        st.title("Steps")
        st.write(
            """ 
            -  Move the slider to select years.
            -  Choose which years drop down to select and click it.
            -  Play the vid.
            -  Feel free to read the comments or leave a comment.
            -  To leave comment type name in the name box.
            -  Leave your comment in comment section.
            -  Press the share comment button to upload your comment.
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
    #st.video(a_play)
    
    #create the Step by step guide for the Contact Us Page.
        st.title("Steps")
        st.write(
            """
            As you can see Contact Us is pretty simple, but should you require any assistance feel free to reach out.
            
            - Add your name.
            - Add your email.
            - Leave your message or any concerns.
            - Or if you feel like reaching out telephonically use the drop down.
            - To find where we are based use the drop down as well.
            - Trends Analytics strife to make the world a better place data at a time.
        
            """
                )
    
        
    
    
