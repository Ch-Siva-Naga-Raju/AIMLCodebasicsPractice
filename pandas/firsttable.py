import pandas

mydataset = {
    "books" : ['Rich Dad Poor Dad', 'Security Analysis', 'Harry Potter'],
    "usefullness": [5, 4, 2],
    "entertainment": [3, 1, 5]
}

bookTable = pandas.DataFrame(mydataset)
print(bookTable)