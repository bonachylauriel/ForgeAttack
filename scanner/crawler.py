
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(url):
    visited = set()
    to_visit = [url]
    urls = []

    while to_visit:
        current_url = to_visit.pop()
        if current_url in visited:
            continue
        visited.add(current_url)
        try:
            response = requests.get(current_url, timeout=5)
            if response.status_code != 200:
                continue
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                absolute_url = urljoin(current_url, link['href'])
                if absolute_url.startswith(url):
                    to_visit.append(absolute_url)
                    urls.append(absolute_url)
        except requests.RequestException:
            continue
    return urls