import pandas

df = pandas.read_csv('dataset.csv')
df['r'] = abs(df['y1'] - df['y2'])
print(sum(df['r']))