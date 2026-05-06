"""
implementations des fonctionnaliters demandées

Un client doit pouvoir s’inscrire auprès de l’application en remplissant un formulaire. Les informations personnelles encodées seront
enregistrées dans la base de données. Tant qu’il n’est pas inscrit,
il ne pourra procéder à aucun achat, location/. . ..

Un client inscrit peut accéder à ses informations personnelles et
les modifier s’il le souhaite.

Un client inscrit peut décider de se désinscrire définitivement de
l’application. Les données personnelles liées à ce client seront alors
définitivement supprimées de la base de données. En effet, le règlement général sur la protection des données (RGPD) oblige l’entreprise à supprimer les informations à caractère personnel du client
désinscrit. Cependant, on souhaite garder les données historiques
qu’il aura pu générer (historiques d’achats, . . .) du moment qu’il
ne soit pas possible de retrouver l’identité du client sur la base de
ces données historiques

Un client inscrit peut procéder à un achat, à une location, à une
commande, . . .

Les membres du service comptabilité (et uniquement eux) doivent
pouvoir accéder au rapport annuel des ventes. Ce dernier affichera,
pour une année introduite par l’utilisateur :
- Le chiffre d’affaires annuel de cette année
- Les chiffres d’affaires mensuels de cette même année

Exemple : un membre du service de comptabilité veut accéder au
rapport annuel de l’année 2016. Il pourra, une fois identifié, accéder à ce rapport de 2016 auprès de l’application (chiffre d’affaires
annuel + évolution mensuelle du chiffre pour cette même année).
"""

from datetime import date


