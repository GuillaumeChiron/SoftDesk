# SoftDesk

API Django REST Framework pour le projet SoftDesk.

## Prerequis

- Python installe sur la machine
- `pip`
- Git, si vous clonez le projet depuis un depot distant

Le projet utilise Django et Django REST Framework. Les dependances sont listees dans `requirements.txt`.

## Installation locale

Placez-vous dans le dossier du projet :

```bash
cd softdesk
```

Creez un environnement virtuel :

```bash
python -m venv env
```

Activez l'environnement virtuel.

Sur Windows :

```bash
env\Scripts\activate
```

Sur macOS ou Linux :

```bash
source env/bin/activate
```

Installez les dependances :

```bash
pip install -r requirements.txt
```

## Base de donnees

Le projet utilise SQLite en local avec le fichier `db.sqlite3`.

Appliquez les migrations :

```bash
python manage.py migrate
```

Si besoin, creez un super-utilisateur pour acceder a l'administration Django :

```bash
python manage.py createsuperuser
```

## Lancement du projet

Demarrez le serveur de developpement :

```bash
python manage.py runserver
```

Le projet sera disponible a l'adresse :

```text
http://127.0.0.1:8000/
```

L'administration Django est disponible ici :

```text
http://127.0.0.1:8000/admin/
```

## URLs du projet

Les URLs principales sont declarees dans `config/urls.py`.

```text
/admin/
/api-auth/
/api/
```

### Authentification

Les routes d'authentification sont accessibles avec le prefixe `/api-auth/`.

| Methode | Endpoint | Description |
| --- | --- | --- |
| GET | `/api-auth/` | Racine du router d'authentification |
| GET | `/api-auth/user/` | Liste des utilisateurs |
| POST | `/api-auth/user/` | Creation d'un utilisateur |
| GET | `/api-auth/user/<id>/` | Detail d'un utilisateur |
| PUT | `/api-auth/user/<id>/` | Remplacement d'un utilisateur |
| PATCH | `/api-auth/user/<id>/` | Mise a jour partielle d'un utilisateur |
| DELETE | `/api-auth/user/<id>/` | Suppression d'un utilisateur |
| POST | `/api-auth/token/` | Obtention des tokens JWT `access` et `refresh` |
| POST | `/api-auth/token/refresh/` | Renouvellement du token `access` |

Exemple de corps pour obtenir un token :

```json
{
  "username": "votre_username",
  "password": "votre_mot_de_passe"
}
```

Les endpoints proteges attendent ensuite le token d'acces dans l'en-tete HTTP :

```text
Authorization: Bearer <access_token>
```

### API metier

Les routes metier sont accessibles avec le prefixe `/api/`.

| Methode | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/` | Racine du router de l'API |
| GET | `/api/project/` | Liste des projets auxquels l'utilisateur contribue |
| POST | `/api/project/` | Creation d'un projet |
| GET | `/api/project/<id>/` | Detail d'un projet |
| PUT | `/api/project/<id>/` | Remplacement d'un projet |
| PATCH | `/api/project/<id>/` | Mise a jour partielle d'un projet |
| DELETE | `/api/project/<id>/` | Suppression d'un projet |
| GET | `/api/contributor/` | Liste des contributeurs des projets accessibles |
| POST | `/api/contributor/` | Ajout d'un contributeur a un projet |
| GET | `/api/contributor/<id>/` | Detail d'un contributeur |
| PUT | `/api/contributor/<id>/` | Remplacement d'un contributeur |
| PATCH | `/api/contributor/<id>/` | Mise a jour partielle d'un contributeur |
| DELETE | `/api/contributor/<id>/` | Suppression d'un contributeur |
| GET | `/api/issue/` | Liste des issues des projets accessibles |
| POST | `/api/issue/` | Creation d'une issue |
| GET | `/api/issue/<id>/` | Detail d'une issue |
| PUT | `/api/issue/<id>/` | Remplacement d'une issue |
| PATCH | `/api/issue/<id>/` | Mise a jour partielle d'une issue |
| DELETE | `/api/issue/<id>/` | Suppression d'une issue |
| GET | `/api/comment/` | Liste des commentaires des issues accessibles |
| POST | `/api/comment/` | Creation d'un commentaire |
| GET | `/api/comment/<id>/` | Detail d'un commentaire |
| PUT | `/api/comment/<id>/` | Remplacement d'un commentaire |
| PATCH | `/api/comment/<id>/` | Mise a jour partielle d'un commentaire |
| DELETE | `/api/comment/<id>/` | Suppression d'un commentaire |

Les commentaires possedent un champ `uuid`, mais les routes de detail utilisent l'identifiant interne `<id>`.

### Champs principaux

Creation d'un utilisateur :

```json
{
  "username": "alice",
  "password": "mot_de_passe",
  "age": 18,
  "can_be_contacted": true,
  "can_data_be_shared": false
}
```

Creation d'un projet :

```json
{
  "title": "Application web",
  "description": "Description du projet",
  "type": "Back-end"
}
```

Valeurs possibles pour `type` : `Back-end`, `Front-end`, `IOS`, `Android`.

Ajout d'un contributeur :

```json
{
  "user": 2,
  "project": 1
}
```

Creation d'une issue :

```json
{
  "title": "Corriger la connexion",
  "description": "Description de l'issue",
  "tag": "Bug",
  "priority": "High",
  "status": "To do",
  "project": 1,
  "assign": 2
}
```

Valeurs possibles pour `tag` : `Bug`, `Feature`, `Task`.
Valeurs possibles pour `priority` : `Low`, `Medium`, `High`.
Valeurs possibles pour `status` : `To do`, `In progress`, `Finished`.

Creation d'un commentaire :

```json
{
  "description": "Commentaire sur l'issue",
  "issue": 1
}
```

### Permissions principales

```text
Les routes metier necessitent un utilisateur authentifie.
Les projets listes sont ceux dont l'utilisateur est contributeur.
Le createur d'un projet devient automatiquement contributeur du projet.
Seul l'auteur d'un projet peut le modifier ou le supprimer.
Seul l'auteur d'un projet peut ajouter, modifier ou supprimer ses contributeurs.
Un contributeur ne peut pas supprimer le createur du projet de la liste des contributeurs.
Seul l'auteur d'une issue ou l'auteur du projet peut modifier ou supprimer une issue.
Seul l'auteur d'un commentaire ou l'auteur du projet peut modifier ou supprimer un commentaire.
```
