# html temp
from pathlib import Path
html_temp = """
            <div style="background-color:#373645;padding:10px">
            <h2 style="color:white;text-align:center;"><b>Solution Approach</b></h2>
            </div>
            """

html_overview = """
                <figure style:"align:center;">
                <img alt="" src="https://cdn-images-1.medium.com/max/591/1*KQxKzb8hE2_t72TBRFl2Bg.png", 
                        style:"align:center">
                        <figcaption style="text-align:center;">
                            The diagram above is a representation of a recommender
                            system running on collaborative filtering method.
                        </figcaption>
                </figure>
                <a>
                    In this project, we were provided with two types of filtering methods namely: 
                    collaborative and content based.
                </a>
                <br></br>
                <ul>
                    <li>
                        Content Based Filtering: To derive our content based recommender system,
                        we gathered the various properties of our items so 
                        that we can convert them into meaningful features.
                        This was done in the feature engineering section.
                        We combined five different features that include title,
                        title cast, director, plot keywords and genre. The data was
                        vectorized and then a similarity index trained using cosine similarity module from scikit-learn.
                    </li>
                    <li>
                        Collaborative Filtering: We utilized Singular Value Decomposition (SVD) from surprise library\
                        to train a model for the collaborative recommender system. \
                        The goal of SVD is to obtain latent factors that are used to \
                        compared similarity across the movie selection of different users
                    </li>
                </ul>
                <br></br>
                <p>
                    The major tweaking of the model was on collaborative filtering method. The notebook provides additional
                    details on both the content and collaborative based models that were developed for the project.
                <p>
                <h3>Project Requirements</h3>
                <p>
                    To build the Model for recommender, we used these packages: Pandas, numpy, Surprise,
                    a Python scikit package built for collaborative filtering.
                </p>
                <h3>Scikit-Surprise<h3>
                <p>
                    The team took advantage of the built-in Scikit-Surprise user rating matrix that is designed for
                    collaborative filtering. Surprise had a significant impact on the time taken to prepare the data
                    because the team relied on the inbuilt user rating systems to read the train dataset. 
                </p>
                <h3>Algorithms</h3>
                <p>
                    Surprise offers 11 different prediction algorithms including variations of KNN and dimensionality reduction 
                    techniques such as SVD and NMF. For this demonstration, we ended up using SVD (Singular Value Decomposition).The SVD model from suprise library was used to train a dataset that contains 
                    four features namely: userId, movieId, rating and timestamp. Timestamp feature was dropped because of the
                    challenges associated with dealing with the datetime format when loading the data to the surprise reader
                    package.
                </p>
                <ul>
                    <li>SVD: A matrix factorization technique popularized by Simon Funk as part of the Netflix prize.</li>
                </ul>
                <h3>Model Evaluation</h3>
                <p>
                    Model accuracy can be evaluated using a qualitative data and quantitative data. In most cases, it is 
                    recommended to use both approaches when assessing model performance. A qualitative approach entails
                    critically analysing the data to check if the recommendations from the model make sense based on the user
                    historical information. The quantitative approach relies on error measurements like root mean squared 
                    error(RMSE) or mean absolute error(MAE). In this project, RMSE was used because there was no access to
                    additioanl information and the time allocated for the project was limited. The best performing model was
                    SVD with a RMSE score of 0.81 on the Kaggle Leaderboard.
                </p>
                <h3>Model Tuning</h3>
                <p>
                    The surprise package offers an option of the cross validate feature that can be used to train models.
                    The model was passed through a five fold cross validation during the fitting stage before being fitted
                    on the training data.
                </p>
                """


# ========================================================================
slides = """
  <div  style:"margin: 0 auto";>
    <!-- this is the embed code provided by Google -->
      <iframe src="https://docs.google.com/presentation/d/1nSL8lKFZ5tdAi7N6yQq2zgNc6DaNYAi0bCUDOj244nk/edit?usp=sharing" 
          frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" 
          webkitallowfullscreen="true">
       </iframe> 
    <!-- Google embed ends -->
  </div>
       """

# ===================================================================================
eda_header = """
    <div style="background-color:#362B39;padding:10px;">
        <h2 style="color:white; text-align:center;">
            <b>Exploratory Data Analysis</b>
        </h2>
        <a style="color:white;text-align:center;">
            Exploratory Data Analysis (EDA) is about understanding the dataset and
            deriving patterns that can help with feature engineering and modelling. In this section,
            we have a few visuals to describe patterns in the data.  A detailed analysis is
            available in our notebook hosted in our Github repository.
        </a>
    </div>
            """
