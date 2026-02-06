"""
Script de test pour WorldEdit GUI
Vérifie que tous les composants sont installés correctement
"""

import sys
import os

def test_python_version():
    """Tester la version de Python"""
    print("🔍 Test de la version Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Trop ancien!")
        print("   Requis: Python 3.8 ou supérieur")
        return False

def test_imports():
    """Tester les imports des dépendances"""
    print("\n🔍 Test des dépendances...")
    
    modules = {
        "customtkinter": "CustomTkinter",
        "PIL": "Pillow",
        "pyperclip": "Pyperclip"
    }
    
    all_ok = True
    for module, name in modules.items():
        try:
            __import__(module)
            print(f"✅ {name} - OK")
        except ImportError:
            print(f"❌ {name} - Manquant!")
            print(f"   Installez avec: pip install {module if module != 'PIL' else 'Pillow'}")
            all_ok = False
    
    return all_ok

def test_files():
    """Tester la présence des fichiers nécessaires"""
    print("\n🔍 Test des fichiers...")
    
    files = {
        "commands.json": "Fichier de commandes",
        "main.py": "Script principal",
        "requirements.txt": "Fichier de dépendances",
        "README.md": "Documentation",
    }
    
    all_ok = True
    for filename, description in files.items():
        if os.path.exists(filename):
            print(f"✅ {description} ({filename}) - OK")
        else:
            print(f"❌ {description} ({filename}) - Manquant!")
            all_ok = False
    
    return all_ok

def test_json():
    """Tester le chargement du fichier JSON"""
    print("\n🔍 Test du fichier JSON...")
    
    try:
        import json
        with open("commands.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        categories = len(data)
        total_commands = sum(len(cat.get("commands", [])) for cat in data.values())
        
        print(f"✅ JSON valide - {categories} catégories, {total_commands} commandes")
        return True
    except Exception as e:
        print(f"❌ Erreur JSON: {e}")
        return False

def test_assets():
    """Tester le dossier assets"""
    print("\n🔍 Test des assets...")
    
    if os.path.exists("assets"):
        icons = [f for f in os.listdir("assets") if f.endswith(".png")]
        if icons:
            print(f"✅ Dossier assets - {len(icons)} icône(s) trouvée(s)")
            return True
        else:
            print("⚠️ Dossier assets vide - Les icônes seront manquantes")
            return True
    else:
        print("⚠️ Dossier assets manquant - Sera créé automatiquement")
        return True

def main():
    """Fonction principale de test"""
    print("=" * 60)
    print("🧪 WorldEdit GUI - Tests de vérification")
    print("=" * 60)
    
    tests = [
        test_python_version(),
        test_imports(),
        test_files(),
        test_json(),
        test_assets()
    ]
    
    print("\n" + "=" * 60)
    if all(tests):
        print("✅ TOUS LES TESTS SONT PASSÉS!")
        print("🚀 Vous pouvez lancer l'application avec: python main.py")
    else:
        print("❌ CERTAINS TESTS ONT ÉCHOUÉ")
        print("📋 Corrigez les problèmes ci-dessus avant de lancer l'application")
    print("=" * 60)
    
    return all(tests)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
