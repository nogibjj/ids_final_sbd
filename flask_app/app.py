from flask import Flask, render_template
import pandas as pd
import os

# Read the dataset
top_200 = pd.read_parquet('https://github.com/nogibjj/ids_final_sbd/raw/main/data/top_200.parquet')

top_10=top_200[top_200['ranking_spotify']<11]
top_10=top_10.groupby('showName').tail(3)


app = Flask(__name__)

@app.route("/")
def index():
  shows_and_data = {}
  for index, row in top_10.iterrows():
    show_name = row['showName']
    total_episodes = row['show_episodes.total']

        # Convert the URL column to a list
    urls = row['ep_audio_preview_url'].split(', ')

    if show_name not in shows_and_data:
      shows_and_data[show_name] = {
                'total_episodes': total_episodes,
                'urls': [],
                'external_url': row['show_external_url'],
                'description': row['showDescription']
            }

    shows_and_data[show_name]['urls'].extend(urls)

  return render_template('index.html', shows_and_data=shows_and_data)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
