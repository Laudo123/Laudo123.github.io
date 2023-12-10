import pandas as pd

# Load data from the CSV file
data = pd.read_csv("static/data.csv")
data.drop(data.columns[0], axis=1, inplace=True)
data = data.dropna()
data['Year'] = data['Year'].astype('int32')

random_urls = data['Image'].sample(15).tolist()
print(random_urls)

