import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="Danyagueni2006", database="Laplateforme")
cursor = conn.cursor()

query = "SELECT * FROM etudiants"
cursor.execute(query,)

resultats = cursor.fetchall()

for ligne in resultats:
    print(ligne)

cursor.close()
conn.close()