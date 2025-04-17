# local_IA_summary
locally executed IA, based on whisper (OpenIA) and Mistral-8B (Mistral AI), to summarize oral meetings
This project has been developped on a Windows 11 laptop, with a Nvidia GPU, with Python 3.13.2
--- 
## Français
### Installation
Ce projet fonctionne sous Windows 11
Pour utiliser ce projet, vous devez 
- Cloner ce dépôt git (ou bien le télécharger en .zip, et l'extraire sur votre machine locale)
- Ouvrir une console Windows **cmd**
- Naviguer à l'emplacement du fichier 
'cd chemin/vers/votre/dossier'
- **Créer un environnement virtuel** dans le bon dossier avec la commande suivante (nécessite d'avoir python installé)
'python -m venv venv' 
- Activer l'environnement virtuel avec la commande suivante
'venv\Scripts\activate'
Vous devriez vois le nom de votre environnement vitruel entre parenthèses (ici, *venv*) au début de la ligne de votre console
- Télécharger les dépendances (nécessite d'avoir pip installé)
'pip install -r requirements.txt'

### Execution
Pour éxecuter ce projet, il doit avoir été correctement installé au préalable. Il suffit ensuite de 
- Naviguer à l'emplacement du fichier 
'cd chemin/vers/votre/dossier'
- Activer l'environnement virtuel avec la commande suivante
'venv\Scripts\activate'
Vous devriez vois le nom de votre environnement vitruel entre parenthèses (ici, *venv*) au début de la ligne de votre console
- Lancer le fichier python voulu
'python real_time.py'
Le script se lance, Ctrl+C pour l'arrêter, et des fichiers .txt sont automatiquement générés. 