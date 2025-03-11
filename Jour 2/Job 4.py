import mysql.connector
conn = mysql.connector.connect(host="localhost",user="root",password="Danyagueni2006", database="Laplateforme")
cursor = conn.cursor()

query = "SELECT nom, capacite FROM salle"
cursor.execute(query)
resultats = cursor.fetchall()

print("Liste des salles :")
for nom, capacite in resultats:
    print(f"Nom : {nom}, Capacité : {capacite}")

query = "SELECT SUM(superficie) FROM etage"
cursor.execute(query)
resultat = cursor.fetchone()[0]
print(f"La superficie de La Plateforme est de {resultat} m2")

query = "SELECT SUM(capacite) FROM salle"
cursor.execute(query)
resultat = cursor.fetchone()[0]
print(f"La capacité de toutes les salles est de : {resultat}")

cursor.close()
conn.close()