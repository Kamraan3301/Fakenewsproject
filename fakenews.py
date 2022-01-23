from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import requests
from random import randint
from urllib.request import Request, urlopen


for x in range(10):
      SearchValue=randint(0,10)

def dailystar():
      for x in range(10):
          SearchValue=randint(0,10)

      req = Request("https://www.thedailystar.net/sports/football")
      html_page = urlopen(req)
      title_class=[]
      soup = BeautifulSoup(html_page, "lxml")
      news_cards= soup.findAll('div', class_='row align-justify f-card-wrapper border-bottom transition')
      for news in news_cards:
            news_name=news.h3
            for news1 in news_name:
                  news_p=news_name.a
                  for news2 in news_p:
                        news_line=news_p.get('href')
                        title_class.append(news_line)
      
      link="https://www.thedailystar.net/"+title_class[SearchValue]
      r = requests.get(link)
      soup = BeautifulSoup(r.content, 'html.parser')
      s = soup.find('div', class_='section-content margin-lr pt-20 pb-20 clearfix')


      lines = s.find_all('p')
      daily=[]

      for line in lines:
            
            daily.append(line.text)
      return daily

def abc():
      # Making a GET request
      for x in range(10):
            SearchValue=randint(0,10)

      req = Request("https://abcnews.go.com/Sports")
      html_page = urlopen(req)
      title_class=[]
      soup = BeautifulSoup(html_page, "lxml")
      course_cards= soup.findAll('section', class_='ContentRoll__Item')
      for course in course_cards:
            course_name=course.h2
            for course1 in course_name:
                  course_price=course_name.a
                  for course2 in course_price:
                        course_lame=course_price.get('href')
                        title_class.append(course_lame)
      link=title_class[SearchValue]
      r = requests.get(link)

      # Parsing the HTML
      soup = BeautifulSoup(r.content, 'html.parser')

      s = soup.find('section', class_='Article__Column Article__Column--main')


      lines = s.find_all('p')
      abcnews=[]

      for line in lines:
            abcnews.append(line.text)
      return abcnews


def GlobalCN():
      # Making a GET request
      for x in range(10):
          SearchValue=randint(1,10)
      req = Request("https://www.globaltimes.cn/world/")
      html_page = urlopen(req)
      title_class=[]
      soup = BeautifulSoup(html_page, "lxml")
      course_cards= soup.findAll('div', class_='list_img')
      for course1 in course_cards:
            course_price=course1.a
            for course2 in course_price:
                  course_lame=course_price.get('href')
                  title_class.append(course_lame)
      r = requests.get(title_class[SearchValue])


            # Parsing the HTML
      soup = BeautifulSoup(r.content, 'html.parser')

      tags = soup.find(class_="article_content")
      globalNews=tags.text
      return globalNews
