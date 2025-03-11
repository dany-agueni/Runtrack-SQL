import mysql.connector


class Employe:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
    def ajouter_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (nom, prenom, salaire, id_service))
        self.conn.commit()
        print("Employé ajouté avec succès.")

    def afficher_tous_les_employes(self):
        self.cursor.execute("SELECT * FROM employe")
        for ligne in self.cursor.fetchall():
            print(ligne)

    def mettre_a_jour_salaire(self, employe_id, nouveau_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        self.cursor.execute(query, (nouveau_salaire, employe_id))
        self.conn.commit()
        print("Salaire mis à jour.")

    def supprimer_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        self.cursor.execute(query, (employe_id,))
        self.conn.commit()
        print("Employé supprimé.")

    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()

db = Employe("localhost", "root", "Danyagueni2006", "Job7")
db.ajouter_employe("Morel", "Luc", 3100, 2)
db.afficher_tous_les_employes()
db.fermer_connexion()