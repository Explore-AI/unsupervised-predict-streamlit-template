# Streamlit dependencies
import streamlit as st

# Data dependencies
import numpy as np
import pandas as pd
import PIL
from PIL import Image

def main():
        img = Image.open('Kmeans.PNG')
        img1 = img.resize((2000,300))
        col1, col2, col3 = st.columns(3)
        with col1:
                st.text("")
        with col2:
                st.image(img1, caption=None, use_column_width=True)
        with col3:
                st.text("")
        st.subheader("KMeans Movie Recommender")
        st.markdown("Kmeans movie recommender is a web app that recommend movies to its users. In this system, users are asked to rate movies they just finished seeing and the ratings are used to recommend other movies to them.")
        img2 = Image.open('Moviepic')
        st.image(img2, caption=None)

        st.markdown("This app is built towards increasing users satisfaction of streaming apps by identifying movies users love through their ratings and recommending similar movies to them. In the same vein, the app identify movies users do not like and make sure similar movies to that are not recommended to such users. The recommendations take diffferent forms such as email notifications, in app notifications or making the recommended movies appear on the frontpage of the user's account.")
        st.markdown("As a way of showing the power of this app to our potential partners, we have provided an interface that allows people to select movies and get lists of movies similar to what they have selected.")
        st.subheader("Using The Kmeans Recommender")
        st.markdown("Go to the KMeans Recommender page.  \nEnter your movie title on the text box.  \nClick on Recommend and a list of similar movies will pop up.")
if __name__ == '__main__':
	main()
	
