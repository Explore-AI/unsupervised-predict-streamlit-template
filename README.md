# Streamlit-based Movie Recommender System
 Two primary approaches are used in recommender systems are content-based and collaborative-based filtering.  In content-based filtering this similarity is measured between items based on their properties, while collaborative filtering uses similarities amongst users to drive recommendations. At a fundamental level, these systems operate using similarity, where we try to match people (users) to things (items). 
    
### 1) Screen recording

[![What is an API](resources/imgs/What_is_a_recommender_system.png)](https://youtu.be/Eeg1DEeWUjA)

#### 1.2) Description of contents

Below is a high-level description of the contents within this repo:

| File Name                             | Description                                                       |
| :---------------------                | :--------------------                                             |
| `edsa_recommender.py`                 | Base Streamlit application definition.                            |
| `recommenders/collaborative_based.py` | Implementation of collaborative filtering.                 |
| `recommenders/content_based.py`       | Implementation of content-based filtering.                 |
| `resources/data/`                     | Sample movie and rating data used to demonstrate app functioning. |
| `resources/models/`                   | Folder to store model and data binaries if produced.              |
| `utils/`                              | Folder to store additional helper functions for the Streamlit app |

## 2) Usage Instructions
### 2.1) Running the recommender locally
It is recommended that the following requirements  made available in a virtual ennvironment:
  -Python 3.6+ 
  -pip3
  -streamlit
  -numpy
  -pandas
  -scikit-learn
  -scikit-surprise
To run the app on a local machine will require the user to navigate to the base of the cloned repo and run the following command in the created virtual environment on git bash:  
 ```bash
 streamlit run edsa_recommender.py
 ```
 If the web server was able to initialise successfully, a local URL and Network URL should be displayed within your bash/terminal session. Copy and paste andy of these URLs in any broswer to access the app if not automatically directed to app upon running the code above.
| :zap: WARNING! :zap:                                                                                                    |
| :--------------------                                                                                                                             |
| This application uses extensive memory to generate results for the recommender system mode. Therefore, it is not recommendend to click the recommender button when running the app locally. Instead we recommend deploying this app on a larger AWS instance with sufficient memory (t2.2xlarge/t2.xlarge) and storage(>= 30 GiB)  |

#### 2.4) Running the recommender system on a remote AWS EC2 instance

The following steps will enable you to run your recommender system on a remote EC2 instance, allowing it to generate recommendation results.

1. Ensure that you have access to a running AWS EC2 instance with an assigned public IP address.

**[On the Host]:**

2. Install the prerequisite python libraries:

```bash
pip install -U streamlit numpy pandas scikit-learn
conda install -c conda-forge scikit-surprise
```

3. Clone your copy of the API repo, and navigate to its root directory:

```bash
git clone https://github.com/{your-account-name}/unsupervised-predict-streamlit-template.git
cd unsupervised-predict-streamlit-template/
```
4. Enter into a Tmux window within the current directory. To do this, simply type `tmux`.  

5. Start the Streamlit web app on port `5000` of the host

```bash
streamlit run --server.port 5000 edsa_recommender.py
```

If this command ran successfully, output similar to the following should be observed on the Host:

```
You can now view your Streamlit app in your browser.

  Network URL: http://172.31.47.109:5000
  External URL: http://3.250.50.104:5000

```

Where the specific `Network` and `External` URLs correspond to those assigned to your own EC2 instance. Copy the value of the external URL.  

**[On the Client]:**

6.  Within your favourite web browser (we hope this isn't Internet Explorer 9), navigate to external URL you just copied from the Host. This should correspond to the following form:

    `http://{public-ip-address-of-remote-machine}:5000`   

    Where the above public IP address corresponds to the one given to your AWS EC2 instance.

    If successful, you should see the landing page of the recommender system app.


![Explore Data Science Academy](resources/imgs/EDSA_logo.png)
