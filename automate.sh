# the following commands are straight from EDSA, this file should be executed 5 to 10 minutes after mounting the s3 bucket
echo "the script has started"

cd ~/
sudo apt-get install automake autotools-dev fuse g++ git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev make pkg-config -y
cd unsupervised-predict-streamlit-template/
pip3 install -r requirements.txt
streamlit run --server.port 5000 edsa_recommender.py

