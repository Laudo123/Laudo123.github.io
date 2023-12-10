import pandas as pd
from flask import Flask, render_template


app = Flask(__name__)
data = pd.read_csv("static/data.csv")
data.drop(data.columns[0], axis=1, inplace=True)
data = data.dropna()
data['Year'] = data['Year'].astype('int32')

@app.route('/')

def index():
    # For simplicity, assume you have a list of image URLs
    random_urls = data['Image'].sample(15).tolist()

    return render_template('index.html', random_urls=random_urls)


if __name__ == '__main__':
    app.run(debug=True)


