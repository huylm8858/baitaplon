import requests
from bs4 import BeautifulSoup

BASE_URL = "https://laodong.vn"

def get_article_links():
    resp = requests.get(BASE_URL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    articles = soup.select('.focus-news .focus-item a')
    links = [BASE_URL + a['href'] for a in articles if 'href' in a.attrs]
    return links

def scrape_laodong_articles():
    all_articles = []
    for url in get_article_links():
        try:
            article = requests.get(url)
            soup = BeautifulSoup(article.text, 'html.parser')
            title = soup.select_one('h1').text.strip()
            desc = soup.select_one('.description').text.strip() if soup.select_one('.description') else ''
            image = soup.select_one('.main-article img')['src'] if soup.select_one('.main-article img') else ''
            content = "\n".join([p.text.strip() for p in soup.select('.main-article p')])
            all_articles.append({
                "Title": title,
                "Description": desc,
                "Image": image,
                "Content": content,
                "URL": url
            })
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return all_articles
