import bs4 as bs
import urllib.request
import ssl

context = ssl._create_unverified_context()
urlPrime = 'https://www.imdb.com/chart/boxoffice'
response = urllib.request.urlopen(urlPrime, context=context).read()
soup = bs.BeautifulSoup(response, 'lxml')
tbody = soup.tbody



print("Information taken from: "+ urlPrime)
#returns for which weekend it is taking the information from
weekOf = soup.find('h4').get_text().strip()
print("\nInformation about: " + weekOf + "\n")

#finds the title of the movie
for titleBody in tbody.find_all('td', class_='titleColumn'):
    print("The movie's title is: " +titleBody.get_text().strip())


#finds the link for the title of the movie
for linkTitle in tbody.find_all('a')[::2]:
    print("https://www.imdb.com:"+linkTitle.get('href'))

#finds the weekend earnings of each movie, since it will also return the gross earning of each movie
#I made it iterate in steps of 2 as to skip the gross earning of each movie
for tdBody in tbody.find_all('td', class_ = 'ratingColumn')[::2] :
    print("This movie earned: " + tdBody.get_text().strip() + " this weekend")


#finds the gross earnings of each movie
for spanBody in tbody.find_all('span', class_ = 'secondaryInfo') :
    print("This movie's gross earning is: "+spanBody.get_text().strip())

#finds the week that the movie is on since release
for movieWeek in tbody.find_all('td', class_ = 'weeksColumn'):
    print("The movie is on: week "+ movieWeek.get_text().strip())


#used as to know why the url link was not working
#link1 ='https://www.imdb.com'+ tbody.find('td', attrs= {'class' : 'posterColumn'}).find('a').get('href')
#print(link1)


