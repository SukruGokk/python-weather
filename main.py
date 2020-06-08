# @author: SukruGokk
# WEATHER

import requests
from bs4 import BeautifulSoup as BS

country = "TR"
city = "ISTANBUL"
region = "EUR"
metric = 1 #1 = Celcius ## 2 = Fahreneit

weatherURL = "http://rss.accuweather.com/rss/liveweather_rss.asp?metric={}&locCode={}|{}||{}|"

def weather():

    # CREATES A SESSION
    with requests.Session() as ses:

        #PAGE
        r = ses.get(weatherURL.format(metric, region, country, city))

        #CONTENT            
        content = BS(r.content, features="lxml")

        #TITLE LIST
        list = content.find_all("title")

        return list

print(weather())
