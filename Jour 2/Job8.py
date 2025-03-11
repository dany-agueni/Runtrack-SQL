import mysql.connector

class Zoo:
    def __init__(self, host, user, password, database):
        """Initialisation de la connexion à la base de données"""
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            print("Connexion réussie au zoo !")
        except mysql.connector.Error as err:
            print(f"Erreur de connexion : {err}")

    def ajouter_cage(self, superficie, capacite_max):
        """Ajoute une nouvelle cage"""
        query = "INSERT INTO cage (superficie, capacite_max) VALUES (%s, %s)"
        self.cursor.execute(query, (superficie, capacite_max))
        self.conn.commit()
        print("Cage ajoutée avec succès !")

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        """Ajoute un nouvel animal"""
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        self.cursor.execute(query, (nom, race, id_cage, date_naissance, pays_origine))
        self.conn.commit()
        print("Animal ajouté avec succès !")

    def supprimer_animal(self, animal_id):
        """Supprime un animal"""
        query = "DELETE FROM animal WHERE id = %s"
        self.cursor.execute(query, (animal_id,))
        self.conn.commit()
        print("Animal supprimé avec succès !")

    def supprimer_cage(self, cage_id):
        """Supprime une cage"""
        query = "DELETE FROM cage WHERE id = %s"
        self.cursor.execute(query, (cage_id,))
        self.conn.commit()
        print("Cage supprimée avec succès !")

    def afficher_animaux(self):
        """Affiche tous les animaux du zoo"""
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        print("\nListe des animaux :")
        for animal in resultats:
            print(animal)

    def afficher_animaux_par_cage(self):
        """Affiche les animaux présents dans chaque cage"""
        query = """
            SELECT animal.nom, animal.race, cage.id AS cage_id
            FROM animal
            LEFT JOIN cage ON animal.id_cage = cage.id
            ORDER BY cage.id;
        """
        self.cursor.execute(query)
        resultats = self.cursor.fetchall()
        print("\nAnimaux dans les cages :")
        for animal in resultats:
            print(f"Cage {animal[2]} : {animal[0]} ({animal[1]})")

    def calculer_superficie_totale(self):
        """Calcule la superficie totale de toutes les cages"""
        query = "SELECT SUM(superficie) FROM cage"
        self.cursor.execute(query)
        resultat = self.cursor.fetchone()[0]
        print(f"\nSuperficie totale du zoo : {resultat} m²")

    def fermer_connexion(self):
        """Ferme la connexion à la base de données"""
        self.cursor.close()
        self.conn.close()
        print("Connexion fermée.")

zoo = Zoo("localhost", "root", "Danyagueni2006", "zoo")

zoo.ajouter_cage(50, 10)
zoo.ajouter_cage(75, 15)
zoo.ajouter_animal("Leo", "Lion", 1, "2018-05-10", "Afrique")
zoo.ajouter_animal("Mia", "Tigre", 2, "2017-08-15", "Inde")
zoo.afficher_animaux()
zoo.afficher_animaux_par_cage()
zoo.calculer_superficie_totale()

zoo.fermer_connexion()

