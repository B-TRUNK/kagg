#Grouping & Sorting

import pandas as pd
reviews = pd.read_csv("../data/reviews.csv")

"""
Introduction
============
Maps allow us to transform data in a DataFrame or Series one value at a time for an entire column. However,
often we want to group our data, and then do something specific to the group the data is in.
As you'll learn, we do this with the groupby() operation. We'll also cover some additional topics,
 such as more complex ways to index your DataFrames, along with how to sort your data.
"""

"""
Groupwise analysis
==================
One function we've been using heavily thus far is the value_counts() function.
 We can replicate what value_counts() does by doing the following:
"""
reviews.groupby('points').points.count()

"""
We can use any of the summary functions we've used before with this data. For example,
 to get the cheapest wine in each point value category,
 we can do the following:
"""
reviews.groupby('points').price.min()

"""
You can think of each group we generate as being a slice of our DataFrame containing only data with values that
match. This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data
in any way we see fit. For example, here's one way of selecting the name of the first wine reviewed from each
winery in the dataset:
"""
reviews.groupby('winery').apply(lambda df: df.title.iloc[0])

"""
For even more fine-grained control, you can also group by more than one column. For an example,
 here's how we would pick out the best wine by country and province:
"""
reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])

"""
Another groupby() method worth mentioning is agg(), which lets you run a bunch of different functions on your
 DataFrame simultaneously.
 For example, we can generate a simple statistical summary of the dataset as follows:
"""
reviews.groupby(['country']).price.agg([len, min, max])

"""

Multi-indexes
=============
In all of the examples we've seen thus far we've been working with DataFrame or Series objects with a
 single-label index. groupby() is slightly different in the fact that, depending on the operation we run,
   it will sometimes result in what is called a multi-index.

A multi-index differs from a regular index in that it has multiple levels. For example:
"""
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed

mi = countries_reviewed.index
type(mi)

"""
However, in general the multi-index method you will use most often is the one for converting back to a
regular index, the reset_index() method:
"""
countries_reviewed.reset_index()

"""

Sorting
=======
Looking again at countries_reviewed we can see that grouping returns data in index order, not in value order.
 That is to say, when outputting the result of a groupby, the order of the rows is dependent on the values in
   the index, not in the data.
To get data in the order want it in we can sort it ourselves. The sort_values() method is handy for this.
"""
countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')

"""
sort_values() defaults to an ascending sort, where the lowest values go first. However,
most of the time we want a descending sort, where the higher numbers go first. That goes thusly:
"""
countries_reviewed.sort_values(by='len', ascending=False)

#To sort by index values, use the companion method sort_index().
#This method has the same arguments and default order:
countries_reviewed.sort_index()

#Finally, know that you can sort by more than one column at a time:
countries_reviewed.sort_values(by=['country', 'len'])
