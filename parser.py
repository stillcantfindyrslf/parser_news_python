import requests
import json
from bs4 import BeautifulSoup


def parser_news():
    with open("data_file.json") as file:
        news_dict = json.load(file)

    headers = {
       "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
    }
    url = "https://otakumode.com/news/anime"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    articles_cards = soup.find_all("article", class_="p-article p-article-list__item c-hit")

    new_news_dict = {}
    for article in articles_cards:
        article_url = f'https://otakumode.com{article.find("a", class_="inherit").get("href")}'
        article_id = article_url.split("/")[-1]
        article_id = article_id[:-4]

        if article_id in news_dict:
            continue
        else:
            article_title = article.find("h3", class_="p-article__title").text.strip()

            news_dict[article_id] = {
                "article_title": article_title,
                "article_url": article_url,
            }

            new_news_dict[article_id] = {
                "article_title": article_title,
                "article_url": article_url,
            }

    with open("data_file.json", "w") as file:
        json.dump(news_dict, file, indent=2, ensure_ascii=False)

    return new_news_dict

def main():
    #print(parser_news())
    parser_news()


if __name__ == '__main__':
    main()