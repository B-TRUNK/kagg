import pandas as pd

# Load a CSV file into a DataFrame
data = pd.read_csv('../data/reviews.csv')

# 1 - load a column
print(data.country)
# 2 - load a column using dictionary notation
print(data['country'])

# 3 - load a row by position
print('First Row Col 0 = ', data['country'][0])

# 4 - index-based selection with iloc
print('iloc[0]' ,data.iloc[0])
print('iloc[:, 0]' ,data.iloc[:, 0])
print('iloc[:3, 0]' ,data.iloc[:3, :2])
print('iloc[[0, 1, 2], :3]' ,data.iloc[[0, 1, 2], :3])
print('iloc[-5:]', data.iloc[-5:])

# 5 - label-based selection with loc
print('[0, "country"]', data.loc[0, 'country'])
print(data.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

# 6 - Manipulating the index
data.set_index('title')
print(data.head())

# 7 - Conditional selection
data.country == 'Italy'
data.loc[data.country == 'Italy']
data.loc[(data.country == 'Italy') & (data.points >= 90)]
data.loc[(data.country == 'Italy') | (data.points >= 90)]
data.loc[data.country.isin(['Italy', 'France'])]
data.loc[data.price.notnull()]
print('NUll prices :', data.loc[data.price.isnull()])
data.loc[data.price.notnull()]

# 8 - Assigning data
data['critic'] = 'everyone'
data['index_backwards'] = range(len(data), 0, -1)