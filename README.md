![Movie_Recommendations](resources/imgs/Image_header.png)  
# Streamlit-based Recommender System
#### EXPLORE Data Science Academy Unsupervised Predict

## 1) Overview

This repository hosts the files needed to deploy **Movie Recommender Engine**, which was built using [Streamlit](https://www.streamlit.io/).   
This App was created by ss4_JHB_Unsupervised_team.

#### 1.2) Description of contents

Below is a high-level description of the contents within this repo:

| File Name                             | Description                                                       |
| :---------------------                | :--------------------                                             |
| `edsa_recommender.py`                 | Base Streamlit application definition.                            |
| `recommenders/collaborative_based.py` | Simple implementation of collaborative filtering.                 |
| `recommenders/content_based.py`       | Simple implementation of content-based filtering.                 |
| `resources/data/`                     | Sample movie and rating data used to demonstrate app functioning. |
| `resources/models/`                   | Folder to store model and data binaries if produced.              |
| `utils/`                              | Folder to store additional helper functions for the Streamlit app |



 
  **Note**:  The compute resources required for this app are heavy. It is suggested that an AWS instance with greater computing power is used. 


## 2) Prerequisite Python libraries

```python
streamlit
joblib
pandas
matplotlib
seaborn
wordcloud
re 
string
suprise
```

## 3) Usage Instructions

#### 3.1) Running the **Movie Recommender** web app on your local machine

Follow the steps below by running the given commands within a Git bash (Windows), or terminal (Mac/Linux):

 1. Ensure that you have the prerequisite Python libraries installed on your local machine

 2. Clone this *forked* repo to your local machine.

 ```bash
 git clone https://github.com/{your-account-name}/unsupervised-predict-streamlit-template.git
 ```  
 

 3. Navigate to the base of the cloned repo, and start the Streamlit app.

 ```bash
 cd unsupervised-predict-streamlit-template/
 streamlit run base_app.py
 ```

 If the web server was able to initialise successfully, the following message should be displayed within your bash/terminal session:

  You can now view your Streamlit app in your browser.

```bash
    Local URL: http://localhost:8501
    Network URL: http://192.168.43.41:8501
```

You should also be automatically directed to the base page of your web app. This should look something like this:

![Explore Data Science Academy](resources/imgs/landing_page_sample.png)

![Explore Data Science Academy](resources/imgs/EDSA_logo.png)