import csv

def insert(post):
    with open('./resources/data/comments.csv', 'a', newline='', encoding='UTF8') as c:
        writer = csv.writer(c)
        # write the data
        writer.writerow(post)