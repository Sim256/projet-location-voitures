import mysql.connector
from mysql.connector import Error

class EmployeDAO:
    """
    Classe d'acces et de gestion des employés dans la base de données DAO
    
    id_employe INT AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telephone VARCHAR(20),
    date_embauche DATE NOT NULL,
    id_agence INT NOT NULL,
    PRIMARY KEY (id_employe),
    UNIQUE (email),
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

    def get_employe_by_id(self, id_employe):
        """Récupère un employé par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Employe WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_employe_by_email(self, email):
        """Récupère l'ID d'un employé par son email"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_employe FROM Employe WHERE email = %s"
                    value = (email,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    if result:
                        return result[0]
                    return None
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_employes(self):
        """Récupère tous les employés"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Employe"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_employes_by_id_agence(self, id_agence):
        """Récupère tous les employés d'une agence par l'ID de l'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Employe WHERE id_agence = %s"
                    value = (id_agence,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_employes_by_id_agence(self, id_agence):
        """Récupère les ID de tous les employés d'une agence par l'ID de l'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_employe FROM Employe WHERE id_agence = %s"
                    value = (id_agence,)
                    cursor.execute(query, value)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_agence_by_id_employe(self, id_employe):
        """Récupère l'ID de l'agence d'un employé par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_agence FROM Employe WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_employe(self, nom, prenom, email, telephone, date_embauche, id_agence):
        """Crée un nouvel employé"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO Employe (nom, prenom, email, telephone, date_embauche, id_agence) VALUES (%s, %s, %s, %s, %s, %s)"
                    values = (nom, prenom, email, telephone, date_embauche, id_agence)
                    cursor.execute(query, values)
                    connection.commit()
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_employe(self, id_employe, nom=None, prenom=None, email=None, telephone=None, date_embauche=None, id_agence=None):
        """Met à jour les informations d'un employé"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "UPDATE Employe SET nom = COALESCE(%s, nom), prenom = COALESCE(%s, prenom), email = COALESCE(%s, email), telephone = COALESCE(%s, telephone), date_embauche = COALESCE(%s, date_embauche), id_agence = COALESCE(%s, id_agence) WHERE id_employe = %s"
                    values = (nom, prenom, email, telephone, date_embauche, id_agence, id_employe)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_employe(self, id_employe):
        """Supprime un employé par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM Employe WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False