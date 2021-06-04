import pandas

df = pandas.read_csv('dataset_class.csv')
df1 = df[(df.y1 == 1) & (df.y1 == 1)]
tp = len(df1)
df1 = df[(df.y2 == 0) & (df.y1 == 1)]
fp = len(df1)
df1 = df[(df.y1 == 0) & (df.y1 == 1)]
fn = len(df1)
df1 = df[(df.y2 == 0) & (df.y1 == 0)]
tn = len(df1)
print((tp + tn) / (tp + tn + fn + fp))