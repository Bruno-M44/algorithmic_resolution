## Extraire les livrables du github sur votre poste de travail :
	`git clone https://github.com/Bruno-M44/algorithmic_resolution`

## Se positionner dans le répertoire
	`cd algorithmic_resolution/` 

## Créer l'environnement virtuel :
	`py -3 -m venv venv`

## Activer l'environnement virtuel :
	`source env/bin/activate`(sous Windows :`C:\\{venv}\\Scripts\\activate.bat`)

## Installer les dépendances :	
	`pip install -r requirements.txt`

## Lancer le programme : 
	`python bruteforce.py`

Le programme se lance, un indicateur de progression apparaît le temps de 
l'exécution (nombre de combinaisons calculées / nombre de combinaison total).  
Une fois le programme terminé, la solution s'affiche.

## Lancer le programme :
    `python optimized.py`

Le programme se lance et analyse les 3 fichiers qu'il doit traiter. Après
chaque analyse, il affiche la meilleure combinaison.