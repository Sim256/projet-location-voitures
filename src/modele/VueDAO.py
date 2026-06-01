import mysql.connector
from mysql.connector import Error

class VueDAO:
    """
    Classe d'acces et de gestion des vues dans la base de données DAO

    CREATE OR REPLACE VIEW VueVehiculesDisponibles AS
    SELECT
        V.id_vehicule,
        V.immatriculation,
        V.marque,
        V.modele,
        V.annee,
        V.kilometrage_actuel,
        V.etat_vehicule,
        V.tarif_journalier,
        C.nom_categorie,
        A.nom_agence,
        A.ville
    FROM Vehicule V, CategorieVehicule C, Agence A
    WHERE V.id_categorie = C.id_categorie
    AND V.id_agence = A.id_agence AND V.etat_vehicule = 'disponible';

    CREATE OR REPLACE VIEW VueChiffreAffairesMensuel AS
    SELECT
        YEAR(P.date_paiement) AS annee,
        MONTH(P.date_paiement) AS mois,
        SUM(P.montant) AS chiffre_affaires_mensuel
    FROM Paiement P WHERE 
        P.statut_paiement = 'effectue'
    GROUP BY YEAR(P.date_paiement), MONTH(P.date_paiement);

    CREATE OR REPLACE VIEW VueRapportAnnuel AS
    SELECT
        YEAR(P.date_paiement) AS annee,
        SUM(P.montant) AS chiffre_affaires_annuel
    FROM Paiement P WHERE P.statut_paiement = 'effectue'
    GROUP BY YEAR(P.date_paiement);

    Actions possibles sur les vues :
    - Récupérer les véhicules disponibles
    - Récupérer le chiffre d'affaires mensuel
    - Récupérer le chiffre d'affaires annuel
    """
    def __init__(self, host, user, password, database, port):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
            'port': port # Il faut s'assurer que le port de docker est le meme 
        }

    def get_vehicules_disponibles(self):
        """Récupère les véhicules disponibles"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM VueVehiculesDisponibles"
                    cursor.execute(query)
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None
        
    def get_chiffre_affaires_mensuel_by_annee(self, annee):
        """Récupère le chiffre d'affaires de tout les mois d'une année donnée"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM VueChiffreAffairesMensuel WHERE annee = %s"
                    cursor.execute(query, (annee,))
                    result = cursor.fetchall()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None

    def get_chiffre_affaires_annuel(self, annee):
        """Récupère le chiffre d'affaires annuel d'une année donnée"""

        try:
            with mysql.connector.connect(**self.config) as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM VueRapportAnnuel WHERE annee = %s"
                    cursor.execute(query, (annee,))
                    result = cursor.fetchone()
                    return result
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return None