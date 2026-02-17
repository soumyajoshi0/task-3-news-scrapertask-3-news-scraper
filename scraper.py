# Task 3 - News Headlines Scraper

import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"

def get_headlines():
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        headlines = []

        for tag in soup.find_all("h2"):
            text = tag.get_text(strip=True)
            if text and len(text) > 20:
                headlines.append(text)

        return headlines

    except Exception as e:
        print("Error:", e)
        return []


def save_headlines(headlines):
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for h in headlines:
            file.write(h + "\n")


def main():
    print("Fetching headlines...")
    headlines = get_headlines()

    if headlines:
        save_headlines(headlines)
        print("Saved", len(headlines), "headlines to headlines.txt")
    else:
        print("No headlines found.")


if __name__ == "__main__":
    main()
