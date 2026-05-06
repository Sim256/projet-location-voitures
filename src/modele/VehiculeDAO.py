import mysql.connector
from mysql.connector import Error

class VehiculeDAO:
    """
    Classe d'acces et de gestion des véhicules dans la base de données DAO

    id_vehicule INT AUTO_INCREMENT,
    immatriculation VARCHAR(50) NOT NULL,
    marque VARCHAR(100) NOT NULL,
    modele VARCHAR(100) NOT NULL,
    annee INT NOT NULL,
    kilometrage_actuel INT NOT NULL DEFAULT 0,
    etat_vehicule VARCHAR(50) NOT NULL,
    tarif_journalier DECIMAL(10,2) NOT NULL,
    id_categorie INT NOT NULL,
    id_agence INT NOT NULL,
    PRIMARY KEY (id_vehicule),
    UNIQUE (immatriculation),
    FOREIGN KEY (id_categorie) REFERENCES CategorieVehicule(id_categorie),
    FOREIGN KEY (id_agence) REFERENCES Agence(id_agence)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port # Il faut s'assurer que le port de docker est le meme 
        }

    def get_vehicule_by_id(self, id_vehicule):
        """Récupère un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_vehicule_by_immatriculation(self, immatriculation):
        """Récupère un véhicule par son immatriculation"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE immatriculation = %s"
                    # Parametres
                    value = (immatriculation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_vehicule_by_immatriculation(self, immatriculation):
        """Récupère l'ID d'un véhicule par son immatriculation"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_vehicule FROM Vehicule WHERE immatriculation = %s"
                    # Parametres
                    value = (immatriculation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def get_all_vehicules(self):
        """Récupère tous les véhicules"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_vehicules_disponibles_by_agence(self, id_agence):
        """Récupère tous les véhicules disponibles d'une agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE id_agence = %s AND etat_vehicule = 'disponible'"
                    # Parametres
                    value = (id_agence,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_vehicules_disponibles_by_categorie(self, id_categorie):
        """Récupère tous les véhicules disponibles d'une catégorie par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE id_categorie = %s AND etat_vehicule = 'disponible'"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_vehicules_disponibles_by_modele(self, modele):
        """Récupère tous les véhicules disponibles d'un modèle donné"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE modele = %s AND etat_vehicule = 'disponible'"
                    # Parametres
                    value = (modele,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_vehicules_disponibles_by_marque(self, marque):
        """Récupère tous les véhicules disponibles d'une marque donnée"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE marque = %s AND etat_vehicule = 'disponible'"
                    # Parametres
                    value = (marque,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_vehicules_disponibles_under_tarif(self, tarif_max):
        """Récupère tous les véhicules disponibles dont le tarif journalier est inférieur ou égal à un montant donné"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE tarif_journalier <= %s AND etat_vehicule = 'disponible'"
                    # Parametres
                    value = (tarif_max,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_vehicules_disponibles_under_kilometrage(self, kilometrage_max):
        """Récupère tous les véhicules disponibles dont le kilométrage actuel est inférieur ou égal à un montant donné"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Vehicule WHERE kilometrage_actuel <= %s AND etat_vehicule = 'disponible'"
                    # Parametres
                    value = (kilometrage_max,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_etat_vehicule_by_id(self, id_vehicule):
        """Récupère l'état d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT etat_vehicule FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_tarif_journalier_vehicule_by_id(self, id_vehicule):
        """Récupère le tarif journalier d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor(dictionary=True) as cursor:
                    # Requête 
                    query = "SELECT tarif_journalier FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result["tarif_journalier"]
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_kilometrage_actuel_vehicule_by_id(self, id_vehicule):
        """Récupère le kilométrage actuel d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT kilometrage_actuel FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result[0]
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_categorie_vehicule_by_id(self, id_vehicule):
        """Récupère l'ID de la catégorie d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_categorie FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result[0]
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_agence_vehicule_by_id(self, id_vehicule):
        """Récupère l'ID de l'agence d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_agence FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result[0]
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_vehicule(self, immatriculation, marque, modele, annee, kilometrage_actuel, etat_vehicule, tarif_journalier, id_categorie, id_agence):
        """Crée un nouveau véhicule dans la base de données"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO Vehicule (immatriculation, marque, modele, annee, kilometrage_actuel, etat_vehicule, tarif_journalier, id_categorie, id_agence) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    # Parametres
                    values = (immatriculation, marque, modele, annee, kilometrage_actuel, etat_vehicule, tarif_journalier, id_categorie, id_agence)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return cursor.lastrowid 
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def update_vehicule(self, id_vehicule, immatriculation=None, marque=None, modele=None, annee=None, kilometrage_actuel=None, etat_vehicule=None, tarif_journalier=None, id_categorie=None, id_agence=None):
        """Met à jour un véhicule dans la base de données"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "UPDATE Vehicule SET immatriculation = COALESCE(%s, immatriculation), marque = COALESCE(%s, marque), modele = COALESCE(%s, modele), annee = COALESCE(%s, annee), kilometrage_actuel = COALESCE(%s, kilometrage_actuel), etat_vehicule = COALESCE(%s, etat_vehicule), tarif_journalier = COALESCE(%s, tarif_journalier), id_categorie = COALESCE(%s, id_categorie), id_agence = COALESCE(%s, id_agence) WHERE id_vehicule = %s"
                    # Parametres
                    values = (immatriculation, marque, modele, annee, kilometrage_actuel, etat_vehicule, tarif_journalier, id_categorie, id_agence, id_vehicule)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_vehicule_by_id(self, id_vehicule):
        """Supprime un véhicule de la base de données par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM Vehicule WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False