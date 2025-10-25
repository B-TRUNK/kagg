#this code deals with pandas mapping functions

import pandas as pd

"""
Summary functions:
==================
Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way.
 For example, consider the describe() method:
"""

reviews = pd.read_csv("../data/reviews.csv")

print(reviews.head())

#data description
print(reviews.points.describe())

"""
This method generates a high-level summary of the attributes of the given column. It is type-aware,
 meaning that its output changes based on the data type of the input.
 The output above only makes sense for numerical data; for string data here's what we get:
"""

print(reviews.country.describe())

"""


If you want to get some particular simple summary statistic about a column in a DataFrame or a Series,
 there is usually a helpful pandas function that makes it happen.
For example, to see the mean of the points allotted (e.g. how well an averagely rated wine does),
 we can use the mean() function:
"""

print(reviews.points.mean())




#To see a list of unique values we can use the unique() function:
print(reviews.country.unique())

#To see a list of unique values and how often they occur in the dataset, we can use the value_counts() method:
print(reviews.country.value_counts())

"""
Maps
====
A map is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values.
In data science we often have a need for creating new representations from existing data,
or for transforming data from the format it is in now to the format that we want it to be in later.
Maps are what handle this work, making them extremely important for getting your work done!
There are two mapping methods that you will use often.
"""

review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)


#apply() is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

print(reviews.apply(remean_points, axis='columns'))

#Pandas will also understand what to do if we perform these operations between
#  Series of equal length. For example,
#  an easy way of combining country and region information in the dataset would be to do the following:

print(reviews.country + " - " + reviews.region_1)
