import pandas as pd
import random
from flask import Flask, render_template


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching during development
data = pd.read_csv("static/data.csv")
#data = pd.read_csv("/home/Laudo/Laudo123.github.io/static/data.csv") # for pythonanywere
data.drop(data.columns[0], axis=1, inplace=True)
data = data.dropna()
data['Year'] = data['Year'].astype('int32')

songs = pd.read_csv("static/genres_v2.csv")
#songs = pd.read_csv("/home/Laudo/Laudo123.github.io/static/genres_v2.csv") # for pythonanywere
songs.drop(songs.columns[0], axis=1, inplace=True)

spider_chart_images = [
    f"static/images/spider_chart{i}.png" for i in range(10) # f"/home/Laudo/Laudo123.github.io/static/images/spider_chart{i}.png" for i in range(10)
]

@app.route('/')


def index():
    # For simplicity, assume you have a list of image URLs
    random_urls = data['Image'].sample(15).tolist()
    # random_indices = data.sample(15).index.tolist()
    # random_urls = data.loc[random_indices, 'Image'].tolist()
    # random_descriptions = data.loc[random_indices, 'Description'].tolist()
    random_song_id = songs['id'].sample(1).tolist()
    song_url = "https://open.spotify.com/embed/track/{}?utm_source=generator&theme=0&autoplay=1".format(random_song_id[0])
    random_spider_chart = random.choice(spider_chart_images)
    return render_template('index.html', random_urls=random_urls, song_url=song_url, random_spider_chart=random_spider_chart)

if __name__ == '__main__':
    app.run(debug=True)


