import mysql.connector
from mysql.connector import Error

class FraisSupplementaireDAO:
    """
    Classe d'acces et de gestion des frais supplémentaires dans la base de données DAO

    id_frais INT AUTO_INCREMENT,
    type_frais VARCHAR(100) NOT NULL,
    montant DECIMAL(10,2) NOT NULL,
    description TEXT,
    date_frais DATE NOT NULL,
    id_location INT NOT NULL,
    PRIMARY KEY (id_frais),
    FOREIGN KEY (id_location) REFERENCES Location(id_location)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port # Il faut s'assurer que le port de docker est le meme 
        }

    def get_frais_supplementaires_by_id(self, id_frais):
        """Récupère les frais supplémentaires par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM FraisSupplementaire WHERE id_frais = %s"
                    value = (id_frais,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_frais_supplementaires(self):
        """Récupère tous les frais supplémentaires"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM FraisSupplementaire"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_montant_frais_supplementaires_by_id(self, id_frais):
        """Récupère le montant des frais supplémentaires par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT montant FROM FraisSupplementaire WHERE id_frais = %s"
                    value = (id_frais,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_description_frais_supplementaires_by_id(self, id_frais):
        """Récupère la description des frais supplémentaires par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT description FROM FraisSupplementaire WHERE id_frais = %s"
                    value = (id_frais,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def create_frais_supplementaires(self, type_frais, montant, description, date_frais, id_location):
        """Crée un frais supplémentaire"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO FraisSupplementaire (type_frais, montant, description, date_frais, id_location) VALUES (%s, %s, %s, %s, %s)"
                    values = (type_frais, montant, description, date_frais, id_location)
                    cursor.execute(query, values)
                    connection.commit()
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_frais_supplementaires(self, id_frais, type_frais=None, montant=None, description=None, date_frais=None, id_location=None):
        """Met à jour un frais supplémentaire"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requête de mise à jour
                    query = "UPDATE FraisSupplementaire SET type_frais = COALESCE(%s, type_frais), montant = COALESCE(%s, montant), description = COALESCE(%s, description), date_frais = COALESCE(%s, date_frais), id_location = COALESCE(%s, id_location) WHERE id_frais = %s"
                    values = (type_frais, montant, description, date_frais, id_location, id_frais)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_frais_supplementaires(self, id_frais):
        """Supprime un frais supplémentaire par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM FraisSupplementaire WHERE id_frais = %s"
                    value = (id_frais,)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False