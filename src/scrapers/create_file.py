import pandas as pd

def create_file(data: list[dict]) -> None:
    # create file
    df = pd.DataFrame(data)
    df.to_csv('data/books.csv', index=False)
    df.to_json('data/books.json', orient='records', indent=4)