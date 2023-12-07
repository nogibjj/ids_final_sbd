from flask import Flask, render_template, request
import pandas as pd
#import delta.tables as dt
import requests

top_10=pd.read_csv('./data/top10.csv')

dict_

app = Flask(__name__)

@app.route("/")
def index():
    podcast_info = [
        {"title": "First Podcast", "url": "https://podz-content.spotifycdn.com/audio/clips/5grWoXOWl74u1vgLKmhONz/clip_2908400_2959200.mp3"},
        {"title": "Second Podcast", "url": "https://example.com/second_podcast.mp3"},
        {"title": "Third Podcast", "url": "https://example.com/third_podcast.mp3"}
    ]
    return render_template('index.html', podcast_info=podcast_info)

#if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)





# Assuming you have a Delta Lake table named 'your_table'
#delta_path = "/path/to/delta/table"
#
#@app.route('/')
#def index():
#    return render_template('index.html')
#
#@app.route('/execute_sql', methods=['POST'])
#def execute_sql():
#    sql_command = request.form['sql_command']
#    
#    # Execute the SQL command on the Delta Lake table
#    delta_table = dt.DeltaTable.forPath(spark, delta_path)
#    delta_table.update(sql_command)
#
#    return render_template('index.html', message=f'SQL command executed: {sql_command}')
#
#if __name__ == '__main__':
#    app.run(debug=True)
