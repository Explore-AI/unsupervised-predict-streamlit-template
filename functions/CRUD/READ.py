import csv
import streamlit as st

COMMENT_TEMPLATE_MD = """{} - {}
> {}"""

def select(): 
    # opening the CSV file
    with open('./resources/data/comments.csv', mode='r') as c:
    # reading the CSV file
        csvFile = csv.reader(c)
        # displaying the contents of the CSV file
        next(csvFile)
        for lines in csvFile:
                st.markdown(COMMENT_TEMPLATE_MD.format(lines[0], lines[2], lines[1]))
                