class VueTerminal:
    """Classe représentant la vue en ligne de commande pour l'application de location de voitures"""
    def display_main_menu(self):
        print("=== Menu Principal ===")
        print("0. Quitter")
        print("=======================")
        print("1. Inscription")
        print("2. Informations personnelles")
        print("3. Modifier les informations personnelles")
        print("4. Désinscription")
        print("5. Louer une voiture")
        print("6. Rapport annuel des ventes")
        print("=======================")
        return input("Choisissez une option: ")
    
    def display_welcome_message(self):
        print("Bienvenue dans notre application de location de voitures!")
    
    def display_goodbye_message(self):
        print("Au revoir!")
    
    def display_invalid_option_message(self):
        print("Option invalide, veuillez réessayer.")

    # ==== Gestion des clients ====

    def sing_up_client(self):
        """Affiche le formulaire d'inscription pour un client et retourne les données saisies, ce formulaire est aussi utilisé pour la modification"""
        print("=== Inscription/Modification ===")
        print("NB: En cas de modification, laissez les champs que vous ne souhaitez pas modifier vides")
        nom = input("Nom: ")
        prenom = input("Prénom: ")
        email = input("Email (nouvel email si modification): ")
        telephone = input("Téléphone: ")
        numero_permis = input("Numéro de permis: ")

        return {
            'nom': nom,
            'prenom': prenom,
            'email': email,
            'telephone': telephone,
            'numero_permis': numero_permis
        }
    
    def sign_up_validation_message(self, valid):
        """Affiche un message de validation ou d'erreur après l'inscription ou la modification des informations personnelles d'un client"""
        if valid:
            print("Votre inscription/modification a été réussie. Merci pour votre confiance!")
        else:
            print("Votre inscription/modification a échoué. Une erreur s'est produite, veuillez réessayer.")
    
    def get_email_client(self):
        """Récupère l'email du client dans le but de récupérer ses informations personnelles ou de procéder à sa désinscription"""
        print("=== Informations personnelles ===")
        email = input("Email: ")
        return email

    def get_email_client_for_update(self):
        """Récupère l'email actuel du client avant une modification"""
        print("=== Modification des informations personnelles ===")
        email = input("Email actuel: ")
        return email
    
    def display_client_info(self, client_info):
        """Affiche les informations personnelles d'un client"""
        if client_info:
            print("=== Informations personnelles ===")
            print(f"ID: {client_info[0]}")
            print(f"Nom: {client_info[1]}")
            print(f"Prénom: {client_info[2]}")
            print(f"Email: {client_info[3]}")
            print(f"Téléphone: {client_info[4]}")
            print(f"Numéro de permis: {client_info[5]}")
            print(f"Date d'inscription: {client_info[6]}")
            print(f"Est anonyme: {client_info[7]}")
            print("===============================")
        else:
            print("Client non trouvé, vérifiez l'email saisi.")
        
    def is_desinscription_confirmed(self, valide):
        """Informe le client de confirmation de sa ésinscription"""
        if valide:
            print("Votre désinscription a été confirmée. Vos données personnelles ont été supprimées.")
        else:
            print("Votre désinscription a été annulée. Une erreur s'est produite, veuillez réessayer.")
            
    # ==== Gestion des locations ====
    
    """
    Une location s'effectue comme suit:
    1. le client entre son email pour verifier son identté et récupérer son ID (deja implémenté)
    2. le client choisit une voiture à louer parmi les voitures disponibles (pour chaque voiture on affiche toutes ses caractéristiques)
    3. le client choisit une voiture et une date de debut et de fin de location
    4. le client choisit le moyen de payement et procède au paiement
    5. le client reçoit une confirmation de sa location
    """
    
    def display_available_cars_menu(self, cars):
        """Affiche les voitures disponibles à la location avec leurs caractéristiques"""
        print("=== Voitures disponibles ===")
        for car in cars:
            print(f"ID: {car[0]}, Immatriculation: {car[1]}, Marque: {car[2]}, Modèle: {car[3]}, Année: {car[4]}, Kilométrage: {car[5]}, Etat: {car[6]}, Tarif journalier: {car[7]}, ID Catégorie: {car[8]}, ID Agence: {car[9]}")
            print("---------------------------")
        print("===========================")
        return input("Entrez l'ID de la voiture que vous souhaitez louer: ")

    def display_rental_amount(self, prix_total, nb_jours, prix_journalier):
        """Affiche le montant a payer pour la location"""
        print("=== Montant de la location ===")
        print(f"Jours: {nb_jours}")
        print(f"Tarif journalier: {prix_journalier} €")
        print(f"Montant total: {prix_total:.2f} €")
        print("==============================")
    
    def get_rental_dates(self):
        """Récupère les dates de début et de fin de location saisies par le client"""
        print("=== Dates de location ===")
        today = date.today()
        while True:
            date_debut = self._read_date_value("début")
            if date_debut < today:
                print("La date de debut doit etre aujourd'hui ou apres.")
                continue

            date_fin = self._read_date_value("fin")
            if date_fin < date_debut:
                print("La date de fin doit etre apres la date de debut.")
                continue

            return (date_debut.year, date_debut.month, date_debut.day), (date_fin.year, date_fin.month, date_fin.day)

    def _read_date_value(self, label):
        while True:
            try:
                année = int(input(f"Année de {label} (YYYY): "))
                mois = int(input(f"Mois de {label} (MM): "))
                jour = int(input(f"Jour de {label} (DD): "))
            except ValueError:
                print("Valeur invalide. Merci de saisir des nombres.")
                continue

            try:
                return date(année, mois, jour)
            except ValueError:
                print("Date invalide, veuillez reessayer.")
    
    def get_payment_infos(self):
        """Récupère le moyen de paiement choisi par le client"""
        print("=== Moyen de paiement ===")
        print("1. Carte de crédit")
        print("2. PayPal")
        print("3. Virement bancaire")
        choice = input("Choisissez un moyen de paiement: ")
        deposite = input("Entrez le montant de l'acompte: ")
        if choice == '1':
            return "Carte de crédit", deposite
        elif choice == '2':
            return "PayPal", deposite
        elif choice == '3':
            return "Virement bancaire", deposite
        else:
            print("Moyen de paiement invalide, veuillez réessayer.")
            return self.get_payment_infos()
        
    def display_rental_confirmation(self, valide):
        """Affiche la confirmation de la location au client"""
        if valide:
            print("Votre location a été confirmée. Merci pour votre confiance!")
        else:
            print("Votre location a échoué. Une erreur s'est produite, veuillez réessayer.")

    # ==== Gestion du rapport annuel des ventes ====

    def get_email_member_comptabilite(self):
        """Récupère l'email du membre du service de comptabilité pour vérifier son identité avant de lui permettre d'accéder au rapport annuel des ventes"""
        print("=== Accès au rapport annuel des ventes ===")
        email_member = input("Entrez votre email d'employe du service de comptabilité: ")
        return email_member
    
    def is_comptabilite_member_valid(self, valid):
        """Informe le membre du service de comptabilité de la validation de son identité"""
        if valid:
            print("Votre identité a été validée. Vous pouvez accéder au rapport annuel des ventes.")
            return True
        else:
            print("Votre identité n'a pas pu être validée. Veuillez vérifier votre email d'employé et réessayer.")
            return False

    def get_year_for_sales_report(self):
        """Récupère l'année pour laquelle le membre du service de comptabilité souhaite accéder au rapport annuel des ventes"""
        print("=== Rapport annuel des ventes ===")
        year = input("Entrez l'année pour laquelle vous souhaitez accéder au rapport annuel des ventes (YYYY): ")
        return year
    
    def display_sales_report(self, annual_revenue, monthly_revenues, year):
        """Affiche le rapport annuel des ventes au membre du service de comptabilité"""
        print("=== Rapport annuel des ventes de l'année", year, "===")
        print(f"Chiffre d'affaires annuel: {annual_revenue} €")
        print("Chiffres d'affaires mensuels:")
        for month, revenue in monthly_revenues.items():
            print(f"{month}: {revenue} €")
        print("===============================")

