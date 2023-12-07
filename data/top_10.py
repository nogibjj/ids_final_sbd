import pandas as pd

top_200=pd.read_parquet('../data/top_200.parquet')

top_10=top_200[top_200['show_ranking']<11]
top_10=top_10.groupby('showName').head(3)

#top_10.to_csv('top_10.csv')

unique_shows = sorted(top_10['showName'].unique())
     # Create a dictionary to store showName and corresponding episode audio URLs
shows_and_urls = {}
for show in unique_shows:
    top_10_episodes = top_10[top_10['showName'] == show]
    audio_urls = top_10_episodes['ep_audio_preview_url'].tolist()
    shows_and_urls[show] = audio_urls