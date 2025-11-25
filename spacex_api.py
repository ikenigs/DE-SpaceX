import requests
import pandas as pd

response = requests.get("https://api.spacexdata.com/v4/launches/latest")
data = response.json()

df=pd.dataframe(data)
print(df).head(5)

