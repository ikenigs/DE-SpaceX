import requests
import pandas as pd

url = "https://api.spacexdata.com/v4/launches"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)
print(df.head())
print(df.columns)
print(df.dtypes)
