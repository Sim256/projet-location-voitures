CREATE DATABASE IF NOT EXISTS location_voitures;
USE location_voitures;

CREATE TABLE Agence (
    id_agence INT AUTO_INCREMENT,
    nom_agence VARCHAR(100) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    ville VARCHAR(100) NOT NULL,
    code_postal VARCHAR(20) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    PRIMARY KEY (id_agence)
);
CREATE TABLE CategorieVehicule (
    id_categorie INT AUTO_INCREMENT,
    nom_categorie VARCHAR(50) NOT NULL,
    description TEXT,
    tarif_base DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_categorie),
    UNIQUE (nom_categorie)
);
CREATE TABLE Client (
    id_client INT AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telephone VARCHAR(20),
    numero_permis VARCHAR(50) NOT NULL,
    date_inscription DATE NOT NULL,
    est_anonymise BOOLEAN NOT NULL DEFAULT FALSE,
    date_desinscription DATE,
    PRIMARY KEY (id_client),
    UNIQUE (email),
    UNIQUE (numero_permis)
);
CREATE TABLE Vehicule (
    id_vehicule INT AUTO_INCREMENT,
    immatriculation VARCHAR(50) NOT NULL,
    marque VARCHAR(100) NOT NULL,
    modele VARCHAR(100) NOT NULL,
    annee INT NOT NULL,
    kilometrage_actuel INT NOT NULL DEFAULT 0,
    etat_vehicule VARCHAR(50) NOT NULL,
    tarif_journalier DECIMAL(10,2) NOT NULL,
    id_categorie INT NOT NULL,
    id_agence INT NOT NULL,
    PRIMARY KEY (id_vehicule),
    UNIQUE (immatriculation),
    FOREIGN KEY (id_categorie) REFERENCES CategorieVehicule(id_categorie),
    FOREIGN KEY (id_agence) REFERENCES Agence(id_agence)
);
CREATE TABLE Reservation (
    id_reservation INT AUTO_INCREMENT,
    date_reservation DATE NOT NULL,
    date_debut DATE NOT NULL,
    date_fin_prevue DATE NOT NULL,
    statut_reservation VARCHAR(50) NOT NULL,
    id_client INT NOT NULL,
    id_vehicule INT NOT NULL,
    PRIMARY KEY (id_reservation),
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_vehicule) REFERENCES Vehicule(id_vehicule)
);
CREATE TABLE Location (
    id_location INT AUTO_INCREMENT,
    date_debut DATE NOT NULL,
    date_fin_prevue DATE NOT NULL,
    date_retour_reelle DATE,
    prix_total DECIMAL(10,2) NOT NULL,
    statut_location VARCHAR(50) NOT NULL,
    kilometrage_depart INT NOT NULL,
    kilometrage_retour INT,
    id_client INT NOT NULL,
    id_vehicule INT NOT NULL,
    id_reservation INT,
    id_agence_depart INT NOT NULL,
    id_agence_retour INT NOT NULL,
    PRIMARY KEY (id_location),
    UNIQUE (id_reservation),
    FOREIGN KEY (id_client) REFERENCES Client(id_client),
    FOREIGN KEY (id_vehicule) REFERENCES Vehicule(id_vehicule),
    FOREIGN KEY (id_reservation) REFERENCES Reservation(id_reservation),
    FOREIGN KEY (id_agence_depart) REFERENCES Agence(id_agence),
    FOREIGN KEY (id_agence_retour) REFERENCES Agence(id_agence)
);
CREATE TABLE Paiement (
    id_paiement INT AUTO_INCREMENT,
    date_paiement DATE NOT NULL,
    montant DECIMAL(10,2) NOT NULL,
    moyen_paiement VARCHAR(50) NOT NULL,
    statut_paiement VARCHAR(50) NOT NULL,
    id_location INT NOT NULL,
    PRIMARY KEY (id_paiement),
    FOREIGN KEY (id_location) REFERENCES Location(id_location)
);
CREATE TABLE FraisSupplementaire (
    id_frais INT AUTO_INCREMENT,
    type_frais VARCHAR(100) NOT NULL,
    montant DECIMAL(10,2) NOT NULL,
    description TEXT,
    date_frais DATE NOT NULL,
    id_location INT NOT NULL,
    PRIMARY KEY (id_frais),
    FOREIGN KEY (id_location) REFERENCES Location(id_location)
);
CREATE TABLE Employe (
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
);

CREATE TABLE Comptable (
    id_employe INT,
    description_role TEXT,
    salaire DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_employe),
    FOREIGN KEY (id_employe) REFERENCES Employe(id_employe)
);

CREATE TABLE Agent_d_agence (
    id_employe INT,
    description_role TEXT,
    salaire DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (id_employe),
    FOREIGN KEY (id_employe) REFERENCES Employe(id_employe)
);