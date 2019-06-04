import pymysql


mydb = pymysql.connect(
    host="",
    user="",
    passwd="",
    database=""
)

mycursor= mydb.cursor()

mycursor.execute("Create table movieWeb(id INT AUTO_INCREMENT PRIMARY KEY, movieTitle varchar(255), movieImage varchar (255), moviePage varchar (255), weekEarn varchar (255), grossEarn varchar(255), weekNum int(5), takenWeek varchar (255), takenTime DATETIME)")

mydb.commit()