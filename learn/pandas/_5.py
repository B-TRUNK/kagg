import pandas as pd
reviews = pd.read_csv("../data/reviews.csv")

#Dtypes
reviews.price.dtype

#Alternatively, the dtypes property returns the dtype of every column in the DataFrame:
reviews.dtypes

#It's possible to convert a column of one type into another wherever such a conversion makes sense by using 
# the astype() function. For example,
#  we may transform the points column from its existing int64 data type into a float64 data type:
reviews.points.astype('float64')

#A DataFrame or Series index has its own dtype, too:
reviews.index.dtype

#Missing data
reviews[pd.isnull(reviews.country)]

#Replacing missing values is a common operation. Pandas provides a really handy method for this problem: fillna().
#  fillna() provides a few different strategies for mitigating such data.
#  For example, we can simply replace each NaN with an "Unknown":
reviews.region_2.fillna("Unknown")

"""
Alternatively, we may have a non-null value that we would like to replace. For example,
 suppose that since this dataset was published,
   reviewer Kerin O'Keefe has changed her Twitter handle from @kerinokeefe to @kerino.
     One way to reflect this in the dataset is using the replace() method:
"""
reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")

#The replace() method is worth mentioning here because it's handy for replacing missing data which is given
#some kind of sentinel value in the dataset: things like "Unknown", "Undisclosed", "Invalid", and so on.