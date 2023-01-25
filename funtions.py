
# Data dependencies
import pandas as pd



# Load your raw data
df = pd.read_csv('resources/data/movies.csv')

#df= df[df.title.duplicated(keep=false)]
print (df.descibe())