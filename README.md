# local_IA_summary
Locally executed IA, based on whisper (OpenIA) and Mistral-8B (Mistral AI), to summarize oral meetings.  
---
___
This project has been developped on a Windows 11 laptop, with a Nvidia GPU, with Python 3.13.2

## Français
### Prérequis
Ce projet nécessite : 
- Python (testé avec 3.13.2)<br>
- Git (testé avec 2.49.0.windows.1)<br>

Ainsi que les *variables d'environnement* correspondantes ajoutées au Path 
### Installation
Ce projet fonctionne sous Windows 11
Pour utiliser ce projet, vous devez 
- Cloner ce dépôt git 
<br><code>git clone --recurse-submodules https://github.com/Ad-Sou/local_IA_summary</code><br>
(télécharger en .zip et extraire ne permet pas le téléchargement automatique de whisper-small, il faut alors le faire manuellement. Privilégiez la commande <code>git clone</code>)
- Ouvrir une console Windows **cmd**
- Naviguer à l'emplacement du fichier
<br><code>cd chemin/vers/votre/dossier</code><br>
- **Créer un environnement virtuel** dans le bon dossier avec la commande suivante (nécessite d'avoir python installé) 
<br><code>python -m venv venv</code><br> 
- Activer l'environnement virtuel avec la commande suivante
<br><code>venv\Scripts\activate</code><br>
Vous devriez vois le nom de votre environnement vitruel entre parenthèses (ici, *venv*) au début de la ligne de votre console
- Télécharger les dépendances (nécessite d'avoir pip installé)
<br><code>pip install -r requirements.txt</code><br>

### Execution
Pour exécuter ce projet, il doit avoir été correctement installé au préalable. Il suffit ensuite de 
- Naviguer à l'emplacement du fichier
<br><code>cd chemin/vers/votre/dossier</code><br>
- Activer l'environnement virtuel avec la commande suivante
<br><code>venv\Scripts\activate</code><br>
Vous devriez vois le nom de votre environnement vitruel entre parenthèses (ici, *venv*) au début de la ligne de votre console
- Lancer le fichier python voulu
<br><code>python real_time.py</code><br>
Le script se lance, Ctrl+C pour l'arrêter, et des fichiers .txt sont automatiquement générés. 