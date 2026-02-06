# 🎮 WorldEdit GUI v2.0.0 - Archive complète

## 📦 Contenu de cette archive

Cette archive contient **tout ce dont vous avez besoin** pour utiliser WorldEdit GUI.

### 📂 Structure des fichiers

```
worldedit_gui/
├── 📄 main.py              # Application principale
├── 📄 commands.json        # Base de données des commandes
├── 📄 requirements.txt     # Dépendances Python
├── 📄 launch.bat          # Lanceur Windows (recommandé)
├── 📄 test_install.py     # Script de test
│
├── 📁 assets/             # Icônes des catégories
│   ├── selection.png
│   ├── blocks.png
│   ├── generation.png
│   └── ... (9 icônes au total)
│
├── 📄 history.json        # Historique (vide au départ)
├── 📄 macros.json         # Macros d'exemple
│
├── 📖 README.md           # Documentation complète
├── 📖 INSTALL.md          # Guide d'installation rapide
├── 📖 CHANGELOG.md        # Notes de version
├── 📖 LICENSE             # Licence MIT
│
└── 📄 example_script.ahk  # Exemple de script AHK
```

## ⚡ Démarrage rapide

### Windows (Recommandé)

1. **Extrayez** l'archive
2. **Double-cliquez** sur `launch.bat`
3. ✨ L'application se lance automatiquement !

Le script `launch.bat` :
- ✅ Vérifie Python
- ✅ Crée un environnement virtuel
- ✅ Installe les dépendances
- ✅ Lance l'application

### Manuel

```bash
# 1. Extraire l'archive
# 2. Ouvrir un terminal dans le dossier
# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python main.py
```

## 🔧 Prérequis

- **Python 3.8+** (obligatoire)
- **AutoHotkey** (optionnel, pour l'automatisation)
- **Windows** (recommandé)

### Installer Python

Si vous n'avez pas Python :
1. Téléchargez depuis https://www.python.org/
2. ⚠️ **IMPORTANT** : Cochez "Add Python to PATH"
3. Installez

### Installer AutoHotkey

Si vous voulez l'automatisation :
1. Téléchargez depuis https://www.autohotkey.com/
2. Installez (paramètres par défaut)
3. Relancez WorldEdit GUI

## ✅ Vérifier l'installation

Lancez le script de test :
```bash
python test_install.py
```

Ce script vérifie :
- ✅ Version de Python
- ✅ Dépendances installées
- ✅ Fichiers présents
- ✅ JSON valide
- ✅ Assets présents

## 📚 Documentation

### Documentation complète
Ouvrez **README.md** pour :
- Guide d'utilisation détaillé
- Tutoriels
- Exemples
- FAQ
- Dépannage

### Installation rapide
Consultez **INSTALL.md** pour :
- Installation en 3 étapes
- Problèmes courants
- Vérification rapide

### Historique des versions
Lisez **CHANGELOG.md** pour :
- Notes de version
- Nouveautés
- Corrections de bugs
- Fonctionnalités à venir

## 🎯 Premiers pas

1. **Lancez l'application** (via `launch.bat` ou `python main.py`)
2. **Cliquez sur une catégorie** (ex: "Sélection")
3. **Choisissez une commande** (ex: "//wand")
4. **Configurez les paramètres** si nécessaire
5. **Cliquez sur** :
   - **📋 Copier** : Copie dans le presse-papier
   - **➕ Ajouter à la file** : Ajoute à la queue
   - **▶️ Exécuter** : Lance via AutoHotkey

## 🔥 Fonctionnalités principales

### ✨ Commandes WorldEdit
- **90+ commandes** WorldEdit 1.7.10
- **9 catégories** organisées
- **Descriptions pédagogiques**
- **Paramètres configurables**

### 📋 File d'attente
- Enchaînez plusieurs commandes
- Exécution par lot
- Gestion visuelle

### 📜 Historique
- Sauvegarde automatique
- Recherche en temps réel
- Réutilisation rapide

### 🔧 Macros
- Créez vos séquences
- Import/Export JSON
- **4 macros d'exemple** incluses
- Édition complète

### ⚡ Automatisation
- Scripts AutoHotkey
- Délai configurable
- Exécution dans Minecraft

## 💡 Astuces

### Raccourcis
- **Ctrl+C** dans les champs pour copier
- **Double-clic** sur une commande de l'historique pour la copier
- **Clic-droit** pour plus d'options (à venir)

### Macros d'exemple
L'archive inclut 4 macros prêtes à l'emploi :
1. **Création sphère basique** - Sphère de pierre
2. **Construction murs maison** - Murs automatiques
3. **Nettoyage terrain** - Aplatir et nettoyer
4. **Copie et rotation** - Dupliquer et pivoter

### Personnalisation
- Éditez `commands.json` pour ajouter des commandes
- Ajoutez vos icônes dans `assets/`
- Créez vos propres macros

## 🐛 Problèmes courants

### "python n'est pas reconnu"
➜ Python n'est pas dans le PATH
- Réinstallez Python
- Cochez "Add to PATH"

### "No module named 'customtkinter'"
➜ Dépendances non installées
```bash
pip install -r requirements.txt
```

### L'application se ferme
➜ Lancez depuis un terminal pour voir l'erreur
```bash
python main.py
```

### AutoHotkey ne fonctionne pas
➜ Vérifiez le chemin dans Paramètres
- Allez dans l'onglet Paramètres
- Cliquez sur "Parcourir"
- Sélectionnez AutoHotkey.exe

## 📞 Support

Consultez la documentation complète dans **README.md**

### Sections utiles
- 🔍 **Dépannage** : Solutions aux problèmes
- ❓ **FAQ** : Questions fréquentes
- 📖 **Guide complet** : Documentation détaillée
- 🎓 **Tutoriels** : Exemples pratiques

## 🚀 Prêt à construire !

Vous avez maintenant tout ce qu'il faut pour :
- ✅ Utiliser WorldEdit facilement
- ✅ Automatiser vos builds
- ✅ Apprendre les commandes
- ✅ Créer des macros puissantes

**Bon build ! 🎮**

---

*Version 2.0.0 - Créé avec ❤️ pour la communauté Minecraft*
