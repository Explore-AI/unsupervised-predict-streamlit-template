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

        st.subheader("About Us")
        st.markdown("KMeans AI is an Artificial Integlligence and Data Analytics services company with its headquarter in Lagos, Nigeria. In over 10 years of its existence as a tech company, KMeans has served over 5 thousand businesses globally, leveraging on robust technologies in the Data and AI space. With a strong and an experienced team of Data professionals, KMeans bring solutions to real life problems using data driven techniques. For more information about us, visit https://www.kmeansAI.com")
        st.subheader("Meet the team")

        img2 = Image.open('KmeansTeam.png')
        img3 = img2.resize((1500,1000))
        st.image(img3, caption=None, use_column_width=True)
        st.markdown("Asides helping businesses solve real life problems, KMeans AI also have a network of aspiring data professionals from Africa. Being that the entire KMeans AI team is made up of Africans and the organization has gone globally, KMeans AI created the network as a way of giving back to the society that made them. The KMeans AI team train young Africans on various tech paths such as Data Analytics, Data Science, Software Development to mention but a few. KMeans AI also give them the opportunity to intern with them, giving them the opportunity of expereincing how the working environment works.")
if __name__ == '__main__':
	main()
