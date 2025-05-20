# ```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

from utils.fetch_page import fetch_page


def parse_book(url, parser = 'lxml') -> list[dict]:
    data: list[dict] = []

    # books container parsing
    all_books = fetch_page(url).find_all('article', class_ = 'product_pod')
    
    # html extract and store
    for books in all_books:
        # page access
        try:
            book_page_url = books.find('h3').find('a')['href']
            book_page = requests.get(urljoin(url,book_page_url))
            book_parser = BeautifulSoup(book_page.text, parser)
        except Exception as e:
            print(f"Create page parser error : {e}")
            return None
        
        # extract data from book page
        try:
            book_container = book_parser.select_one('div.container-fluid.page div.page_inner div.content div#content_inner article.product_page')
        
            # genre
            ul = book_parser.select_one('div.container-fluid.page div.page_inner ul.breadcrumb')
            li_list = ul.find_all('li')
            genre = li_list[2].text.strip()

            # title
            title = book_container.select_one('div.row div.col-sm-6.product_main h1').text

            # price
            price = book_container.select_one('div.row div.col-sm-6.product_main p.price_color').text.replace("\u00c2", "").replace("\u00a3", "")

            # stock
            stock = re.search(r'\d+', book_container.select_one('div.row div.col-sm-6.product_main p.instock.availability').text.strip()).group(0)

            # rating
            rating_tag = book_container.select_one('div.row div.col-sm-6.product_main p.star-rating')
            rating_dict = {
                'One' : 1,
                'Two' : 2,
                'Three' : 3,
                'Four' : 4,
                'Five' : 5
            }

            if rating_tag:
                for k in rating_dict:
                    if k in rating_tag['class']:
                        rating = rating_dict[k]

            # add data
            if genre and title and price and stock and rating:
                data.append({
                    'Genre' : genre,
                    'Title' : title,
                    'Price' : float(price),
                    'Stock' : int(stock),
                    'Rating' : rating
                })
            else:
                print('Data tidak ada!')
                return None
        except Exception as e:
            print(f"Extract data error : {e}")
            return None
    
    return data
    