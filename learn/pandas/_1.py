import pandas as pd

df = pd.DataFrame(
    {'Yes': [50, 21],
     'No': [131, 2]
    })

df2 = pd.DataFrame(
    {'Bob': ['I liked it.', 'It was awful.'], 
     'Sue': ['Pretty good.', 'Bland.']},
    index=['Product A', 'Product B'])

df3 = pd.Series([1, 2, 3, 4, 5])

df4 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

print(df ,"\n====================\n" ,df2 ,"\n====================\n", df3 ,"\n====================\n", df4)