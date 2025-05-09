from scraper import scrape_laodong_articles
from utils import save_to_csv
from datetime import datetime

if __name__ == "__main__":
    data = scrape_laodong_articles()
    filename = f"data/laodong_data_{datetime.now().strftime('%Y-%m-%d')}.csv"
    save_to_csv(data, filename)
