import mysql.connector
from mysql.connector import Error

class Agent_d_agenceDAO:
    """
    Classe d'acces et de gestion des agents d'agence dans la base de données DAO

    id_employe INT,
    description_role TEXT,
    salaire DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_employe),
    FOREIGN KEY (id_employe) REFERENCES Employe(id_employe)

    Herite de l'entite Employe
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port
        }

    def get_agent_d_agence_by_id(self, id_employe):
        """Récupère un agent d'agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Agent_d_agence WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_all_agents_d_agence(self):
        """Récupère tous les agents d'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM Agent_d_agence"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_salaire_agent_d_agence_by_id(self, id_employe):
        """Récupère le salaire d'un employe par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT salaire FROM Agent_d_agence WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_description_role_agent_d_agence_by_id(self, id_employe):
        """Récupère la description du rôle d'un employe par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT description_role FROM Agent_d_agence WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def create_agent_d_agence(self, id_employe, description_role, salaire):
        """Crée un agent d'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "INSERT INTO Agent_d_agence (id_employe, description_role, salaire) VALUES (%s, %s, %s)"
                    values = (id_employe, description_role, salaire)
                    cursor.execute(query, values)
                    connection.commit()
                    result = cursor.lastrowid
                    return cursor.lastrowid
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def update_agent_d_agence(self, id_employe, description_role=None, salaire=None):
        """Met à jour un agent d'agence"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "UPDATE Agent_d_agence SET description_role = COALESCE(%s, description_role), salaire = COALESCE(%s, salaire) WHERE id_employe = %s"
                    values = (description_role, salaire, id_employe)
                    cursor.execute(query, values)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        
    def delete_agent_d_agence(self, id_employe):
        """Supprime un agent d'agence par son ID"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "DELETE FROM Agent_d_agence WHERE id_employe = %s"
                    value = (id_employe,)
                    cursor.execute(query, value)
                    connection.commit()
                    return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False