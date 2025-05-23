# ```python
import os 
from dotenv import load_dotenv
from scrapers.parse_book import parse_book
from scrapers.create_file import create_file

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.google.com")

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