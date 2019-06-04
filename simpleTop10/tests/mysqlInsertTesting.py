import pymysql
from simpleTop10.mySoupConnect import *

mydb = pymysql.connect(
    host="",
    user="",
    passwd="",
    database=""
)
mycursor = mydb.cursor()

sql1 = "Insert into movieweb (movieTitle, movieImage, moviePage, weekEarn, grossEarn, weekNum, takenWeek, takenTime) values (%s, %s, %s, %s, %s, %s, %s, %s)"
val1 = (film_Title, movie_Image, link_Title, td_Body, span_Body, movie_Week, website_taken, time_taken)
mycursor.executemany(sql1, val1)

sql2 = "Insert into movieweb(movieImage) values (%s)"
val2 = movie_Image
mycursor.executemany(sql2,val2)

sql3 = "Insert into movieweb(moviePage) values (%s)"
val3 = link_Title
mycursor.executemany(sql3,val3)

sql4 = "Insert into movieweb(weekEarn) values (%s)"
val4 = td_Body
mycursor.executemany(sql4,val4)

sql5 = "Insert into movieweb(grossEarn) values (%s)"
val5 = span_Body
mycursor.executemany(sql5,val5)

sql6 = "Insert into movieweb(weekNum) values (%s)"
val6 = movie_Week
mycursor.executemany(sql6, val6)

sql7 = "Insert into movieweb(takenWeek) values (%s)"
val7 = website_taken
mycursor.executemany(sql7, val7)

sql8 = "Insert into movieweb(takenTime) values (%s)"
val8 = time_taken
mycursor.executemany(sql8, val8)

mydb.commit()