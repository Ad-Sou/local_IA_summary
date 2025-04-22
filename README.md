# local_IA_summary
Locally executed IA, based on whisper (OpenIA) and Mistral-8B (Mistral AI), to summarize oral meetings.  
---
___
This project has been developped on a Windows 11 laptop, with a Nvidia GPU, with Python 3.13.2

## Français
### Prérequis 
L'utilisation de la LLM pour ce projet nécessite :<br>
1. Un compilateur C++ installé sur votre ordinateur. 
<br><code>https://visualstudio.microsoft.com/visual-cpp-build-tools/</code><br>
S'assurer de cocher :
- Compilateur C++ MSVC (ex. v14.x)
- CMake	
- Windows 11 SDK 
- Build Tools pour C++ (ex. MSBuild, nmake, etc.)<br>

2. Python (testé avec 3.13.2) <br>
3. Git (testé avec 2.49.0.windows.1) <br>

Chacune de ces installations **doit être accessible dans le Path**, dans les variables d'environnement utilisateur/système 

### Installation 
Ce projet fonctionne sous Windows 11
Pour utiliser ce projet, vous devez 
- Cloner **la branche principale (main)** de ce dépôt git (ou bien le télécharger en .zip, et l'extraire sur votre machine locale)
<br><code>git clone --branch main --single-branch https://github.com/Ad-Sou/local_IA_summary</code><br>
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