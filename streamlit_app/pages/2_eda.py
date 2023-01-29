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
        df = pd.read_csv('movies.csv')
        col1, col2, col3 = st.columns(3)
        with col1:
                st.text("")
        with col2:
                st.image(img1, caption=None, use_column_width=True)
        with col3:
                st.text("")
        st.subheader("Data Exploration")
        st.markdown("The dataset used for the set up of this movie recommendation system is a dataset gotten from the internet movie database (imdb).  The dataset contains 62423 movies spanning various movie genres. Below are informations about the dataset:")
        st.dataframe(df)
if __name__ == '__main__':
	main()
