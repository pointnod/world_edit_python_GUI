# ⚡ Guide d'installation rapide

## 🚀 Installation en 3 étapes

### Étape 1 : Vérifier Python
Ouvrez un terminal et tapez :
```bash
python --version
```
Vous devez avoir **Python 3.8 ou supérieur**.

Si Python n'est pas installé :
- Téléchargez depuis https://www.python.org/
- ⚠️ **IMPORTANT** : Cochez "Add Python to PATH" pendant l'installation !

### Étape 2 : Installer les dépendances
Dans le dossier de l'application, ouvrez un terminal et tapez :
```bash
pip install -r requirements.txt
```

### Étape 3 : Lancer l'application

**Windows** : Double-cliquez sur `launch.bat`

**Ou manuellement** :
```bash
python main.py
```

## 🔧 Installation AutoHotkey (optionnel)

Pour l'automatisation des commandes :

1. Téléchargez : https://www.autohotkey.com/
2. Installez avec les paramètres par défaut
3. Relancez WorldEdit GUI
4. Allez dans Paramètres et vérifiez le chemin AHK

## ✅ Vérification

L'application devrait se lancer avec :
- Une fenêtre sombre et moderne
- Des catégories sur la gauche
- Un panneau central vide (normal au démarrage)
- Une file d'attente à droite

## ❌ Problèmes courants

### "python n'est pas reconnu..."
➜ Python n'est pas dans le PATH. Réinstallez Python en cochant "Add to PATH"

### "No module named 'customtkinter'"
➜ Les dépendances ne sont pas installées :
```bash
pip install -r requirements.txt
```

### L'application se ferme immédiatement
➜ Lancez depuis un terminal pour voir les erreurs :
```bash
python main.py
```

## 📞 Besoin d'aide ?

Consultez le **README.md** complet pour plus d'informations !

---

**Bon build ! 🎮**
