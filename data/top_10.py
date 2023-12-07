import pandas as pd

top_200=pd.read_parquet('../data/top_200.parquet')

top_10=top_200[top_200['show_ranking']<11]
top_10.groupby('showName').head(10)

top_10.to_csv('top_10.csv')

