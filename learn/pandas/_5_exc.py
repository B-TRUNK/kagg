import pandas as pd
reviews = pd.read_csv("../data/reviews.csv")

#What is the data type of the points column in the dataset?
dtype = reviews.points.dtype

#Create a Series from entries in the points column, but convert the entries to strings.
#  Hint: strings are str in native Python.
point_strings = reviews.points.astype('str')

#Sometimes the price column is null. How many reviews in the dataset are missing a price?
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

"""
What are the most common wine-producing regions? Create a Series counting the number of times each value occurs
 in the region_1 field. This field is often missing data, so replace missing values with Unknown.
   Sort in descending order. Your output should look something like this:

Unknown                    21247
Napa Valley                 4480
                           ...  
Bardolino Superiore            1
Primitivo del Tarantino        1
Name: region_1, Length: 1230, dtype: int64
"""
reviews_per_region = reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
