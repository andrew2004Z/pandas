import pandas

df = pandas.read_csv('dataset.csv')
print(df)
df['a'] = df['User Rating']

df = df[(df.Year == 2010)]
df = df[df.a == 4.8]
print(df.head)