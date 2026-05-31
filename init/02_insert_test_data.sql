USE location_voitures;

INSERT INTO Agence (nom_agence, adresse, ville, code_postal, telephone)
VALUES
('Agence Bruxelles', 'RUE de bruxelles 61', 'Bruxelles', '1000', '041234567'),
('Agence Namur', 'rue du pont de la carpe 3', 'Namur', '5000', '041234567');

INSERT INTO CategorieVehicule (nom_categorie, description, tarif_base)
VALUES
('Citadine', 'Petite voiture economique pour la ville', 35.00),
('SUV', 'Vehicule spacieux adapte aux longs trajets', 70.00),
('Utilitaire', 'Vehicule destine au transport de materiel', 55.00);

INSERT INTO Client (nom, prenom, email, telephone, numero_permis, date_inscription, est_anonymise, date_desinscription)
VALUES
('Dupont', 'Marie', 'rayanne@gmail.com', '0499001122', 'PERMIS001', '2026-03-01', FALSE, NULL),
('Martin', 'Ali', 'simon@icloud.com', '0499003344', 'PERMIS002', '2026-03-05', FALSE, NULL),
('Bernard', 'Sofia', 'mateo@outlook.com', '0499005566', 'PERMIS003', '2026-03-10', FALSE, NULL);

INSERT INTO Vehicule (immatriculation, marque, modele, annee, kilometrage_actuel, etat_vehicule, tarif_journalier, id_categorie, id_agence)
VALUES
('1-ABC-123', 'Renault', 'Clio', 2022, 25000, 'disponible', 40.00, 1, 1),
('1-DEF-456', 'Peugeot', '208', 2023, 18000, 'disponible', 45.00, 1, 1),
('1-GHI-789', 'Toyota', 'RAV4', 2021, 32000, 'loue', 75.00, 2, 2);

INSERT INTO Employe (nom, prenom, email, telephone, date_embauche, id_agence)
VALUES
('SOHAIB', 'RIFFI', 'SOHAIB.RIFFI@gmail.com', '0477001122', '2025-06-15', 1),
('ZOBIDA', 'LOUIS', 'ZOBIDA.LOUIS@gmail.com', '0477003344', '2024-09-01', 1),
('MARTIN', 'JACOM', 'MARTIN.JACOM@gmail.com', '0477005566', '2023-11-20', 2);

INSERT INTO Agent_d_agence (id_employe, description_role, salaire)
VALUES
(1, 'Employe charge de la gestion des locations en agence', 250.00),
(3, 'Employe charge de la gestion operationnelle en agence', 2400.00);

INSERT INTO Comptable (id_employe, description_role, salaire)
VALUES
(2, 'Employe ayant acces aux rapports financiers', 3200.00);

INSERT INTO Reservation (date_reservation, date_debut, date_fin_prevue, statut_reservation, id_client, id_vehicule)
VALUES
('2026-03-15', '2026-04-10', '2026-04-15', 'confirmee', 1, 1),
('2026-03-18', '2026-04-12', '2026-04-18', 'confirmee', 2, 3),
('2026-03-20', '2026-04-20', '2026-04-22', 'annulee', 3, 2);
 
INSERT INTO Location (date_debut, date_fin_prevue, date_retour_reelle, prix_total, statut_location, kilometrage_depart, kilometrage_retour, id_client, id_vehicule, id_reservation, id_agence_depart, id_agence_retour)
VALUES
('2026-04-10', '2026-04-15', '2026-04-15', 200.00, 'terminee', 25000, 25520, 1, 1, 1, 1, 1),
('2026-04-05', '2026-04-08', '2026-04-09', 135.00, 'terminee', 18000, 18310, 2, 2, NULL, 1, 1),
('2026-04-12', '2026-04-18', NULL, 450.00, 'en_cours', 32000, NULL, 2, 3, 2, 2, 2);

INSERT INTO Paiement (date_paiement, montant, moyen_paiement, statut_paiement, id_location)
VALUES
('2026-04-10', 100.00, 'carte_bancaire', 'effectue', 1),
('2026-04-15', 100.00, 'virement', 'effectue', 1),
('2026-04-05', 135.00, 'carte_bancaire', 'effectue', 2),
('2026-04-12', 200.00, 'carte_bancaire', 'en_attente', 3);

INSERT INTO FraisSupplementaire (type_frais, montant, description, date_frais, id_location)
VALUES
('retard', 25.00, 'Retard de restitution du vehicule', '2026-04-09', 2),
('depassement_km', 30.00, 'Depassement du kilometrage autorise', '2026-04-15', 1);