# ===================================================================================
rec_header = """
    <div style="background-color:#362b39;padding:10px">
        <h2 style = "color:white; text-align:center;">
            <b>Movie Recommender Engine</b>
        </h2>
        <h3 style ="color:white;text-align:center">
            Thirteen Analytics - Explore Data Science Academy
        </h3>
    </div>
            """
# ===================================================================================
sweet = """
    <div style="background-color:#362B39;padding:10px;">
            <h2 style="color:white; text-align:center;">
                <b>SWEETVIZ</b>
            </h2>
            <a style="color:white;text-align:center;">
                Sweetviz is an open source Python based library that is used to generate a simple report
                about a dataset. Sweetviz provides high density visualizations
                based on the data sources of the movie recommender engine.
            </a2>
    </div>
            """
# ===================================================================================
prof = """
    <div style="background-color:#362B39;padding:10px;">
        <h2 style="color:white;text-align:center;">
            <b>Data Overview</b></h2>
        <a style="color:white;text-align:center;"> 
                Pandas profiling aids in the provision of analytical overview
                of the data. In this section, you can familiriaze with the datasets by looking at 
                descriptive statistics generated by pandas profiling.
        </a>
    </div>
            """
# ===================================================================================
team = """
<style>
    body {
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
    }

    html {
  box-sizing: border-box;
    }

*, *:before, *:after {
  box-sizing: inherit;
}

.column {
  float: left;
  width: 33.3%;
  margin-bottom: 16px;
  padding: 0 8px;
}

.card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  margin: 8px;
}

.about-section {
  padding: 50px;
  text-align: center;
  background-color: #474e5d;
  color: white;
}

.container {
  padding: 0 16px;
}

.container::after, .row::after {
  content: "";
  clear: both;
  display: table;
}

.title {
  color: grey;
}

.button {
  border: none;
  outline: 0;
  display: inline-block;
  padding: 8px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
}

.button:hover {
  background-color: #555;
}

@media screen and (max-width: 650px) {
  .column {
    width: 100%;
    display: block;
  }
}
</style>
<body>
<div class="about-section">
  <h1 style="color:white;">About Us Page</h1>
  <p>
    Thirteen Analytics is an African multinational technology corporation based in Johannesburg,
    South-Africa and its presence and operations in 2 economic giant countries 
    (Nigeria and Kenya). The company is known for innovations and application of
     Data Engineering, Analytics, Machine learning Models and Business intelligence to 
     provide cost-effective solutions to business problems.
  </p>
</div>

<h2 style="text-align:center">Our Team</h2>
<div class="row">
  <div class="column">
    <div class="card">
      <img src="/w3images/team1.jpg" alt="Ola" style="width:100%">
      <div class="container">
        <h2>Olanidotun Jonibola</h2>
        <p class="title">Team Lead</p>
        <p>Experienced in handling Data Science Projects.</p>
        <p>jane@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="/w3images/team2.jpg" alt="Khoele" style="width:100%">
      <div class="container">
        <h2>Joshua Khoele</h2>
        <p class="title">Senior Data Analyst</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>mike@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="/w3images/team3.jpg" alt="Gadvin" style="width:100%">
      <div class="container">
        <h2>Gadvin Gitamo</h2>
        <p class="title">Senior Data Engineer</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>john@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="/w3images/team2.jpg" alt="Hunadi" style="width:100%">
      <div class="container">
        <h2>Hunadi Mawela</h2>
        <p class="title">Senior Web Developer</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>mike@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>

  <div class="column">
    <div class="card">
      <img src="https://drive.google.com/file/d/1PHu4Cg4oLDCJL4qnoysCqrdplHoMVUPn/view?usp=sharing" alt="Jack" style="width:100%">
      <div class="container">
        <h2>Jack Kamire</h2>
        <p class="title">Senior Modelling Engineer</p>
        <p>Some text that describes me lorem ipsum ipsum lorem.</p>
        <p>mike@example.com</p>
        <p><button class="button">Contact</button></p>
      </div>
    </div>
  </div>
</div>
</body>
"""


def read_file(markdown_file, folder):
    return Path(folder+markdown_file).read_text()


home = read_file("index.html", "./utils/")
