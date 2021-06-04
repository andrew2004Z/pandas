import pandas

df = pandas.read_csv('dataset.csv')
print(df)
minl = 200000
miny = 2009
for i in range(2009, 2019):
    df = pandas.read_csv('dataset.csv')
    df = df[df.Year == i]
    if len(df) < minl:
        minl = len(df)
        miny = i
print(miny)