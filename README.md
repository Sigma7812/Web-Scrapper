# Web-Scrapper
# Multi-Site News Headlines Scraper
## Description
This Python script scrapes top news headlines from multiple news websites using `requests` and `BeautifulSoup`.   Each run generates a timestamped `.txt` file so past results are preserved.
## Features
- Scrapes multiple sites (BBC, Al Jazeera, CNN)
- Automatically saves headlines to `headlines_YYYY-MM-DD_HH-MM-SS.txt`
- Removes duplicates
- Filters out very short text
- Customizable list of news sites

## Installation
```bash
pip install requests beautifulsoup4
