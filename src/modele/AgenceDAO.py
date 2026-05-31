import mysql.connector
from mysql.connector import Error

class AgenceDAO:
    """
    Classe d'acces et de gestion des agences dans la base de données DAO

    id_agence INT AUTO_INCREMENT,
    nom_agence VARCHAR(100) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    code_postal VARCHAR(20) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_agence)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port # Il faut s'assurer que le port de docker est le meme 
        }

    def get_agence_by_id(self, id_agence):
        """Récupère une agence par son ID"""

        # Connexion automatique grace a l'utilisation du bloc with gerant la déconnextion
        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "SELECT * FROM Agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Récupération du resultat
                    result = cursor.fetchone()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_agences(self):
        """Récupère toutes les agences"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete
                    query = "SELECT * FROM Agence"
                    # Execution de la requete
                    cursor.execute(query)
                    # Récupération du resultat
                    result = cursor.fetchall()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_nom_agence_by_id(self, id_agence):
        """Récupère le nom d'une agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "SELECT nom_agence FROM Agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Récupération du resultat
                    result = cursor.fetchone()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_adresse_agence_by_id(self, id_agence):
        """Récupère l'adresse d'une agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "SELECT adresse FROM Agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Récupération du resultat
                    result = cursor.fetchone()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_ville_agence_by_id(self, id_agence):
        """Récupère la ville d'une agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "SELECT ville FROM Agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Récupération du resultat
                    result = cursor.fetchone()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_agences_by_ville(self, ville):
        """Récupère toutes les agences d'une ville"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "SELECT * FROM Agence WHERE ville = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (ville,)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Récupération du resultat
                    result = cursor.fetchall()
                    # Retour du resultat
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def create_agence(self, nom_agence, adresse, ville, code_postal, telephone):
        """Crée une nouvelle agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "INSERT INTO Agence (nom_agence, adresse, ville, code_postal, telephone) VALUES (%s, %s, %s, %s, %s)"
                    # Construction du tuple de parametres pour la requete
                    values = (nom_agence, adresse, ville, code_postal, telephone)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, values)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return cursor.lastrowid
        except Error as e:  
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def update_agence(self, id_agence, nom_agence=None, adresse=None, ville=None, code_postal=None, telephone=None):
        """Met à jour une agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "UPDATE Agence SET nom_agence = COALESCE(%s, nom_agence), adresse = COALESCE(%s, adresse), ville = COALESCE(%s, ville), code_postal = COALESCE(%s, code_postal), telephone = COALESCE(%s, telephone) WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    values = (nom_agence, adresse, ville, code_postal, telephone, id_agence)
                    # Execution de la requete avec les parametres
                    cursor.execute(query, values)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_agence_by_id(self, id_agence):
        """Supprime une agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Construction de la requete avec utilisation de placeholerd pour éviter les injections SQL
                    query = "DELETE FROM Agence WHERE id_agence = %s"
                    # Construction du tuple de parametres pour la requete
                    value = (id_agence,) # Il faut s'assurer que le tuple contient une virgule pour être considéré comme un tuple d'un seul élément
                    # Execution de la requete avec les parametres
                    cursor.execute(query, value)
                    # Validation de la transaction pour rendre definitif les modifications
                    connection.commit()
                    # Retour du resultat
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False