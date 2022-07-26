# visuals will come here
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_tags import st_tags
import base64
import string
import re
movies = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/movies.csv')
imdb_data_budget = pd.read_csv('https://raw.githubusercontent.com/Dream-Team-Unsupervised/Data/main/imdb_data.csv')
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
        background-image: url("data:image/gif;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return

def visuals():
        
        set_png_as_page_bg('./resources/imgs/stats.gif')
    
        st.title("Xplore the Statistics")
        st.write("**Hi there**, you can explore some interesting stats about the movies.")

        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: right;} </style>', unsafe_allow_html=True)
        st.write('<style>div.st-bf{flex-direction:column;} div.st-ag{font-weight:bold;padding-left:2px;}</style>', unsafe_allow_html=True)
        chart = st.radio("",("Bar Chart","Line Chart","Box Plot"))
    
        if chart == "Bar Chart":
                with st.expander("Bar Chart"):
                        options = st.multiselect('Select data', ['titles', 'genres'])
                        st.write(options)
                
        elif chart == "Line Chart":
            with st.expander("Line Chart"):
                options = st.multiselect('Select data', ['Genres', 'Ratings', 'Years', 'Budget'])

                if 'Years' in options:
                        st.markdown("### KPI 1900-2022")
                        kpi1, kpi2, kpi3 = st.columns(3)

                        my_dynamic_value = 333.3335 

                        new_val = 222

                        final_val = my_dynamic_value / new_val

                        kpi1.metric(label = "Avg released movies",
                                value = 3716.5,
                                delta = 1411)

                        kpi2.metric(label = "Bounce Rate",
                                value = 78,
                                delta = -5,
                                delta_color = 'inverse')
                        kpi3.metric(label = "Unique Visitors",
                                value = "%.2f" %final_val )
                
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
                elif 'Budget' in options:
                        # budget distribution plot
                        st.markdown("<h1 style = 'text-align: center;'>Movie Budget Distribution</h1>", unsafe_allow_html=True)
                        # punctuations = string.punctuation 
                        # budget = []
                        # for text in imdb_data_budget.to_list():
                        #         budget.append(int(re.sub('^[a-zA-Z]+','',text.translate(str.maketrans(' ',' ', punctuations)))))
                        #         budget_df  = pd.DataFrame(budget, columns = ['budget'])
                        #         fig = plt.figure(figsize=(9,3))
                        #         sns.histplot(budget_df['budget'], bins=10000, color = '#FF824E')
                        #         plt.xlabel('Budget')
                        #         plt.xlim(left=0,right = 250000000)
                        #         plt.title('Movie Budget Distribution', fontweight = 'bold')
                        #         st.pyplot(fig)
                        #         st.write(f'Average rating  database: {round(np.mean(budget_df["budget"]),2)} with a skewness to the right.')
        elif chart == "Box Plot":
                with st.expander("Box Plot"):
                        options = st.multiselect('Select data', ['Ratings', 'Years'])
                        
                        if 'Ratings' in options:
                                # plot movie ratings distribution 
                                fig = plt.figure(figsize=(9,3))
                                sns.boxplot(x = "rating", data=ratings, color = '#FF4B4B')
                                plt.title('Movie Ratings Distribution', fontweight = 'bold')
                                plt.show()
                                st.pyplot(fig)
                                st.info(f'Average rating  database: {round(np.mean(ratings["rating"]),2)} with 75% of the rating greater than 3.')
#     st.write("Due to the popularity of movies since 1974 we can definitely agree that there has been a influx of movies per annum.")
#     # st.image('./resources/imgs/stats.gif')
#     st.image('./resources/imgs/newplot2.png')
#     st.markdown("")
#     st.write("Below you can find the most popular genres rated for #appname") 
#     st.image('./resources/imgs/newplot3.png')
#     st.markdown("")
#     st.write("")
#     st.image('./resources/imgs/newplot4.png')
#     st.markdown("")
#     st.write("")
#     st.image('./resources/imgs/newplot5.png')
 # TODO: this should probably display visuals without returning anything