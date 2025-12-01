import pandas as pd
import singer
from schema import schema

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    df = pd.read_json(url)

    # Convert to pure Python types, remove NaN, convert timestamps
    df = df.astype(object).where(pd.notnull(df), None)

    records = df.to_dict(orient='records')

    singer.write_schema('launches', schema, 'id')
    singer.write_records('launches', records)

if __name__ == '__main__':
    main()