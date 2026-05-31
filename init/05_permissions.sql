USE location_voitures;

CREATE USER IF NOT EXISTS 'agent_agence_user'@'%' IDENTIFIED BY 'agent123';
CREATE USER IF NOT EXISTS 'comptable_user'@'%' IDENTIFIED BY 'compta123';
CREATE USER IF NOT EXISTS 'admin_user'@'%' IDENTIFIED BY 'admin123';

GRANT SELECT, INSERT, UPDATE ON location_voitures.Client TO 'agent_agence_user'@'%';
GRANT SELECT, INSERT, UPDATE ON location_voitures.Reservation TO 'agent_agence_user'@'%';
GRANT SELECT, INSERT, UPDATE ON location_voitures.Location TO 'agent_agence_user'@'%';
GRANT SELECT ON location_voitures.Vehicule TO 'agent_agence_user'@'%';
GRANT SELECT ON location_voitures.Agence TO 'agent_agence_user'@'%';
GRANT SELECT ON location_voitures.CategorieVehicule TO 'agent_agence_user'@'%';
GRANT SELECT, INSERT ON location_voitures.FraisSupplementaire TO 'agent_agence_user'@'%';

GRANT SELECT, INSERT, UPDATE ON location_voitures.Paiement TO 'comptable_user'@'%';
GRANT SELECT, INSERT, UPDATE ON location_voitures.FraisSupplementaire TO 'comptable_user'@'%';
GRANT SELECT ON location_voitures.Location TO 'comptable_user'@'%';
GRANT SELECT ON location_voitures.Client TO 'comptable_user'@'%';
GRANT SELECT ON location_voitures.VueChiffreAffairesMensuel TO 'comptable_user'@'%';
GRANT SELECT ON location_voitures.VueRapportAnnuel TO 'comptable_user'@'%';

GRANT ALL PRIVILEGES ON location_voitures.* TO 'admin_user'@'%';

FLUSH PRIVILEGES;