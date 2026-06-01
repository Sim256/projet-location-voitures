import mysql.connector
from mysql.connector import Error

class LocationDAO:
    """
    Classe d'acces et de gestion des locations dans la base de données DAO

    id_location INT AUTO_INCREMENT,
    date_debut DATE NOT NULL,
    date_fin_prevue DATE NOT NULL,
    date_retour_reelle DATE,
    prix_total DECIMAL(10,2) NOT NULL,
    statut_location VARCHAR(50) NOT NULL,
    kilometrage_depart INT NOT NULL,
    kilometrage_retour INT,
    id_client INT NOT NULL,
    id_vehicule INT NOT NULL,
    id_reservation INT,
    id_agence_depart INT NOT NULL,
    id_agence_retour INT NOT NULL,
    PRIMARY KEY (id_location),
    UNIQUE (id_reservation),
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_vehicule) REFERENCES Vehicule(id_vehicule),
    FOREIGN KEY (id_reservation) REFERENCES Reservation(id_reservation),
    FOREIGN KEY (id_agence_depart) REFERENCES Agence(id_agence),
    FOREIGN KEY (id_agence_retour) REFERENCES Agence(id_agence)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port # Il faut s'assurer que le port de docker est le meme 
        }
        
    def get_location_by_id(self, id_location):
        """Récupère une location par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location WHERE id_location = %s"
                    value = (id_location,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations(self):
        """Récupère toutes les locations"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def get_id_location_by_id_reservation(self, id_reservation):
        """Récupère l'ID d'une location par son ID de réservation"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_location FROM Location WHERE id_reservation = %s"
                    value = (id_reservation,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_vehicule(self, id_vehicule):
        """Récupère toutes les locations d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location WHERE id_vehicule = %s"
                    value = (id_vehicule,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_client(self, id_client):
        """Récupère toutes les locations d'un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location WHERE id_client = %s"
                    value = (id_client,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_agence_depart(self, id_agence_depart):
        """Récupère toutes les locations d'une agence de départ par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location WHERE id_agence_depart = %s"
                    value = (id_agence_depart,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_id_agence_retour(self, id_agence_retour):
        """Récupère toutes les locations d'une agence de retour par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location WHERE id_agence_retour = %s"
                    value = (id_agence_retour,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_locations_by_statut(self, statut_location):
        """Récupère toutes les locations d'un statut donné"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Location WHERE statut_location = %s"
                    value = (statut_location,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_location(self, date_debut, date_fin_prevue, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour):
        """Crée une nouvelle location"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO Location (date_debut, date_fin_prevue, date_retour_reelle, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    value = (date_debut, date_fin_prevue, None, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour)
                    cursor.execute(query, value)
                    connection.commit()
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def update_location(self, id_location, date_debut=None, date_fin_prevue=None, date_retour_reelle=None, prix_total=None, statut_location=None, kilometrage_depart=None, kilometrage_retour=None, id_client=None, id_vehicule=None, id_reservation=None, id_agence_depart=None, id_agence_retour=None):
        """Met à jour une location"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requête de mise à jour
                    query = "UPDATE Location SET date_debut = COALESCE(%s, date_debut), date_fin_prevue = COALESCE(%s, date_fin_prevue), date_retour_reelle = COALESCE(%s, date_retour_reelle), prix_total = COALESCE(%s, prix_total), statut_location = COALESCE(%s, statut_location), kilometrage_depart = COALESCE(%s, kilometrage_depart), kilometrage_retour = COALESCE(%s, kilometrage_retour), id_client = COALESCE(%s, id_client), id_vehicule = COALESCE(%s, id_vehicule), id_reservation = COALESCE(%s, id_reservation), id_agence_depart = COALESCE(%s, id_agence_depart), id_agence_retour = COALESCE(%s, id_agence_retour) WHERE id_location = %s"
                    values = (date_debut, date_fin_prevue, date_retour_reelle, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour, id_location)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_location(self, id_location):
        """Supprime une location par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM Location WHERE id_location = %s"
                    value = (id_location,)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
