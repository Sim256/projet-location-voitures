USE location_voitures;

DELIMITER $$

CREATE TRIGGER verif_reservation_chevauchement_insert
BEFORE INSERT ON Reservation
FOR EACH ROW
BEGIN
    IF NEW.statut_reservation <> 'annulee'
       AND EXISTS (
        SELECT *
        FROM Reservation R
        WHERE R.id_vehicule = NEW.id_vehicule
          AND R.statut_reservation <> 'annulee'
          AND NEW.date_debut <= R.date_fin_prevue
          AND NEW.date_fin_prevue >= R.date_debut
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ce vehicule est deja reserve sur cette periode.';
    END IF;
END$$

CREATE TRIGGER verif_reservation_chevauchement_update
BEFORE UPDATE ON Reservation
FOR EACH ROW
BEGIN
    IF NEW.statut_reservation <> 'annulee'
       AND EXISTS (
        SELECT *
        FROM Reservation R
        WHERE R.id_vehicule = NEW.id_vehicule
          AND R.id_reservation <> NEW.id_reservation
          AND R.statut_reservation <> 'annulee'
          AND NEW.date_debut <= R.date_fin_prevue
          AND NEW.date_fin_prevue >= R.date_debut
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ce vehicule est deja reserve sur cette periode.';
    END IF;
END$$

CREATE TRIGGER verif_dates_reservation_insert
BEFORE INSERT ON Reservation
FOR EACH ROW
BEGIN
    IF NEW.date_fin_prevue < NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de fin prevue doit etre superieure ou egale a la date de debut.';
    END IF;

    IF NEW.date_reservation > NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de reservation ne peut pas etre apres la date de debut.';
    END IF;
END$$

CREATE TRIGGER verif_dates_reservation_update
BEFORE UPDATE ON Reservation
FOR EACH ROW
BEGIN
    IF NEW.date_fin_prevue < NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de fin prevue doit etre superieure ou egale a la date de debut.';
    END IF;

    IF NEW.date_reservation > NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de reservation ne peut pas etre apres la date de debut.';
    END IF;
END$$

CREATE TRIGGER verif_location_reservation_insert
BEFORE INSERT ON Location
FOR EACH ROW
BEGIN
    IF NEW.id_reservation IS NOT NULL
       AND NOT EXISTS (
        SELECT *
        FROM Reservation R
        WHERE R.id_reservation = NEW.id_reservation
          AND R.id_client = NEW.id_client
          AND R.id_vehicule = NEW.id_vehicule
          AND R.statut_reservation <> 'annulee'
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La location ne correspond pas a la reservation.';
    END IF;
END$$

CREATE TRIGGER verif_location_reservation_update
BEFORE UPDATE ON Location
FOR EACH ROW
BEGIN
    IF NEW.id_reservation IS NOT NULL
       AND NOT EXISTS (
        SELECT *
        FROM Reservation R
        WHERE R.id_reservation = NEW.id_reservation
          AND R.id_client = NEW.id_client
          AND R.id_vehicule = NEW.id_vehicule
          AND R.statut_reservation <> 'annulee'
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La location ne correspond pas a la reservation.';
    END IF;
END$$

CREATE TRIGGER verif_location_chevauchement_insert
BEFORE INSERT ON Location
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT *
        FROM Location L
        WHERE L.id_vehicule = NEW.id_vehicule
          AND (
                (
                    L.date_retour_reelle IS NOT NULL
                    AND NEW.date_debut <= L.date_retour_reelle
                    AND NEW.date_fin_prevue >= L.date_debut
                )
                OR
                (
                    L.date_retour_reelle IS NULL
                    AND NEW.date_debut <= L.date_fin_prevue
                    AND NEW.date_fin_prevue >= L.date_debut
                )
          )
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ce vehicule est deja loue sur cette periode.';
    END IF;
END$$

CREATE TRIGGER verif_location_chevauchement_update
BEFORE UPDATE ON Location
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT *
        FROM Location L
        WHERE L.id_vehicule = NEW.id_vehicule
          AND L.id_location <> NEW.id_location
          AND (
                (
                    L.date_retour_reelle IS NOT NULL
                    AND NEW.date_debut <= L.date_retour_reelle
                    AND NEW.date_fin_prevue >= L.date_debut
                )
                OR
                (
                    L.date_retour_reelle IS NULL
                    AND NEW.date_debut <= L.date_fin_prevue
                    AND NEW.date_fin_prevue >= L.date_debut
                )
          )
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Ce vehicule est deja loue sur cette periode.';
    END IF;
END$$

CREATE TRIGGER verif_dates_location_insert
BEFORE INSERT ON Location
FOR EACH ROW
BEGIN
    IF NEW.date_fin_prevue < NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de fin prevue doit etre superieure ou egale a la date de debut.';
    END IF;

    IF NEW.date_retour_reelle IS NOT NULL
       AND NEW.date_retour_reelle < NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de retour reelle ne peut pas etre anterieure a la date de debut.';
    END IF;
END$$

CREATE TRIGGER verif_dates_location_update
BEFORE UPDATE ON Location
FOR EACH ROW
BEGIN
    IF NEW.date_fin_prevue < NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de fin prevue doit etre superieure ou egale a la date de debut.';
    END IF;

    IF NEW.date_retour_reelle IS NOT NULL
       AND NEW.date_retour_reelle < NEW.date_debut THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'La date de retour reelle ne peut pas etre anterieure a la date de debut.';
    END IF;
END$$

CREATE TRIGGER verif_kilometrage_location_insert
BEFORE INSERT ON Location
FOR EACH ROW
BEGIN
    IF NEW.kilometrage_depart < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le kilometrage de depart ne peut pas etre negatif.';
    END IF;

    IF NEW.kilometrage_retour IS NOT NULL
       AND NEW.kilometrage_retour < NEW.kilometrage_depart THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le kilometrage de retour ne peut pas etre inferieur au kilometrage de depart.';
    END IF;
END$$

CREATE TRIGGER verif_kilometrage_location_update
BEFORE UPDATE ON Location
FOR EACH ROW
BEGIN
    IF NEW.kilometrage_depart < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le kilometrage de depart ne peut pas etre negatif.';
    END IF;

    IF NEW.kilometrage_retour IS NOT NULL
       AND NEW.kilometrage_retour < NEW.kilometrage_depart THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le kilometrage de retour ne peut pas etre inferieur au kilometrage de depart.';
    END IF;
END$$

CREATE TRIGGER maj_kilometrage_retour
AFTER UPDATE ON Location
FOR EACH ROW
BEGIN
    IF NEW.date_retour_reelle IS NOT NULL
       AND NEW.kilometrage_retour IS NOT NULL THEN
        UPDATE Vehicule
        SET kilometrage_actuel = NEW.kilometrage_retour
        WHERE id_vehicule = NEW.id_vehicule;
    END IF;
END$$

CREATE TRIGGER maj_etat_vehicule_insert 
AFTER INSERT ON Location
FOR EACH ROW
BEGIN
    UPDATE Vehicule
    SET etat_vehicule = 'loue'
    WHERE id_vehicule = NEW.id_vehicule;
END$$

CREATE TRIGGER maj_etat_vehicule_update
AFTER UPDATE ON Location
FOR EACH ROW
BEGIN
    IF NEW.date_retour_reelle IS NOT NULL THEN
        UPDATE Vehicule
        SET etat_vehicule = 'disponible'
        WHERE id_vehicule = NEW.id_vehicule;
    END IF;
END$$

CREATE TRIGGER maj_agence_vehicule_retour
AFTER UPDATE ON Location
FOR EACH ROW
BEGIN
    IF NEW.date_retour_reelle IS NOT NULL THEN
        UPDATE Vehicule
        SET id_agence = NEW.id_agence_retour
        WHERE id_vehicule = NEW.id_vehicule;
    END IF;
END$$

CREATE TRIGGER anonymiser_client_desinscrit
BEFORE UPDATE ON Client
FOR EACH ROW
BEGIN
    IF NEW.est_anonymise = TRUE AND OLD.est_anonymise = FALSE THEN
        SET NEW.nom = 'ANONYMISE';
        SET NEW.prenom = 'ANONYMISE';
        SET NEW.email = CONCAT('anonyme_', OLD.id_client, '@anonyme.local');
        SET NEW.telephone = NULL;
        SET NEW.numero_permis = CONCAT('ANONYME_', OLD.id_client);
    END IF;
END$$

CREATE TRIGGER verif_comptable_insert
BEFORE INSERT ON Comptable
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT *
        FROM Agent_d_agence
        WHERE id_employe = NEW.id_employe
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cet employe est deja agent d agence.';
    END IF;
END$$

CREATE TRIGGER verif_agent_insert
BEFORE INSERT ON Agent_d_agence
FOR EACH ROW
BEGIN
    IF EXISTS (
        SELECT *
        FROM Comptable
        WHERE id_employe = NEW.id_employe
    ) THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cet employe est deja comptable.';
    END IF;
END$$

CREATE TRIGGER verif_montant_paiement_insert
BEFORE INSERT ON Paiement
FOR EACH ROW
BEGIN
    IF NEW.montant <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le montant du paiement doit etre strictement positif.';
    END IF;
END$$

CREATE TRIGGER verif_montant_paiement_update
BEFORE UPDATE ON Paiement
FOR EACH ROW
BEGIN
    IF NEW.montant <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le montant du paiement doit etre strictement positif.';
    END IF;
END$$

CREATE TRIGGER verif_montant_frais_insert
BEFORE INSERT ON FraisSupplementaire
FOR EACH ROW
BEGIN
    IF NEW.montant <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le montant du frais supplementaire doit etre strictement positif.';
    END IF;
END$$

CREATE TRIGGER verif_montant_frais_update
BEFORE UPDATE ON FraisSupplementaire
FOR EACH ROW
BEGIN
    IF NEW.montant <= 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Le montant du frais supplementaire doit etre strictement positif.';
    END IF;
END$$

DELIMITER ;