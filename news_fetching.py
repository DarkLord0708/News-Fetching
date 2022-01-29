import requests
import json

# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

if __name__ == '__main__':
    url = "https://newsapi.org/v2/everything?q=tesla&from=2021-12-06&sortBy=publishedAt&apiKey=ff3ad897d91446ddb484113af3c33571"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])

