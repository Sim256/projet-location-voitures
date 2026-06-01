import mysql.connector
from mysql.connector import Error

class PaiementDAO:
    """
    Classe d'acces et de gestion des paiements dans la base de données DAO
    
    id_paiement INT AUTO_INCREMENT,
    date_paiement DATE NOT NULL,
    montant DECIMAL(10,2) NOT NULL,
    moyen_paiement VARCHAR(50) NOT NULL,
    statut_paiement VARCHAR(50) NOT NULL,
    id_location INT NOT NULL,
    PRIMARY KEY (id_paiement),
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

    def get_paiement_by_id(self, id_paiement):
        """Récupère un paiement par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Paiement WHERE id_paiement = %s"
                    value = (id_paiement,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_paiement_id_by_id_location(self, id_location):
        """Récupère un paiement par l'ID de la location"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_paiement FROM Paiement WHERE id_location = %s"
                    value = (id_location,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
        
    def get_all_paiements(self):
        """Récupère tous les paiements"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Paiement"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_paiement_by_id_location(self, id_location):
        """Récupère tous les paiements d'une location par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Paiement WHERE id_location = %s"
                    value = (id_location,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_statut_paiement_by_id(self, id_paiement):
        """Récupère le statut d'un paiement par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT statut_paiement FROM Paiement WHERE id_paiement = %s"
                    value = (id_paiement,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_moyen_paiement_by_id(self, id_paiement):
        """Récupère le moyen de paiement d'un paiement par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT moyen_paiement FROM Paiement WHERE id_paiement = %s"
                    value = (id_paiement,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_montant_paiement_by_id(self, id_paiement):
        """Récupère le montant d'un paiement par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT montant FROM Paiement WHERE id_paiement = %s"
                    value = (id_paiement,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_paiement(self, date_paiement, montant, moyen_paiement, statut_paiement, id_location):
        """Crée un nouveau paiement"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO Paiement (date_paiement, montant, moyen_paiement, statut_paiement, id_location) VALUES (%s, %s, %s, %s, %s)"
                    values = (date_paiement, montant, moyen_paiement, statut_paiement, id_location)
                    cursor.execute(query, values)
                    connection.commit()
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_paiement(self, id_paiement, date_paiement=None, montant=None, moyen_paiement=None, statut_paiement=None):
        """Met à jour un paiement"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "UPDATE Paiement SET date_paiement = COALESCE(%s, date_paiement), montant = COALESCE(%s, montant), moyen_paiement = COALESCE(%s, moyen_paiement), statut_paiement = COALESCE(%s, statut_paiement) WHERE id_paiement = %s"
                    values = (date_paiement, montant, moyen_paiement, statut_paiement, id_paiement)
                    cursor.execute(query, values)
                    connection.commit()
                    result = cursor.rowcount
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_paiement(self, id_paiement):
        """Supprime un paiement"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM Paiement WHERE id_paiement = %s"
                    value = (id_paiement,)
                    cursor.execute(query, value)
                    connection.commit()
                    result = cursor.rowcount
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False