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
                    query = "SELECT * FROM CategorieVehicule WHERE id_categorie = %s"
                    value = (id_categorie,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_id_categorie_by_nom(self, nom_categorie):
        """Récupère l'ID d'une catégorie de véhicule par son nom"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT id_categorie FROM CategorieVehicule WHERE nom_categorie = %s"
                    value = (nom_categorie,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
    
    def get_all_categorie_vehicules(self):
        """Récupère toutes les catégories de véhicules"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM CategorieVehicule"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_description_categorie_vehicule_by_id(self, id_categorie):
        """Récupère la description d'une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT description FROM CategorieVehicule WHERE id_categorie = %s"
                    value = (id_categorie,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_tarif_base_categorie_vehicule_by_id(self, id_categorie):
        """Récupère le tarif de base d'une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT tarif_base FROM CategorieVehicule WHERE id_categorie = %s"
                    value = (id_categorie,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_categorie_vehicule(self, nom_categorie, description, tarif_base):
        """Crée une nouvelle catégorie de véhicule"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO CategorieVehicule (nom_categorie, description, tarif_base) VALUES (%s, %s, %s)"
                    values = (nom_categorie, description, tarif_base)
                    cursor.execute(query, values)
                    connection.commit()
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_categorie_vehicule(self, id_categorie, nom_categorie=None, description=None, tarif_base=None):
        """Met à jour une catégorie de véhicule"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "UPDATE CategorieVehicule SET nom_categorie = COALESCE(%s, nom_categorie), description = COALESCE(%s, description), tarif_base = COALESCE(%s, tarif_base) WHERE id_categorie = %s"
                    values = (nom_categorie, description, tarif_base, id_categorie)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_categorie_vehicule(self, id_categorie):
        """Supprime une catégorie de véhicule par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM CategorieVehicule WHERE id_categorie = %s"
                    value = (id_categorie,)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False