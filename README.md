# Application de Location de Voitures

Ce projet universitaire implémente une base de données MySQL et une application en ligne de commande (Python) respectant l'architecture MVC pour gérer une agence de location de véhicules.

## 🛠 Prérequis

- **Docker** (pour la base de données MySQL)
- **Python 3**

## 🚀 1. Lancer la base de données

Le dossier `init/` contient les scripts SQL (Création, Données de test, Vues, Triggers, Permissions). Docker les exécutera automatiquement au premier lancement.

Depuis la racine du projet, lancez :
```bash
docker compose up -d
```

*(Si vous souhaitez réinitialiser la base, supprimez les volumes Docker associés puis relancez cette commande).*

## 💻 2. Lancer l'application Python

1. **Installer la dépendance MySQL :**
   ```bash
   pip install -r requirements.txt
   ```
2. **Démarrer l'interface console :**
   ```bash
   python src/main.py
   ```

## 🧪 Données de test utiles (Démo)

Pour vos tests ou pour l'évaluateur, la base de données est pré-remplie :

- **Email Client** (pour louer ou rendre un véhicule) : `rayanne@gmail.com` ou `simon@icloud.com`
- **Email Comptable** (accès exclusif à l'option 6 - Rapports) : `ZOBIDA.LOUIS@gmail.com`
