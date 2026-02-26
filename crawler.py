import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json

visited = set()
queue = ["https://example.com"]  # Start here
data = []  # Store extracted info

def crawl(url, max_pages=10):
    if url in visited or len(data) >= max_pages:
        return
    
    visited.add(url)
    print(f"Crawling: {url}")
    
    try:
        resp = requests.get(url, timeout=5)
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        # Extract WHAT YOU WANT (titles, prices, jobs)
        title = soup.find('title').text if soup.find('title') else "No title"
        data.append({"url": url, "title": title})
        
        # Follow links
        for link in soup.find_all('a', href=True):
            next_url = urljoin(url, link['href'])
            if urlparse(next_url).netloc == urlparse(url).netloc:
                queue.append(next_url)
                
    except:
        pass

while queue and len(data) < 10:
    crawl(queue.pop(0))

# Save data
with open('crawled_data.json', 'w') as f:
    json.dump(data, f, indent=2)

