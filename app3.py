
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Read the dataset
#top_200 = pd.read_parquet('https://github.com/nogibjj/ids_final_sbd/raw/main/data/top_200.parquet')
top_200 = pd.read_parquet('data/top_200.parquet')
@app.route("/", methods=['GET', 'POST'])
def index():
    ranking_type = request.form.get('ranking_type', 'ranking_spotify')

    if ranking_type == 'ranking_time':
        top_filtered = top_200[top_200['ranking_time'] < 11].groupby('showName').tail(3).sort_values(by='ranking_time', ascending=True)
    elif ranking_type == 'ranking_episodes':
        top_filtered = top_200[top_200['ranking_episodes'] < 11].groupby('showName').tail(3).sort_values(by='ranking_episodes', ascending=True)
    else:
        top_filtered = top_200[top_200['ranking_spotify'] < 11].groupby('showName').tail(3)

    shows_and_data = {}
    for _, row in top_filtered.iterrows():
        show_name = row['showName']
        total_episodes = row['show_episodes.total']
        average_episode_t= row['average_ep_duration_minutes']
        image= row['showImageUrl']

        # Convert the URL column to a list, Handle missing or None values in 'ep_audio_preview_url'
        urls = row['ep_audio_preview_url']
        if urls:
            urls = urls.split(', ')
        else:
            urls = []

        if show_name not in shows_and_data:
            shows_and_data[show_name] = {
                'total_episodes': total_episodes,
                'av_episode_t':average_episode_t,
                'image':image,
                'urls': [],
                'external_url': row['show_external_url'],
                'description': row['showDescription']
            }

        shows_and_data[show_name]['urls'].extend(urls)

    return render_template('index3.html', shows_and_data=shows_and_data, ranking_type=ranking_type)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
