# 🎮 WorldEdit GUI v2.0.0

Interface graphique moderne et intuitive pour WorldEdit 1.7.10 sur Minecraft.

![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 📋 Table des matières

- [Présentation](#présentation)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Configuration](#configuration)
- [Fonctionnalités avancées](#fonctionnalités-avancées)
- [Dépannage](#dépannage)
- [FAQ](#faq)

## 🎯 Présentation

WorldEdit GUI est un outil graphique complet qui facilite l'utilisation des commandes WorldEdit pour Minecraft 1.7.10. Que vous soyez débutant ou utilisateur avancé, cet outil vous permet de :

- ✨ Découvrir et apprendre toutes les commandes WorldEdit
- 🚀 Exécuter des commandes rapidement avec une interface intuitive
- 📦 Créer et gérer des macros pour automatiser vos tâches répétitives
- 📜 Conserver un historique complet de vos commandes
- ⚡ Automatiser l'exécution via AutoHotkey

## ✨ Fonctionnalités

### Interface utilisateur
- **Interface moderne** : Design sombre et épuré avec CustomTkinter
- **Catégorisation intelligente** : Commandes organisées par fonction
- **Descriptions pédagogiques** : Chaque commande est documentée
- **Paramètres dynamiques** : Configuration visuelle de chaque paramètre

### Gestion des commandes
- **Toutes les commandes WorldEdit 1.7.10** : Accès complet à l'API
- **File d'attente** : Enchaînez plusieurs commandes
- **Copie rapide** : Presse-papier intégré
- **Validation des paramètres** : Aide à la saisie avec suggestions

### Automatisation
- **Scripts AutoHotkey** : Exécution automatique dans Minecraft
- **Délai configurable** : Évitez les erreurs de spam
- **Mode batch** : Exécutez des séquences complexes

### Historique
- **Sauvegarde automatique** : Toutes vos commandes sont enregistrées
- **Recherche et filtrage** : Retrouvez rapidement une commande
- **Réutilisation rapide** : Un clic pour rajouter à la file
- **Horodatage** : Suivez votre activité

### Macros
- **Création illimitée** : Enregistrez vos séquences favorites
- **Import/Export** : Partagez vos macros en JSON
- **Édition complète** : Modifiez vos macros à tout moment
- **Exécution rapide** : Lancez vos macros en un clic

## 💻 Installation

### Prérequis

- **Python 3.8 ou supérieur**
- **Windows** (pour l'automatisation AutoHotkey)
- **AutoHotkey** (optionnel, pour l'automatisation)

### Installation rapide

1. **Téléchargez le fichier ZIP** et extrayez-le
2. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
3. **Lancez l'application** :
   ```bash
   python main.py
   ```

### Installation d'AutoHotkey (optionnel)

Pour utiliser l'automatisation :

1. Téléchargez AutoHotkey : https://www.autohotkey.com/
2. Installez-le (installation par défaut)
3. Redémarrez WorldEdit GUI

## 🚀 Utilisation

### Lancement

```bash
python main.py
```

### Interface principale

L'interface est divisée en 4 zones :

1. **Panneau gauche** : Catégories de commandes
2. **Panneau central** : Commandes et paramètres
3. **Panneau droit** : File d'attente et actions
4. **Panneau inférieur** : Onglets (Historique, Macros, Paramètres)

### Workflow de base

#### 1. Sélectionner une catégorie
Cliquez sur une catégorie dans le panneau gauche (ex: "Sélection", "Manipulation de blocs")

#### 2. Configurer une commande
- Lisez la description
- Cliquez sur ℹ️ pour plus de détails
- Remplissez les paramètres si nécessaire

#### 3. Actions disponibles
- **➕ Ajouter à la file** : Ajoute la commande à la queue
- **📋 Copier** : Copie la commande dans le presse-papier
- **▶️ Exécuter** : Exécute immédiatement via AHK

#### 4. Gérer la file d'attente
- Visualisez toutes les commandes en attente
- Retirez les commandes avec ❌
- **📋 Copier tout** : Copie toute la file
- **▶️ Exécuter (AHK)** : Lance l'exécution automatique
- **🗑️ Vider la file** : Efface tout

### Exemple pratique

**Objectif** : Créer une sphère de pierre de rayon 10

1. Cliquez sur "Génération" dans les catégories
2. Trouvez la commande "//sphere"
3. Dans le paramètre "bloc", tapez : `stone`
4. Dans le paramètre "rayon", tapez : `10`
5. Cliquez sur **📋 Copier** ou **▶️ Exécuter**
6. La commande `//sphere stone 10` est prête !

## ⚙️ Configuration

### Paramètres de base

Accédez à l'onglet **⚙️ Paramètres** :

- **Délai entre commandes** : 50-1000ms (défaut: 100ms)
- **Chemin AutoHotkey** : Sélectionnez votre installation AHK

### Fichiers de configuration

Tous les fichiers sont dans le dossier de l'application :

- `commands.json` : Définitions des commandes
- `history.json` : Historique (auto-généré)
- `macros.json` : Vos macros (auto-généré)
- `assets/` : Icônes des catégories

## 🔧 Fonctionnalités avancées

### Création de macros

Les macros permettent d'enregistrer des séquences de commandes réutilisables.

**Exemple** : Macro pour créer une maison basique

1. Allez dans l'onglet **🔧 Macros**
2. Cliquez sur **➕ Nouvelle macro**
3. Nom : `Maison basique`
4. Description : `Crée les murs et le toit d'une maison`
5. Commandes :
   ```
   //pos1
   //pos2
   //walls stone
   //expand 5 up
   //set air
   ```
6. **💾 Sauvegarder**

Votre macro est prête ! Vous pouvez :
- **▶️** Exécuter directement
- **➕** Ajouter à la file d'attente
- **✏️** Éditer
- **❌** Supprimer

### Import/Export de macros

**Exporter** vos macros :
1. Onglet Macros → **💾 Exporter**
2. Choisissez l'emplacement
3. Fichier JSON créé

**Importer** des macros :
1. Onglet Macros → **📂 Importer**
2. Sélectionnez un fichier JSON
3. Les macros sont fusionnées

### Historique avancé

**Rechercher** dans l'historique :
- Tapez dans le champ de recherche
- Filtrage en temps réel
- Cherchez par commande ou mot-clé

**Réutiliser** une commande :
- **📋** Copier dans le presse-papier
- **➕** Ajouter à la file d'attente

### Personnalisation

#### Ajouter de nouvelles commandes

Éditez `commands.json` :

```json
{
  "ma_categorie": {
    "name": "Ma Catégorie",
    "icon": "custom.png",
    "commands": [
      {
        "name": "//macommande",
        "description": "Description de ma commande",
        "syntax": "//macommande <param>",
        "params": [
          {
            "name": "param",
            "type": "text",
            "default": "valeur",
            "required": true
          }
        ]
      }
    ]
  }
}
```

#### Types de paramètres

- `text` : Champ texte libre
- `number` : Valeur numérique
- `choice` : Menu déroulant avec options

## 🔍 Dépannage

### L'application ne se lance pas

**Problème** : Erreur au lancement
**Solution** :
```bash
# Réinstallez les dépendances
pip install --upgrade -r requirements.txt

# Vérifiez votre version Python
python --version  # Doit être 3.8+
```

### AutoHotkey ne fonctionne pas

**Problème** : Les commandes ne s'exécutent pas automatiquement
**Solutions** :
1. Vérifiez qu'AutoHotkey est installé
2. Dans Paramètres, cliquez sur **📁 Parcourir**
3. Sélectionnez `AutoHotkey.exe` (généralement dans `C:\Program Files\AutoHotkey\`)
4. Assurez-vous que Minecraft est au premier plan

### Les icônes ne s'affichent pas

**Problème** : Pas d'icônes dans les catégories
**Solution** : Créez le dossier `assets/` et ajoutez vos icônes PNG

### Historique trop volumineux

**Problème** : L'historique ralentit l'application
**Solution** : 
1. Onglet Historique
2. **🗑️ Effacer l'historique**
3. L'historique est limité à 1000 entrées automatiquement

## ❓ FAQ

### Puis-je utiliser cet outil sur Mac/Linux ?

L'interface fonctionne sur tous les OS, mais l'automatisation AutoHotkey est Windows uniquement. Sur Mac/Linux, vous pouvez copier les commandes dans le presse-papier.

### L'outil modifie-t-il Minecraft ?

Non, l'outil génère simplement des commandes texte. Il n'interagit pas directement avec Minecraft.

### Puis-je ajouter mes propres commandes ?

Oui ! Éditez le fichier `commands.json` pour ajouter de nouvelles commandes et catégories.

### Les macros sont-elles sauvegardées ?

Oui, automatiquement dans `macros.json`. Vous pouvez aussi les exporter manuellement.

### Comment partager mes macros ?

Exportez-les en JSON depuis l'onglet Macros, puis partagez le fichier. Les autres utilisateurs pourront les importer.

### Quelle est la différence entre copier et exécuter ?

- **Copier** : Place la commande dans le presse-papier (vous la collez manuellement)
- **Exécuter** : Lance AutoHotkey qui tape la commande automatiquement dans Minecraft

### Puis-je annuler une commande ?

Utilisez `//undo` dans Minecraft après exécution, ou ajoutez-le à votre macro.

## 📝 Notes de version

### v2.0.0 (Actuelle)
- ✨ Ajout du système de macros
- 📜 Historique persistant avec recherche
- 🎨 Interface modernisée avec CustomTkinter
- ⚡ Amélioration des performances
- 🐛 Correction de bugs mineurs

### v1.0.0
- 🎉 Version initiale
- 📦 Support de toutes les commandes WorldEdit 1.7.10
- 🤖 Automatisation AutoHotkey

## 🤝 Contribution

Les contributions sont les bienvenues ! Vous pouvez :
- Ajouter de nouvelles commandes dans `commands.json`
- Créer des icônes pour les catégories
- Partager vos macros
- Signaler des bugs
- Proposer des améliorations

## 📄 Licence

Ce projet est distribué sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.

## 🙏 Remerciements

- Équipe WorldEdit pour le plugin
- Communauté Python
- CustomTkinter pour l'interface moderne
- AutoHotkey pour l'automatisation

---

**Créé avec ❤️ pour la communauté Minecraft**

*Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue ou à contribuer au projet !*
