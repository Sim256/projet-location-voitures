import mysql.connector
from mysql.connector import Error

class ClientDAO:
    """
    Classe d'acces et de gestion des clients dans la base de données DAO

    id_client INT AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telephone VARCHAR(20),
    numero_permis VARCHAR(50) NOT NULL,
    date_inscription DATE NOT NULL,
    est_anonymise BOOLEAN NOT NULL DEFAULT FALSE,
    date_desinscription DATE,
    PRIMARY KEY (id_client),
    UNIQUE (email),
    UNIQUE (numero_permis)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }

    def get_client_by_id(self, id_client):
        """Récupère un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Client WHERE id_client = %s"
                    value = (id_client,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_client_by_email(self, email):
        """Récupère l'ID d'un client par son email"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_client FROM Client WHERE email = %s"
                    value = (email,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result[0] if result else None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_client_by_numero_permis(self, numero_permis):
        """Récupère l'ID d'un client par son numéro de permis"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_client FROM Client WHERE numero_permis = %s"
                    value = (numero_permis,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_all_clients(self):
        """Récupère tous les clients"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Client"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_is_anonymise_client_by_id(self, id_client):
        """Récupère si un client est anonyme par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT est_anonymise FROM Client WHERE id_client = %s"
                    value = (id_client,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_numero_permis_client_by_id(self, id_client):
        """Récupère le numéro de permis d'un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT numero_permis FROM Client WHERE id_client = %s"
                    value = (id_client,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_client(self, nom, prenom, email, telephone, numero_permis):
        """Crée un nouveau client"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO Client (nom, prenom, email, telephone, numero_permis, date_inscription) VALUES (%s, %s, %s, %s, %s, NOW())"
                    values = (nom, prenom, email, telephone, numero_permis)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def update_client(self, id_client, nom=None, prenom=None, email=None, telephone=None, numero_permis=None):
        """Met à jour un client"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "UPDATE Client SET nom = COALESCE(%s, nom), prenom = COALESCE(%s, prenom), email = COALESCE(%s, email), telephone = COALESCE(%s, telephone), numero_permis = COALESCE(%s, numero_permis) WHERE id_client = %s"
                    values = (nom, prenom, email, telephone, numero_permis, id_client)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
            
    def desinscription_client_by_id(self, id_client):
        """Désinscrit un client en le rendant anonyme et en changant sa date de désinscription"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "UPDATE Client SET nom = 'Anonyme', prenom = 'Anonyme', email = CONCAT('anonyme_', %s, '@email.com'), telephone = NULL, numero_permis = CONCAT('anonyme_', %s), date_desinscription = NOW(), est_anonymise = TRUE WHERE id_client = %s"
                    value = (id_client, id_client, id_client)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
            
    def delete_client(self, id_client):
        """Supprime un client par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM Client WHERE id_client = %s"
                    value = (id_client,)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False