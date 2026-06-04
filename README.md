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

Les URLs principales sont declarees dans `config/urls.py` :

```text
/admin/
/api-auth/
/api/
```

Les routes d'authentification doivent etre ajoutees dans :

```text
authentication/urls.py
```

Elles seront ensuite accessibles avec le prefixe :

```text
/api-auth/
```

Les routes de l'API doivent etre ajoutees dans :

```text
api/urls.py
```

Elles seront ensuite accessibles avec le prefixe :

```text
/api/
```

Pour le moment, aucun endpoint metier n'est encore enregistre dans le router de `api/urls.py`.

## Commandes utiles

Lancer les tests :

```bash
python manage.py test
```

Verifier les migrations a creer apres modification des modeles :

```bash
python manage.py makemigrations
```

Appliquer les migrations :

```bash
python manage.py migrate
```
