# visuals will come here
from sqlalchemy import true
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# load data
movies = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/movies.csv')
imdb = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/imdb_data.csv')
imdb_data_budget = imdb['runtime'].to_list()
ratings = pd.read_csv('resources/data/ratings.csv')
movies = movies.dropna() 
@st.cache(allow_output_mutation=True)

def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        body {
        background-image: url('data:image/gif;base64,%s');
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

def visuals():
    
        st.subheader('Xplore the Statistics')
        st.write("**Hi Xplorer**, you can explore some interesting stats about the movies.")
        
        with st.expander("Statistics Xplorer"):
                st.write("### Moivie KPIs 1900-2022")
                kpi2, kpi1, kpi3 = st.columns(3)
                my_dynamic_value = 3716.5 

                new_val = 222

                final_val = my_dynamic_value / new_val
                
                kpi1.metric(label = "Avg released movies",
                        value = 3716.5,
                        delta = 1411)

                kpi3.metric(label = "Avg rating",
                        value = 3.54 )
                st.info('Select 2 or more metrics to plot 1 or more movie statistics')
                options = st.multiselect('', ['Ratings', 'Movies', 'Ratings Frequency','Distribution', 'Genres', 'Top Rated'])
                if 'Movies' in options and 'Distribution' in options:

                        movies['year'] = [x[-1].strip('()') for x in movies.title.str.split(" ")]
        
                        num_pattern = r'^$|[a-zA-Z]|Τσιτσάνης|101次求婚|2006–2007|выбывание|پدر|Начальник|Джа|Девочки|первого'
                        movies["year"] = movies["year"].replace(to_replace = num_pattern, value = np.nan, regex = True)
                        year = [int(x) for x in movies["year"].dropna()]
                        fig = plt.figure(figsize=(9,3))
                        sns.histplot(year, kde = True,color = '#FF4B4B')
                        plt.xlabel('Year')
                        plt.xlim(left=1900, right = 2022)
                        plt.title('Movie Release Year Distribution', fontweight = 'bold')
                        st.pyplot(fig)
                        st.info(f'Our algorithms recommend from few 90s movie classics and a significant number 21st century movies')
                if 'Ratings' in options and 'Distribution' in options:
                        # plot movie ratings distribution 
                        fig = plt.figure(figsize=(9,3))
                        sns.boxplot(x = "rating", data=ratings, color = '#FF4B4B')
                        plt.title('Movie Ratings Distribution', fontweight = 'bold')
                        plt.show()
                        st.pyplot(fig)
                        st.info(f'Average rating  distribution is {round(np.mean(ratings["rating"]),2)} with 75% of the ratings greater than 3.')
                if 'Distribution' in options and 'Ratings Frequency' in options:
                        st.image('./resources/imgs/Ratings.png')
                        st.info("We can see the most frequent movie rating is at 4.0 with the least at 1.5")
                if 'Genres' in options and 'Top Rated' in options:
                        st.image('./resources/imgs/genres.png')
                        st.info("We can see the most popular movie genres rated and drama is dramatically the most popular with 16.2%")
        