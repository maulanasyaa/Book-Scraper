# Books Scraper – Python Project

## Description
A small command-line tool that downloads book data from the demo site “https://books.toscrape.com” and stores the result in two files: data/books.csv and data/books.json.
The project is meant as a first practice in Python web-scraping, covering these topics: the requests library, HTML parsing with BeautifulSoup, splitting code into reusable modules, and writing tabular data with Pandas.

## Data that is collected
- Genre – the category of the book
- Title – the book name
- Price – price in GBP (pounds)
- Stock – how many copies are listed as available
- Rating – star rating converted to the numbers 1-5

## Result files
- data/books.csv
- data/books.json

## Folder layout

```bash
books_scraper/
│
├─ scrape_book.py main program – run this file
├─ utils/ helper modules
│ ├─ init.py
│ ├─ fetch_page.py download a page and return BeautifulSoup
│ ├─ parse_book.py extract details from each book page
│ └─ create_file.py write CSV and JSON
└─ data/ (created automatically – contains output)
```

## Prerequisites
- Python 3.10 or newer
- Third-party packages: requests, beautifulsoup4, lxml, pandas

## It is recommended to work inside a virtual environment so that dependencies stay isolated.

#### Create and activate the virtual environment (Linux / macOS)

```bash
python -m venv .venv
source .venv/bin/activate
```

#### On Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install the required packages

```bash
pip install -r requirements.txt
```

## How to run the scraper

```bash
python scrape_book.py
```

## Learning notes
- Modular code: each task (fetch, parse, write) lives in its own file, so it is easy to maintain.
- Type hints help editors or linters show mistakes earlier.
- Basic error handling with try/except keeps the script from crashing.
- Using CSS selectors in BeautifulSoup (select_one, find_all) simplifies element targeting compared with chains of find().

## License
The project is purely educational. The target website “books.toscrape.com” was created for web-scraping practice and can be accessed without special permission.
Source code is released under the MIT license.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
