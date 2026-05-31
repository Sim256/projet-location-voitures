import mysql.connector
from mysql.connector import Error

from datetime import datetime

class ReservationDAO:
    """
    Classe d'acces et de gestion des réservations dans la base de données DAO

    id_reservation INT AUTO_INCREMENT,
    date_reservation DATE NOT NULL,
    date_debut DATE NOT NULL,
    date_fin_prevue DATE NOT NULL,
    statut_reservation VARCHAR(50) NOT NULL,
    id_client INT NOT NULL,
    id_vehicule INT,
    id_categorie INT,
    PRIMARY KEY (id_reservation),
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_vehicule) REFERENCES Vehicule(id_vehicule),
    FOREIGN KEY (id_categorie) REFERENCES CategorieVehicule(id_categorie)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port # Il faut s'assurer que le port de docker est le meme
        }

    def get_reservation_by_id(self, id_reservation):
        """Récupère une réservation par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE id_reservation = %s"
                    # Parametres
                    value = (id_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_reservations(self):
        """Récupère toutes les réservations"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_statut_reservation_by_id(self, id_reservation):
        """Récupère le statut d'une réservation par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT statut_reservation FROM Reservation WHERE id_reservation = %s"
                    # Parametres
                    value = (id_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_dates_reservation_by_id(self, id_reservation):
        """Récupère les dates d'une réservation par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT date_reservation, date_debut, date_fin_prevue FROM Reservation WHERE id_reservation = %s"
                    # Parametres
                    value = (id_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_client_id_vehicule_id_categorie_by_id_reservation(self, id_reservation):
        """Récupère l'ID du client, de la catégorie et du véhicule d'une réservation par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_client, id_vehicule, id_categorie FROM Reservation WHERE id_reservation = %s"
                    # Parametres
                    value = (id_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_reservations_by_id_client(self, id_client):
        """Récupère toutes les réservations d'un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE id_client = %s"
                    # Parametres
                    value = (id_client,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_reservations_by_id_vehicule(self, id_vehicule):
        """Récupère toutes les réservations d'un véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE id_vehicule = %s"
                    # Parametres
                    value = (id_vehicule,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_reservations_by_id_categorie(self, id_categorie):
        """Récupère toutes les réservations d'une catégorie par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE id_categorie = %s"
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
    
    def get_reservations_by_statut(self, statut_reservation):
        """Récupère toutes les réservations d'un statut donné"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE statut_reservation = %s"
                    # Parametres
                    value = (statut_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_reservations_by_date_debut(self, date_debut):
        """Récupère toutes les réservations d'une date de début donnée"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE date_debut = %s"
                    # Parametres
                    value = (date_debut,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_reservations_by_date_fin_prevue(self, date_fin_prevue):
        """Récupère toutes les réservations d'une date de fin prévue donnée"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE date_fin_prevue = %s"
                    # Parametres
                    value = (date_fin_prevue,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None 
        
    def get_reservations_by_date_reservation(self, date_reservation):
        """Récupère toutes les réservations d'une date de réservation donnée"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM Reservation WHERE date_reservation = %s"
                    # Parametres
                    value = (date_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_reservation(self, date_debut, date_fin_prevue, statut_reservation, id_client, id_vehicule=None, id_categorie=None):
        """Crée une nouvelle réservation"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO Reservation (date_reservation, date_debut, date_fin_prevue, statut_reservation, id_client, id_vehicule) VALUES (%s, %s, %s, %s, %s, %s)"
                    # Parametres
                    values = (datetime.now().strftime('%Y-%m-%d'), date_debut, date_fin_prevue, statut_reservation, id_client, id_vehicule)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour de l'ID de la réservation créée
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_reservation(self, id_reservation, date_reservation=None, date_debut=None, date_fin_prevue=None, statut_reservation=None, id_client=None, id_vehicule=None, id_categorie=None):
        """Met à jour une réservation"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete de mise à jour dynamique en fonction des paramètres fournis
                    query = "UPDATE Reservation SET date_reservation = COALESCE(%s, date_reservation), date_debut = COALESCE(%s, date_debut), date_fin_prevue = COALESCE(%s, date_fin_prevue), statut_reservation = COALESCE(%s, statut_reservation), id_client = COALESCE(%s, id_client), id_vehicule = COALESCE(%s, id_vehicule) WHERE id_reservation = %s"
                    # Parametres
                    values = (date_reservation, date_debut, date_fin_prevue, statut_reservation, id_client, id_vehicule, id_reservation)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_reservation(self, id_reservation):
        """Supprime une réservation par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM Reservation WHERE id_reservation = %s"
                    # Parametres
                    value = (id_reservation,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Resultat
                    result = cursor.rowcount
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False