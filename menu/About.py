import streamlit as st

def about():
    #about page title
    st.title("Trends Analytics")
    # company behind the app infomation
    st.write("**About Trends Analytics**.")
    st.info("Founded in 2022, Trends Analytics is a data driven company which provides data and business solutions. " +
            "We use Artificial Intelligence (AI) and Advanced Analytics to enable more personalised " +
            "solutions for your business needs. We are passionate about Artificial Intelligence and its impact in the " +
            "future of our society. We help optimise  operations, superior customer experiences and innovative business models. " +
            "We have a team of certified Data Professionals, which consists of Data Scientists, Engineers, Analysts and Project Managers.")
    st.markdown("")
    #app information
    st.write("**About Movie Xplorer**.")
    st.info("Movie Xplorer is a movie recommendation application which uses collaborative and content-based algorithms to recommend " +
            "movies to the user. The dataset is obtained from MovieLens and is maintained by the GroupLens research group in the " +
            "Department of Computer Science and Engineering at the University of Minnesota. Additional movie content data was legally " +
            "scraped from IMDB. The movie recommendations are catered to each user\'s needs and the user can comment about the movies they" +
            " have watched. The video content is legally scraped from YouTube.")
    st.markdown("")
    with st.expander("We are based at"):
        st.markdown("2ⁿᵈ floor")
        st.markdown("420 Milton Street")
        st.markdown("Marshaltown")
        st.markdown("Johannesburg 2000")
        st.markdown("Tel no: 011 668 4397(moviexp)")