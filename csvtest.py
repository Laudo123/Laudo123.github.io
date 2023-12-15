import pandas as pd

# Load data from the CSV file
songs = pd.read_csv("static/genres_v2.csv")
#data = pd.read_csv("/home/Laudo/Laudo123.github.io/static/data.csv") # for pythonanywere
songs.drop(songs.columns[0], axis=1, inplace=True)
random_song_id = songs['id'].sample(1).tolist()
song_url = "https://open.spotify.com/embed/track/{}?utm_source=generator&theme=0&autoplay=1".format(random_song_id[0])
print(song_url)
