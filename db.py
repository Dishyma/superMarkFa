import mysql.connector
base = mysql.connector.connect(
    host="170.187.207.138",
    user ="dishyma",
    passwd = "Ca426391*",
)
cursor = base.cursor()



base.close()