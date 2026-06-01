from vue.interface import VueTerminal
from modele.AgenceDAO import AgenceDAO
from modele.Agent_d_agenceDAO import Agent_d_agenceDAO
from modele.CategorieVehiculeDAO import CategorieVehiculeDAO
from modele.ClientDAO import ClientDAO
from modele.ComptableDAO import ComptableDAO
from modele.EmployeDAO import EmployeDAO
from modele.FraisSupplementaireDAO import FraisSupplementaireDAO
from modele.LocationDAO import LocationDAO
from modele.PaiementDAO import PaiementDAO
from modele.VueDAO import VueDAO
from modele.ReservationDAO import ReservationDAO
from modele.VehiculeDAO import VehiculeDAO

from datetime import date
from decimal import Decimal

class Application:
    def __init__(self):
        self.vue = VueTerminal()
        self.agence_dao = AgenceDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.agent_d_agence_dao = Agent_d_agenceDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.categorie_vehicule_dao = CategorieVehiculeDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.client_dao = ClientDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.comptable_dao = ComptableDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.employe_dao = EmployeDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.frais_supplementaire_dao = FraisSupplementaireDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.location_dao = LocationDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.paiement_dao = PaiementDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.vue_dao = VueDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.reservation_dao = ReservationDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)
        self.vehicule_dao = VehiculeDAO(host='localhost', user='root', password='root123', database='location_voitures', port=3307)

    def run(self):
        """Est appeler en premier pour demarer l'app, celle ci appele la methode adequate de la vue pour afficher la page d'acceuil"""

        self.vue.display_welcome_message()
        while True:
            """
            Les differents coix possibles sont:
            0: Quitter l'application
            1: Inscription
            2: Informations personnelles
            3: Modifier les informations personnelles
            4: Désinscription
            5: Louer une voiture
            6: Rapport annuel des ventes
            """
            choise = self.vue.display_main_menu()
            
            match choise:
                case '0':
                    # Quitter l'application
                    self.vue.display_goodbye_message()
                    break
                case '1': 
                    # Inscription
                    client_data = self.vue.sing_up_client()
                    result = self.client_dao.create_client(**client_data)
                    self.vue.sign_up_validation_message(result)
                case '2':
                    # Informations personnelles
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    if not id_client:
                        self.vue.display_client_info(None)
                        continue
                    client_info = self.client_dao.get_client_by_id(id_client)
                    self.vue.display_client_info(client_info)
                case '3':
                    # Modifier les informations personnelles
                    email = self.vue.get_email_client_for_update()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    if not id_client:
                        self.vue.display_client_info(None)
                        continue

                    client_data = self.vue.sing_up_client()
                    updates = {}
                    for key, value in client_data.items():
                        if value is None:
                            updates[key] = None
                            continue
                        stripped = value.strip()
                        updates[key] = stripped if stripped != "" else None

                    if all(value is None for value in updates.values()):
                        self.vue.sign_up_validation_message(True)
                        continue

                    result = self.client_dao.update_client(id_client=id_client, **updates)
                    self.vue.sign_up_validation_message(result)
                case '4':
                    # Désinscription
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    if not id_client:
                        self.vue.display_client_info(None)
                        continue
                    result = self.client_dao.desinscription_client_by_id(id_client)
                    self.vue.is_desinscription_confirmed(result)
                case '5':
                    # Louer une voiture
                    """
                    Une location s'effectue comme suit:
                    1. le client entre son email pour verifier son identté et récupérer son ID 
                    2. le client choisit une voiture à louer parmi les voitures disponibles (pour chaque voiture on affiche toutes ses caractéristiques)
                    3. le client choisit une voiture et une date de debut et de fin de location
                    4. le client choisit le moyen de payement et procède au paiement
                    5. le client reçoit une confirmation de sa location
                    """
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    if not id_client:
                        self.vue.display_client_info(None)
                        continue
                    # Affichage des voitures disponibles (uniquement)
                    vehicules_disponibles = self.vue_dao.get_vehicules_disponibles()
                    id_vehicule = self.vue.display_available_cars_menu(vehicules_disponibles)
                    # Récupération des dates de début et de fin de location
                    date_debut, date_fin = self.vue.get_rental_dates()
                    date_debut_db = date(date_debut[0], date_debut[1], date_debut[2])
                    date_fin_db = date(date_fin[0], date_fin[1], date_fin[2])
                    # Calcule du nombre de jours
                    nb_jours = days_between(date_debut_db, date_fin_db)
                    # Prix total de la location

                    prix_journalier = self.vehicule_dao.get_tarif_journalier_vehicule_by_id(id_vehicule=id_vehicule)
                    # Erreur de typage connue 
                    prix_total = nb_jours * prix_journalier
                    self.vue.display_rental_amount(prix_total, nb_jours, prix_journalier)
                    # Récupération du moyen de paiement et le montant choisi
                    moyen_paiement, montant = self.vue.get_payment_infos()
                    # Création de la location
                    kilometrage_depart = self.vehicule_dao.get_kilometrage_actuel_vehicule_by_id(id_vehicule)
                    id_agence_depart = self.vehicule_dao.get_id_agence_vehicule_by_id(id_vehicule)
                    id_agence_retour = id_agence_depart
                    # Création de la reservation
                    id_reservation = self.reservation_dao.create_reservation(
                        date_debut_db,
                        date_fin_db,
                        'en cours',
                        id_client,
                        id_vehicule=id_vehicule,
                        id_categorie=None
                    )
                    id_location = self.location_dao.create_location(date_debut_db, date_fin_db, prix_total, 'en cours', kilometrage_depart, None, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour)
                    # Création du paiement
                    date_paiement_actuelle = date.today()
                    self.paiement_dao.create_paiement(date_paiement_actuelle, montant, moyen_paiement, 'effectue', id_location)
                    # Comfirmation
                    self.vue.display_rental_confirmation(id_location)
                case '6':
                    # Rapport annuel des ventes
                    """
                    L'obtention d'un rapport s'effectue comme suit:
                    1. le comptable entre son email pour verifier son identté et récupérer son ID
                    2. le comptable choisit l'année pour laquelle il veut obtenir le rapport annuel
                    3. le comptable reçoit le rapport annuel des ventes de l'année choisie
                    """
                    email = self.vue.get_email_member_comptabilite()
                    id_employe = self.employe_dao.get_id_employe_by_email(email)
                    if not id_employe:
                        self.vue.display_invalid_option_message()
                        continue
                    comptable = self.comptable_dao.get_comptable_by_id(id_employe)
                    if self.vue.is_comptabilite_member_valid(comptable):
                        try:
                            year = self.vue.get_year_for_sales_report()
                            year = int(year)
                            # Utilisation du rôle comptable_user pour démontrer les permissions RGPD/Sécurité
                            compta_vue_dao = VueDAO(host='localhost', user='comptable_user', password='compta123', database='location_voitures', port=3307)
                            report_mensuel = compta_vue_dao.get_chiffre_affaires_mensuel_by_annee(year)
                            report_annuel = compta_vue_dao.get_chiffre_affaires_annuel(year)
                            chiffre_annuel = report_annuel[1] if report_annuel else 0
                            self.vue.display_sales_report(chiffre_annuel, report_mensuel, year)
                        except ValueError:
                            self.vue.display_invalid_option_message()
                        except Exception as e:
                            print(f"Erreur inattendue lors de la génération du rapport : {e}")

                case '7':
                    email = self.vue.get_email_client()
                    id_client = self.client_dao.get_id_client_by_email(email)
                    if not id_client:
                        self.vue.display_invalid_option_message()
                        continue
                    
                    all_locations = self.location_dao.get_all_locations_by_id_client(id_client)
                    if not all_locations:
                        self.vue.display_locations_en_cours([])
                        continue

                    # Filtrer les locations en cours
                    locations_en_cours = [loc for loc in all_locations if loc[5] == 'en cours']
                    id_location = self.vue.display_locations_en_cours(locations_en_cours)
                    
                    if not id_location:
                        continue
                        
                    try:
                        id_location = int(id_location)
                    except ValueError:
                        self.vue.display_invalid_option_message()
                        continue
                        
                    # Vérifier que la location appartient bien à l'utilisateur et est en cours
                    loc_to_close = next((loc for loc in locations_en_cours if loc[0] == id_location), None)
                    if not loc_to_close:
                        self.vue.display_invalid_option_message()
                        continue
                        
                    date_retour, new_km = self.vue.get_retour_infos()
                    id_vehicule = loc_to_close[9]
                    
                    try:
                        # Mise à jour DB
                        res_loc = self.location_dao.update_location(id_location=id_location, date_retour_reelle=date_retour, kilometrage_retour=new_km, statut_location='terminee')
                        res_veh = self.vehicule_dao.update_vehicule(id_vehicule=id_vehicule, kilometrage_actuel=new_km, etat_vehicule='disponible')
                        
                        self.vue.display_retour_confirmation(res_loc and res_veh)
                    except Exception as e:
                        print(f"Erreur inattendue lors du retour du véhicule : {e}")

                case _:
                    self.vue.display_invalid_option_message()

def days_between(date1, date2):
    """Calcule le nombre de jours entre deux dates"""
    d1 = _coerce_date(date1)
    d2 = _coerce_date(date2)
    return abs((d2 - d1).days)

def _coerce_date(value):
    if isinstance(value, date):
        return value
    return date(value[0], value[1], value[2])