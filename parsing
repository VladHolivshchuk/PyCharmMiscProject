import requests
from bs4 import BeautifulSoup

def parsbooks(page_url, n=8):
    resp = requests.get(page_url)
    soup = BeautifulSoup(resp.text, "html.parser")
    books = soup.select("article.product_pod")
    results = []
    for book in books[:n]:

        title = book.h3.a["title"]

        price = book.select_one("p.price_color").text.strip()

        startag = book.select_one("p.star-rating")
        classes = startag["class"]

        rating = None
        for c in classes:
            if c != "star-rating":
                rating = c
        results.append({
            "title": title,
            "price": price,
            "rating": rating
        })
    return results

if __name__ == "__main__":
    url = "http://books.toscrape.com/"
    booksinfo = parsbooks(url, n=8)
    for b in booksinfo:
        print(b)
