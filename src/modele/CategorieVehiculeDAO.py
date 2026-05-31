import mysql.connector
from mysql.connector import Error

class CategorieVehiculeDAO:
    """
    Classe d'acces et de gestion des catégories de véhicules dans la base de données DAO

    id_categorie INT AUTO_INCREMENT,
    nom_categorie VARCHAR(50) NOT NULL,
    description TEXT,
    tarif_base DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_categorie),
    UNIQUE (nom_categorie)
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }
    
    def get_categorie_vehicule_by_id(self, id_categorie):
        """Récupère une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM CategorieVehicule WHERE id_categorie = %s"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_categorie_by_nom(self, nom_categorie):
        """Récupère l'ID d'une catégorie de véhicule par son nom"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT id_categorie FROM CategorieVehicule WHERE nom_categorie = %s"
                    # Parametres
                    value = (nom_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def get_all_categorie_vehicules(self):
        """Récupère toutes les catégories de véhicules"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT * FROM CategorieVehicule"
                    # Execution 
                    cursor.execute(query)
                    # Resultat
                    result = cursor.fetchall()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_description_categorie_vehicule_by_id(self, id_categorie):
        """Récupère la description d'une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT description FROM CategorieVehicule WHERE id_categorie = %s"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_tarif_base_categorie_vehicule_by_id(self, id_categorie):
        """Récupère le tarif de base d'une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "SELECT tarif_base FROM CategorieVehicule WHERE id_categorie = %s"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Resultat
                    result = cursor.fetchone()
                    # Retour
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_categorie_vehicule(self, nom_categorie, description, tarif_base):
        """Crée une nouvelle catégorie de véhicule"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "INSERT INTO CategorieVehicule (nom_categorie, description, tarif_base) VALUES (%s, %s, %s)"
                    # Parametres
                    values = (nom_categorie, description, tarif_base)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_categorie_vehicule(self, id_categorie, nom_categorie=None, description=None, tarif_base=None):
        """Met à jour une catégorie de véhicule"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "UPDATE CategorieVehicule SET nom_categorie = COALESCE(%s, nom_categorie), description = COALESCE(%s, description), tarif_base = COALESCE(%s, tarif_base) WHERE id_categorie = %s"
                    # Parametres
                    values = (nom_categorie, description, tarif_base, id_categorie)
                    # Execution 
                    cursor.execute(query, values)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_categorie_vehicule(self, id_categorie):
        """Supprime une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    # Requête 
                    query = "DELETE FROM CategorieVehicule WHERE id_categorie = %s"
                    # Parametres
                    value = (id_categorie,)
                    # Execution 
                    cursor.execute(query, value)
                    # Commit pour sauvegarder les changements
                    connection.commit()
                    # Retour
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False