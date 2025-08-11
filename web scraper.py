Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# List of news sites to scrape (URL, Tag to search)
NEWS_SITES = [
    ("https://www.bbc.com/news", "h2"),
    ("https://www.aljazeera.com", "h3"),
    ("https://edition.cnn.com", "span")  # CNN uses <span> for headlines
]

# Common headers to avoid blocking
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_headlines(url, tag):
    """Fetch headlines from a given news site"""
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
...         headlines = soup.find_all(tag)
... 
...         extracted = []
...         for h in headlines:
...             text = h.get_text(strip=True)
...             if text and text not in extracted and len(text) > 10:  # Avoid duplicates and very short text
...                 extracted.append(text)
... 
...         return extracted
... 
...     except requests.RequestException as e:
...         print(f"❌ Error fetching {url}: {e}")
...         return []
... 
... def save_headlines(all_headlines):
...     """Save all headlines to a timestamped file"""
...     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
...     filename = f"headlines_{timestamp}.txt"
...     with open(filename, "w", encoding="utf-8") as file:
...         for site, headlines in all_headlines.items():
...             file.write(f"=== {site} ===\n")
...             for hl in headlines:
...                 file.write(hl + "\n")
...             file.write("\n")
...     print(f"✅ Headlines saved to {filename}")
... 
... def main():
...     all_headlines = {}
...     for site, tag in NEWS_SITES:
...         print(f"📡 Fetching from {site}...")
...         headlines = fetch_headlines(site, tag)
...         all_headlines[site] = headlines
...         print(f"   ➡ {len(headlines)} headlines found")
... 
...     save_headlines(all_headlines)
... 
... if __name__ == "__main__":
...     main()
