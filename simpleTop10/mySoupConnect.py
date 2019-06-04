import bs4 as bs
import urllib.request
import ssl
import time
import pandas as pd

context = ssl._create_unverified_context()
urlPrime = 'https://www.imdb.com/chart/boxoffice'
response = urllib.request.urlopen(urlPrime, context=context).read()
soup = bs.BeautifulSoup(response, 'lxml')
tbody = soup.tbody
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

film_Title = []
movie_Image = []
link_Title = []
td_Body = []
span_Body = []
movie_Week = []
time_taken = []
website_taken = []

print("Information taken from: "+ urlPrime)
#returns for which weekend it is taking the information from
weekOf = soup.find('h4').get_text().strip()
#print("\nInformation about: " + weekOf + "\n")

#finds the title of the movie
for titleBody in tbody.find_all('td', class_='titleColumn'):
    #print("The movie's title is: " +titleBody.get_text().strip())
    film_Title.append(titleBody.get_text().strip())

#finds the movie image url
for movieImage in tbody.find_all('img'):
    #print("movie image: "+ movieImage.get('src'))
    movie_Image.append( movieImage.get('src'))

#finds the link for the movie
for linkTitle in tbody.find_all('a')[::2]:
    #print("https://www.imdb.com:"+linkTitle.get('href'))
    link_Title.append("https://www.imdb.com:"+linkTitle.get('href'))

#finds the weekend earnings of each movie, since it will also return the gross earning of each movie
#I made it iterate in steps of 2 as to skip the gross earning of each movie
for tdBody in tbody.find_all('td', class_ = 'ratingColumn')[::2] :
    #print("This movie earned: " + tdBody.get_text().strip() + " this weekend")
    td_Body.append(tdBody.get_text().strip())

#finds the gross earnings of each movie
for spanBody in tbody.find_all('span', class_ = 'secondaryInfo') :
    #print("This movie's gross earning is: "+spanBody.get_text().strip())
    span_Body.append(spanBody.get_text().strip())

#finds the week that the movie is on since release
for movieWeek in tbody.find_all('td', class_ = 'weeksColumn'):
    #print("The movie is on: week "+ movieWeek.get_text().strip())
    movie_Week.append(movieWeek.get_text().strip())

for number in film_Title:
    time_taken.append(now)
    website_taken.append(weekOf)



#converts the list of lists into a single list that can be used for the mysql insert


#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Six
list_of_lists = [film_Title, movie_Image, link_Title, td_Body, span_Body, movie_Week, website_taken, time_taken]
oldArr = (list_of_lists)
size = len(oldArr[1])
newArr = []
for i in range(size):
    newArr.append([])
for i,val in enumerate(oldArr):
    for index,value in enumerate(val):
        newArr[index].append(value)

newTuple = tuple(newArr)
print (newTuple)


#print(film_Title)
#print(movie_Image)
#print(link_Title)
#print(td_Body)
#print(span_Body)
#print(movie_Week)
#print(website_taken)
#print(time_taken)


#listPD = pd.DataFrame({film_Title, movie_Image, link_Title, td_Body, span_Body, movie_Week, website_taken, time_taken})

#print(listPD)



#appends a flat list, one list after another, however i need to append column by column
#flat_list = []
#for sublist in l:
#    for item in sublist:
#        flat_list.append(item)
#print(flat_list)

#x1=[]
#x2=[]
#x3=[]
#x4=[]
#x5=[]
#x6=[]
#x7=[]
#x8=[]
#new_list=[]

#for i in range(len(film_Title)):
    #x1.append(film_Title[i])
    #x2.append(movie_Image[i])
    #x3.append(link_Title[i])
    #x4.append(td_Body[i])
    #x5.append(span_Body[i])
    #x6.append(movie_Week[i])
    #x7.append(website_taken[i])
    #x8.append(time_taken[i])

#print(x1)

#the next print is to verify that the time is properly appended to the list
#print(now)

#uncomment the next block as to make sure there are the same number of everything for the movies
#print(len(film_Title))
#print(len(movie_Image))
#print(len(link_Title))
#print(len(td_Body))
#print(len(span_Body))
#print(len(movie_Week))
#print(len(website_taken))
#print(len(time_taken))

#for mysql use the datetime format in mysql

#used as to know why the url link was not working
#link1 ='https://www.imdb.com'+ tbody.find('td', attrs= {'class' : 'posterColumn'}).find('a').get('href')
#print(link1)


