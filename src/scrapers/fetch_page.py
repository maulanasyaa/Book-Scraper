import requests
from bs4 import BeautifulSoup

def fetch_page(url, parser = 'lxml') -> BeautifulSoup:
    try:
        # request to website 
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # create parser 
        soup = BeautifulSoup(response.text, parser)
        return soup
    except Exception as e:
        print(f"Error saat request: {e}")
