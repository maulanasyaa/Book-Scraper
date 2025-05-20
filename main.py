# ```python
import os 
from utils.parse_book import parse_book
from utils.create_file import create_file

BASE_URL = "https://books.toscrape.com"

def main():
    os.makedirs('data', exist_ok=True)
    try:
        books = parse_book(BASE_URL)
        create_file(books)
        print(f"Scraping {BASE_URL} : SUCCESS!")
    except Exception as e:
        print(f"Error : {e}")


if __name__ == '__main__' :
    main()