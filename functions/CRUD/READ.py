import csv
import streamlit as st

def select(): 
    # opening the CSV file
    with open('./resources/data/comments.csv', mode='r') as c:
    # reading the CSV file
        csvFile = csv.reader(c)
        # displaying the contents of the CSV file
        next(csvFile)
        for lines in csvFile:
                st.write(lines[0] + "\n\nComment : " + lines[1])
                # f'<a target="_blank" href="{link6}">Riaan James-Verwey</a>'
                