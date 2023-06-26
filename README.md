# SoftDesk

Ce programme utilise le framework Django étendu par djangorestframework.
Il propose une API permettant à un éventuel frontend 
d'interragir avec les fonctionnalités du site.

## Pré-requis

- Python 3.x (développé avec Python 3.11.3)
- Django > 4.2

L'ensemble des dépendances sont consultables dans le *Pipfile* ou le fichier *requirements.txt*

## Installation

1. Clonez ce dépôt sur votre machine locale.
``` git clone https://github.com/benjaminbourdon/SoftDesk.git ```
2. Accédez au répertoire du projet. Par exemple, ```cd SoftDesk```
3. Créez un environnement virtuel.  
La documentation recommande *pipenv*. 
Si *pipenv* est déjà installé sur votre système : 
``` pipenv install ```
Alternativement, avec *venv* :
``` python3 -m venv env ```
4. Activez l'environnement virtuel :
    + Avec *pipenv* : ```pipenv shell```
    + Avec *venv* : 
        + Sur macOS et Linux : ```source env/bin/activate```
        + Sur Windows avec PowerShell : ```env\Scripts\Activate.ps1```
5. Si vous avez choisi *venv*, installez les dépendances manuellement : 
```pip install -r requirements.txt```  
Avec pipenv, les dépendances ont automatiquement été installées lors de la création de l'environnement virtuel. Vous pouvez le vérifier avec :
```pipenv graph```
6. Effectuez la création de la base de données.  
```python manage.py migrate```
7. Lancez le serveur de développement : ```python manage.py runserver```

## Utilisation 

1. Executez le serveur de développement : ```python manage.py runserver```
2. Accédez aux points d'accès de l'api ayant pour base http://localhost:8000/api/ 
dans votre navigateur ou via un utilitaire tel que Postman.
3. Pour accéder à l'espace admin, vous devez vous rendre à l'adresse : <http://localhost:8000/admin/>  

## Documentation des points d'accès (*endPoint*)

Les différents points d'accès disponibles sont repertoriés et documentés :
- sur Postman <https://documenter.getpostman.com/view/26396904/2s93z6eQ8n>
- localement via swagger/openapi : 
<http://localhost:8000/swagger-ui/> (en cours de construction)

## Structure du projet

Le projet suit la structure standard du framework Django.

- **SoftDesk** : répertoire racine du projet Django
    - **config/** : contient les fichiers du configuration principaux
    - **project_api/** : répertoire contenant l'application au sens de Django
    - **static/** : répertoire pour les fichiers statiques (CSS, etc.)
    - **templates/** : répertoires pour les templates HTML non liés à une application spécifiques
    - **manage.py** : point d'entrée pour les commandes de gestion Django