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

###########################################################################################################################

import requests
from bs4 import BeautifulSoup

url = "https://www.x-rates.com/table/?from=USD&amount=1"
res = requests.get(url)
s = BeautifulSoup(res.text, "html.parser")

table = s.find("table", class_="ratesTable")
rows = table.find_all("tr")[1:6]  # берём первые 5 валют

for row in rows:
    cols = row.find_all("td")
    currency = cols[0].get_text(strip=True)
    rate = cols[1].get_text(strip=True)
    print(f"{currency}: {rate}")
