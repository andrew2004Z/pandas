import pandas

df = pandas.read_csv('dataset.csv')
print(df)
df = df[df.Name == 'Hamilton: The Revolution']
df = df[df.Name == 'Player\'s Handbook (Dungeons & Dragons)']
df = df[df.Year == 2015]
df = df[df.Name == 'Diagnostic and Statistical Manual of Mental Di...']
print(df)