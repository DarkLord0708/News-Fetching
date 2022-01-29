import requests
import json

# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

if __name__ == '__main__':
    url = "paste your api url here"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    for article in arts:
        print(article['title'])

