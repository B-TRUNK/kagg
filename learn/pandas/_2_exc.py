import pandas as pd


#Create a variable df containing the country, province, region_1, and region_2 columns of the records with the index labels
#  0, 1, 10, and 100. In other words, generate the following DataFrame:
data = pd.read_csv('../data/reviews.csv')

df = data.loc[[0, 1, 10, 100], ['country', 'province', 'region_1', 'region_2']]
print(df)

#Create a variable df containing the country and variety columns of the first 100 records.
var = data.loc[:99, ['country', 'variety']] 

#Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = data.loc[data.country == 'Italy']
print(italian_wines)

#Create a DataFrame `top_oceania_wines` containing all reviews with at least 95 points (out of 100)
#  for wines from Australia or New Zealand.
top_oceania_wines = data.loc[((data.country == 'Australia') | (data.country == 'New Zealand')) & (data.points >= 95)]
print(top_oceania_wines)

