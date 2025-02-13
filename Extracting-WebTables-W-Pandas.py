# pip install pandas
# pip install lxml 

import pandas as pd

nobel = pd.read_html('https://en.wikipedia.org/wiki/List_of_Nobel_laureates')
print(len(nobel))
print(nobel)

# The pandas.read_html() function is used to extract tables from HTML content. Under the hood, 
# it relies on external libraries to parse the HTML and convert it into a structured format (like a DataFrame). The two most common libraries for this are:
# lxml: A fast and efficient library for processing XML and HTML.
# html5lib: A pure Python library that parses HTML more leniently, similar to how web browsers do.
# By default, pandas tries to use lxml because it is faster and more memory-efficient than html5lib. 
# However, lxml is not included with Python or pandas by default, so you need to install it separately.
# test