import pandas

df = pandas.read_csv('dataset.csv')
min_y1, max_y1 = min(df.y1), max(df.y1)
min_y2, max_y2 = min(df.y2), max(df.y2)
df['y1_norm'] = (df['y1'] - min_y1) / (max_y1 - min_y1)
df['y2_norm'] = (df['y2'] - min_y2) / (max_y2 - min_y2)

print(sum(df.y1_norm) / len(df), sum(df.y2_norm) / len(df), sorted(df.y1_norm)[len(df)//2], sorted(df.y2_norm)[len(df)//2])