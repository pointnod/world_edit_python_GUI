@echo off
title WorldEdit GUI Launcher
color 0A

echo ========================================
echo   WorldEdit GUI v2.0.0 - Launcher
echo ========================================
echo.

REM Verification de Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH!
    echo.
    echo Telechargez Python depuis: https://www.python.org/
    echo N'oubliez pas de cocher "Add Python to PATH" lors de l'installation
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.

REM Installation des dependances si necessaire
if not exist "venv\" (
    echo [INFO] Creation de l'environnement virtuel...
    python -m venv venv
    echo [OK] Environnement virtuel cree
    echo.
)

REM Activation de l'environnement virtuel
call venv\Scripts\activate.bat

REM Installation/mise a jour des dependances
echo [INFO] Verification des dependances...
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERREUR] Impossible d'installer les dependances!
    pause
    exit /b 1
)
echo [OK] Dependances installees
echo.

REM Lancement de l'application
echo [INFO] Lancement de WorldEdit GUI...
echo ========================================
echo.
python main.py

REM Si l'application se ferme avec une erreur
if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo [ERREUR] L'application s'est fermee avec une erreur!
    echo ========================================
    pause
)

deactivate
