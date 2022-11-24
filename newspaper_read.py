import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__== '__main__':
    speak("News for today")
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=d05fe9f99ad54e909eca5bc7dd948e36"
    news = requests.get(url).text  #.text is mandatory becz request.get(url) don't give text

    # we have got the news in string format so we need to convert it into python object by jason.loads()
    news_dict = json.loads(news)
    # print(news_dict["articles"])
    arts = news_dict['articles']
    for articles in arts:
        speak(articles['title'])
        speak(articles['description'])
        speak("Moving to next news")
