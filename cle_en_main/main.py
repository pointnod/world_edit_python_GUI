"""
WorldEdit GUI - Interface graphique pour WorldEdit 1.7.10
Version: 2.0.0
Auteur: Assistant IA
Description: Outil GUI pour faciliter l'utilisation des commandes WorldEdit
"""

import customtkinter as ctk
import json
import os
import sys
from tkinter import messagebox, filedialog, Toplevel
from PIL import Image
import pyperclip
import subprocess
from datetime import datetime
import shutil

# Configuration de l'apparence
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class WorldEditGUI:
    def __init__(self):
        """Initialisation de l'application"""
        self.root = ctk.CTk()
        self.root.title("WorldEdit GUI v2.0.0 - Minecraft 1.7.10")
        self.root.geometry("1200x800")
        
        # Chemins des fichiers
        self.base_path = self.get_base_path()
        self.commands_file = os.path.join(self.base_path, "commands.json")
        self.history_file = os.path.join(self.base_path, "history.json")
        self.macros_file = os.path.join(self.base_path, "macros.json")
        self.assets_path = os.path.join(self.base_path, "assets")
        
        # Variables d'état
        self.commands_data = {}
        self.command_queue = []
        self.history = []
        self.macros = {}
        self.current_category = None
        self.ahk_path = self.get_default_ahk_path()
        
        # Charger les données
        self.load_commands()
        self.load_history()
        self.load_macros()
        
        # Construire l'interface
        self.create_ui()
        
    def get_base_path(self):
        """Obtenir le chemin de base de l'application"""
        if getattr(sys, 'frozen', False):
            return os.path.dirname(sys.executable)
        return os.path.dirname(os.path.abspath(__file__))

    def get_default_ahk_path(self):
        """Définir le chemin AutoHotkey par défaut (v2 puis v1)."""
        preferred_paths = [
            r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\AutoHotkey Dash.lnk",
            r"C:\Program Files\AutoHotkey\Compiler\Ahk2Exe.exe",
            "autohotkey.exe",
        ]

        for path in preferred_paths:
            if os.path.exists(path):
                return path
        return preferred_paths[-1]
    
    def load_commands(self):
        """Charger les commandes depuis le fichier JSON"""
        try:
            with open(self.commands_file, 'r', encoding='utf-8') as f:
                self.commands_data = json.load(f)
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de charger commands.json: {e}")
            self.commands_data = {}
    
    def load_history(self):
        """Charger l'historique des commandes"""
        try:
            if os.path.exists(self.history_file):
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    self.history = json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de l'historique: {e}")
            self.history = []
    
    def save_history(self):
        """Sauvegarder l'historique des commandes"""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de l'historique: {e}")
    
    def load_macros(self):
        """Charger les macros"""
        try:
            if os.path.exists(self.macros_file):
                with open(self.macros_file, 'r', encoding='utf-8') as f:
                    self.macros = json.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement des macros: {e}")
            self.macros = {}
    
    def save_macros(self):
        """Sauvegarder les macros"""
        try:
            with open(self.macros_file, 'w', encoding='utf-8') as f:
                json.dump(self.macros, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des macros: {e}")
    
    def create_ui(self):
        """Créer l'interface utilisateur principale"""
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Titre
        title = ctk.CTkLabel(main_frame, text="🎮 WorldEdit GUI 1.7.10", 
                            font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=10)
        
        # Container pour la partie principale
        content_frame = ctk.CTkFrame(main_frame)
        content_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frame gauche: Catégories
        left_frame = ctk.CTkFrame(content_frame, width=200)
        left_frame.pack(side="left", fill="y", padx=(0, 10))
        
        categories_label = ctk.CTkLabel(left_frame, text="📁 Catégories", 
                                       font=ctk.CTkFont(size=16, weight="bold"))
        categories_label.pack(pady=10)
        
        self.categories_frame = ctk.CTkScrollableFrame(left_frame, width=180)
        self.categories_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.create_categories()
        
        # Frame central: Commandes
        center_frame = ctk.CTkFrame(content_frame)
        center_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))
        
        commands_label = ctk.CTkLabel(center_frame, text="⚙️ Commandes", 
                                     font=ctk.CTkFont(size=16, weight="bold"))
        commands_label.pack(pady=10)
        
        self.commands_frame = ctk.CTkScrollableFrame(center_frame)
        self.commands_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Frame droite: File d'attente et actions
        right_frame = ctk.CTkFrame(content_frame, width=300)
        right_frame.pack(side="right", fill="y")
        
        queue_label = ctk.CTkLabel(right_frame, text="📋 File d'attente", 
                                  font=ctk.CTkFont(size=16, weight="bold"))
        queue_label.pack(pady=10)
        
        self.queue_frame = ctk.CTkScrollableFrame(right_frame, height=200)
        self.queue_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Boutons d'action
        actions_frame = ctk.CTkFrame(right_frame)
        actions_frame.pack(fill="x", padx=5, pady=10)
        
        ctk.CTkButton(actions_frame, text="📋 Copier tout", 
                     command=self.copy_queue).pack(fill="x", pady=2)
        ctk.CTkButton(actions_frame, text="▶️ Exécuter (AHK)", 
                     command=self.execute_queue_ahk).pack(fill="x", pady=2)
        ctk.CTkButton(actions_frame, text="🗑️ Vider la file", 
                     command=self.clear_queue).pack(fill="x", pady=2)
        
        # Frame du bas: Onglets
        bottom_frame = ctk.CTkFrame(main_frame)
        bottom_frame.pack(fill="x", padx=10, pady=(10, 0))
        
        # Onglets
        self.tabview = ctk.CTkTabview(bottom_frame)
        self.tabview.pack(fill="x", pady=5)
        
        # Onglet Historique
        self.tabview.add("📜 Historique")
        self.create_history_tab()
        
        # Onglet Macros
        self.tabview.add("🔧 Macros")
        self.create_macros_tab()
        
        # Onglet Paramètres
        self.tabview.add("⚙️ Paramètres")
        self.create_settings_tab()
    
    def create_categories(self):
        """Créer les boutons de catégories"""
        for category_id, category_data in self.commands_data.items():
            btn = ctk.CTkButton(
                self.categories_frame,
                text=category_data.get("name", category_id),
                command=lambda c=category_id: self.show_category(c),
                height=40,
                anchor="w"
            )
            btn.pack(fill="x", pady=2)
    
    def show_category(self, category_id):
        """Afficher les commandes d'une catégorie"""
        self.current_category = category_id
        
        # Nettoyer le frame des commandes
        for widget in self.commands_frame.winfo_children():
            widget.destroy()
        
        category_data = self.commands_data.get(category_id, {})
        commands = category_data.get("commands", [])
        
        for cmd in commands:
            self.create_command_widget(cmd)
    
    def create_command_widget(self, cmd_data):
        """Créer un widget pour une commande"""
        # Frame pour la commande
        cmd_frame = ctk.CTkFrame(self.commands_frame)
        cmd_frame.pack(fill="x", padx=5, pady=5)
        
        # En-tête de la commande
        header_frame = ctk.CTkFrame(cmd_frame)
        header_frame.pack(fill="x", padx=5, pady=5)
        
        name_label = ctk.CTkLabel(header_frame, text=cmd_data.get("name", ""),
                                 font=ctk.CTkFont(size=14, weight="bold"))
        name_label.pack(side="left", padx=5)
        
        # Bouton info
        info_btn = ctk.CTkButton(header_frame, text="ℹ️", width=30,
                                command=lambda: self.show_command_info(cmd_data))
        info_btn.pack(side="right", padx=5)
        
        # Description
        desc_label = ctk.CTkLabel(cmd_frame, text=cmd_data.get("description", ""),
                                 wraplength=400, justify="left")
        desc_label.pack(fill="x", padx=5, pady=5)
        
        # Paramètres
        params = cmd_data.get("params", [])
        param_widgets = {}
        
        if params:
            params_frame = ctk.CTkFrame(cmd_frame)
            params_frame.pack(fill="x", padx=5, pady=5)
            
            for param in params:
                param_name = param.get("name", "")
                param_type = param.get("type", "text")
                param_default = param.get("default", "")
                
                # Label du paramètre
                label = ctk.CTkLabel(params_frame, text=f"{param_name}:")
                label.pack(anchor="w", padx=5, pady=2)
                
                # Widget selon le type
                if param_type == "choice":
                    choices = param.get("choices", [])
                    widget = ctk.CTkComboBox(params_frame, values=choices)
                    if param_default:
                        widget.set(param_default)
                elif param_type == "number":
                    widget = ctk.CTkEntry(params_frame)
                    if param_default:
                        widget.insert(0, str(param_default))
                else:  # text
                    widget = ctk.CTkEntry(params_frame)
                    if param_default:
                        widget.insert(0, param_default)
                
                widget.pack(fill="x", padx=5, pady=2)
                param_widgets[param_name] = widget
        
        # Boutons d'action
        buttons_frame = ctk.CTkFrame(cmd_frame)
        buttons_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkButton(buttons_frame, text="➕ Ajouter à la file",
                     command=lambda: self.add_to_queue(cmd_data, param_widgets)).pack(side="left", padx=2)
        ctk.CTkButton(buttons_frame, text="📋 Copier",
                     command=lambda: self.copy_command(cmd_data, param_widgets)).pack(side="left", padx=2)
        ctk.CTkButton(buttons_frame, text="▶️ Exécuter",
                     command=lambda: self.execute_command(cmd_data, param_widgets)).pack(side="left", padx=2)
    
    def show_command_info(self, cmd_data):
        """Afficher les informations détaillées d'une commande"""
        info_window = Toplevel(self.root)
        info_window.title("Informations de la commande")
        info_window.geometry("500x400")
        
        frame = ctk.CTkFrame(info_window)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Nom
        ctk.CTkLabel(frame, text=cmd_data.get("name", ""), 
                    font=ctk.CTkFont(size=18, weight="bold")).pack(pady=5)
        
        # Syntaxe
        ctk.CTkLabel(frame, text="Syntaxe:", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=5)
        syntax_text = ctk.CTkTextbox(frame, height=50)
        syntax_text.pack(fill="x", padx=5, pady=5)
        syntax_text.insert("1.0", cmd_data.get("syntax", ""))
        syntax_text.configure(state="disabled")
        
        # Description
        ctk.CTkLabel(frame, text="Description:", 
                    font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=5)
        desc_text = ctk.CTkTextbox(frame, height=100)
        desc_text.pack(fill="x", padx=5, pady=5)
        desc_text.insert("1.0", cmd_data.get("description", ""))
        desc_text.configure(state="disabled")
        
        # Paramètres
        params = cmd_data.get("params", [])
        if params:
            ctk.CTkLabel(frame, text="Paramètres:", 
                        font=ctk.CTkFont(weight="bold")).pack(anchor="w", pady=5)
            params_text = ctk.CTkTextbox(frame, height=150)
            params_text.pack(fill="x", padx=5, pady=5)
            
            for param in params:
                param_info = f"• {param.get('name', '')} ({param.get('type', 'text')})"
                if param.get('required', False):
                    param_info += " [REQUIS]"
                param_info += f"\n  Défaut: {param.get('default', 'aucun')}\n"
                params_text.insert("end", param_info)
            
            params_text.configure(state="disabled")
    
    def build_command(self, cmd_data, param_widgets):
        """Construire une commande avec ses paramètres"""
        base_cmd = cmd_data.get("name", "")
        params = cmd_data.get("params", [])
        
        command_parts = [base_cmd]
        
        for param in params:
            param_name = param.get("name", "")
            widget = param_widgets.get(param_name)
            
            if widget:
                value = widget.get().strip()
                
                # Traiter les choix spéciaux
                if "(-e)" in value:
                    command_parts.append("-e")
                elif "(-a)" in value:
                    command_parts.append("-a")
                elif "(-o)" in value:
                    command_parts.append("-o")
                elif "(-r)" in value:
                    command_parts.append("-r")
                elif value and value not in ["sans entités", "coller air", "position actuelle"]:
                    command_parts.append(value)
        
        return " ".join(command_parts)
    
    def add_to_queue(self, cmd_data, param_widgets):
        """Ajouter une commande à la file d'attente"""
        command = self.build_command(cmd_data, param_widgets)
        self.command_queue.append(command)
        self.update_queue_display()
        
        # Ajouter à l'historique
        self.add_to_history(command, self.current_category)
    
    def update_queue_display(self):
        """Mettre à jour l'affichage de la file d'attente"""
        for widget in self.queue_frame.winfo_children():
            widget.destroy()
        
        for i, cmd in enumerate(self.command_queue):
            frame = ctk.CTkFrame(self.queue_frame)
            frame.pack(fill="x", pady=2)
            
            label = ctk.CTkLabel(frame, text=f"{i+1}. {cmd}", anchor="w")
            label.pack(side="left", fill="x", expand=True, padx=5)
            
            remove_btn = ctk.CTkButton(frame, text="❌", width=30,
                                      command=lambda idx=i: self.remove_from_queue(idx))
            remove_btn.pack(side="right", padx=2)
    
    def remove_from_queue(self, index):
        """Retirer une commande de la file d'attente"""
        if 0 <= index < len(self.command_queue):
            self.command_queue.pop(index)
            self.update_queue_display()
    
    def copy_command(self, cmd_data, param_widgets):
        """Copier une commande dans le presse-papier"""
        command = self.build_command(cmd_data, param_widgets)
        pyperclip.copy(command)
        messagebox.showinfo("Succès", f"Commande copiée: {command}")
        self.add_to_history(command, self.current_category)
    
    def execute_command(self, cmd_data, param_widgets):
        """Exécuter une seule commande via AHK"""
        command = self.build_command(cmd_data, param_widgets)
        self.execute_ahk_script([command])
        self.add_to_history(command, self.current_category)
    
    def copy_queue(self):
        """Copier toute la file d'attente dans le presse-papier"""
        if not self.command_queue:
            messagebox.showwarning("Attention", "La file d'attente est vide!")
            return
        
        commands_text = "\n".join(self.command_queue)
        pyperclip.copy(commands_text)
        messagebox.showinfo("Succès", f"{len(self.command_queue)} commandes copiées!")
    
    def clear_queue(self):
        """Vider la file d'attente"""
        self.command_queue.clear()
        self.update_queue_display()
    
    def execute_queue_ahk(self):
        """Exécuter la file d'attente via AutoHotkey"""
        if not self.command_queue:
            messagebox.showwarning("Attention", "La file d'attente est vide!")
            return
        
        self.execute_ahk_script(self.command_queue)
    
    def execute_ahk_script(self, commands):
        """Générer et exécuter un script AutoHotkey"""
        try:
            delay = self.delay_var.get() if hasattr(self, 'delay_var') else 100
            
            # Créer le script AHK
            script_content = "#NoEnv\nSetWorkingDir %A_ScriptDir%\n\n"
            
            for cmd in commands:
                script_content += f'Send, {cmd}\n'
                script_content += 'Send, {{Enter}}\n'
                script_content += f'Sleep, {delay}\n\n'
            
            # Sauvegarder le script
            script_path = os.path.join(self.base_path, "temp_script.ahk")
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            # Exécuter le script
            subprocess.Popen([self.ahk_path, script_path])
            messagebox.showinfo("Succès", f"{len(commands)} commande(s) en cours d'exécution!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur d'exécution AHK: {e}")
    
    def add_to_history(self, command, category):
        """Ajouter une commande à l'historique"""
        entry = {
            "command": command,
            "category": category,
            "timestamp": datetime.now().isoformat()
        }
        self.history.insert(0, entry)
        
        # Limiter l'historique à 1000 entrées
        if len(self.history) > 1000:
            self.history = self.history[:1000]
        
        self.save_history()
        if hasattr(self, 'history_listbox'):
            self.update_history_display()
    
    def create_history_tab(self):
        """Créer l'onglet historique"""
        history_tab = self.tabview.tab("📜 Historique")
        
        # Barre de recherche
        search_frame = ctk.CTkFrame(history_tab)
        search_frame.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkLabel(search_frame, text="🔍 Rechercher:").pack(side="left", padx=5)
        self.history_search = ctk.CTkEntry(search_frame)
        self.history_search.pack(side="left", fill="x", expand=True, padx=5)
        self.history_search.bind("<KeyRelease>", lambda e: self.update_history_display())
        
        ctk.CTkButton(search_frame, text="🗑️ Effacer l'historique",
                     command=self.clear_history).pack(side="right", padx=5)
        
        # Liste de l'historique
        self.history_listbox = ctk.CTkScrollableFrame(history_tab, height=150)
        self.history_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.update_history_display()
    
    def update_history_display(self):
        """Mettre à jour l'affichage de l'historique"""
        for widget in self.history_listbox.winfo_children():
            widget.destroy()
        
        search_term = self.history_search.get().lower() if hasattr(self, 'history_search') else ""
        
        for entry in self.history:
            cmd = entry.get("command", "")
            
            if search_term and search_term not in cmd.lower():
                continue
            
            frame = ctk.CTkFrame(self.history_listbox)
            frame.pack(fill="x", pady=2)
            
            # Timestamp
            timestamp = entry.get("timestamp", "")
            if timestamp:
                try:
                    dt = datetime.fromisoformat(timestamp)
                    time_str = dt.strftime("%d/%m/%Y %H:%M")
                except:
                    time_str = "N/A"
            else:
                time_str = "N/A"
            
            time_label = ctk.CTkLabel(frame, text=time_str, width=120)
            time_label.pack(side="left", padx=5)
            
            # Commande
            cmd_label = ctk.CTkLabel(frame, text=cmd, anchor="w")
            cmd_label.pack(side="left", fill="x", expand=True, padx=5)
            
            # Boutons
            ctk.CTkButton(frame, text="📋", width=30,
                         command=lambda c=cmd: pyperclip.copy(c)).pack(side="right", padx=2)
            ctk.CTkButton(frame, text="➕", width=30,
                         command=lambda c=cmd: self.add_command_to_queue(c)).pack(side="right", padx=2)
    
    def add_command_to_queue(self, command):
        """Ajouter une commande de l'historique à la file"""
        self.command_queue.append(command)
        self.update_queue_display()
        messagebox.showinfo("Succès", "Commande ajoutée à la file!")
    
    def clear_history(self):
        """Effacer l'historique"""
        if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir effacer l'historique?"):
            self.history.clear()
            self.save_history()
            self.update_history_display()
    
    def create_macros_tab(self):
        """Créer l'onglet macros"""
        macros_tab = self.tabview.tab("🔧 Macros")
        
        # Barre d'outils
        toolbar = ctk.CTkFrame(macros_tab)
        toolbar.pack(fill="x", padx=5, pady=5)
        
        ctk.CTkButton(toolbar, text="➕ Nouvelle macro",
                     command=self.create_macro).pack(side="left", padx=2)
        ctk.CTkButton(toolbar, text="💾 Sauvegarder",
                     command=self.save_macros).pack(side="left", padx=2)
        ctk.CTkButton(toolbar, text="📂 Importer",
                     command=self.import_macros).pack(side="left", padx=2)
        ctk.CTkButton(toolbar, text="💾 Exporter",
                     command=self.export_macros).pack(side="left", padx=2)
        
        # Liste des macros
        self.macros_listbox = ctk.CTkScrollableFrame(macros_tab, height=150)
        self.macros_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        
        self.update_macros_display()
    
    def update_macros_display(self):
        """Mettre à jour l'affichage des macros"""
        for widget in self.macros_listbox.winfo_children():
            widget.destroy()
        
        for macro_name, macro_data in self.macros.items():
            frame = ctk.CTkFrame(self.macros_listbox)
            frame.pack(fill="x", pady=5, padx=5)
            
            # En-tête
            header = ctk.CTkFrame(frame)
            header.pack(fill="x", padx=5, pady=5)
            
            name_label = ctk.CTkLabel(header, text=f"📦 {macro_name}",
                                     font=ctk.CTkFont(size=14, weight="bold"))
            name_label.pack(side="left", padx=5)
            
            # Boutons d'action
            btn_frame = ctk.CTkFrame(header)
            btn_frame.pack(side="right")
            
            ctk.CTkButton(btn_frame, text="▶️", width=30,
                         command=lambda m=macro_name: self.execute_macro(m)).pack(side="left", padx=2)
            ctk.CTkButton(btn_frame, text="➕", width=30,
                         command=lambda m=macro_name: self.add_macro_to_queue(m)).pack(side="left", padx=2)
            ctk.CTkButton(btn_frame, text="✏️", width=30,
                         command=lambda m=macro_name: self.edit_macro(m)).pack(side="left", padx=2)
            ctk.CTkButton(btn_frame, text="❌", width=30,
                         command=lambda m=macro_name: self.delete_macro(m)).pack(side="left", padx=2)
            
            # Description
            desc = macro_data.get("description", "Aucune description")
            ctk.CTkLabel(frame, text=desc).pack(anchor="w", padx=5, pady=2)
            
            # Nombre de commandes
            commands = macro_data.get("commands", [])
            ctk.CTkLabel(frame, text=f"📋 {len(commands)} commande(s)").pack(anchor="w", padx=5, pady=2)
    
    def create_macro(self):
        """Créer une nouvelle macro"""
        dialog = Toplevel(self.root)
        dialog.title("Nouvelle macro")
        dialog.geometry("600x500")
        
        frame = ctk.CTkFrame(dialog)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Nom
        ctk.CTkLabel(frame, text="Nom de la macro:").pack(anchor="w", pady=5)
        name_entry = ctk.CTkEntry(frame)
        name_entry.pack(fill="x", pady=5)
        
        # Description
        ctk.CTkLabel(frame, text="Description:").pack(anchor="w", pady=5)
        desc_entry = ctk.CTkEntry(frame)
        desc_entry.pack(fill="x", pady=5)
        
        # Commandes
        ctk.CTkLabel(frame, text="Commandes (une par ligne):").pack(anchor="w", pady=5)
        commands_text = ctk.CTkTextbox(frame, height=250)
        commands_text.pack(fill="both", expand=True, pady=5)
        
        # Bouton sauvegarder
        def save_new_macro():
            name = name_entry.get().strip()
            desc = desc_entry.get().strip()
            commands = [cmd.strip() for cmd in commands_text.get("1.0", "end").split("\n") if cmd.strip()]
            
            if not name:
                messagebox.showerror("Erreur", "Le nom est requis!")
                return
            
            if name in self.macros:
                if not messagebox.askyesno("Confirmation", "Une macro avec ce nom existe déjà. Écraser?"):
                    return
            
            self.macros[name] = {
                "description": desc,
                "commands": commands
            }
            
            self.save_macros()
            self.update_macros_display()
            dialog.destroy()
            messagebox.showinfo("Succès", "Macro créée avec succès!")
        
        ctk.CTkButton(frame, text="💾 Sauvegarder", command=save_new_macro).pack(pady=10)
    
    def edit_macro(self, macro_name):
        """Éditer une macro existante"""
        macro_data = self.macros.get(macro_name, {})
        
        dialog = Toplevel(self.root)
        dialog.title(f"Éditer: {macro_name}")
        dialog.geometry("600x500")
        
        frame = ctk.CTkFrame(dialog)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Nom
        ctk.CTkLabel(frame, text="Nom de la macro:").pack(anchor="w", pady=5)
        name_entry = ctk.CTkEntry(frame)
        name_entry.insert(0, macro_name)
        name_entry.pack(fill="x", pady=5)
        
        # Description
        ctk.CTkLabel(frame, text="Description:").pack(anchor="w", pady=5)
        desc_entry = ctk.CTkEntry(frame)
        desc_entry.insert(0, macro_data.get("description", ""))
        desc_entry.pack(fill="x", pady=5)
        
        # Commandes
        ctk.CTkLabel(frame, text="Commandes (une par ligne):").pack(anchor="w", pady=5)
        commands_text = ctk.CTkTextbox(frame, height=250)
        commands_text.pack(fill="both", expand=True, pady=5)
        commands_text.insert("1.0", "\n".join(macro_data.get("commands", [])))
        
        # Bouton sauvegarder
        def save_edited_macro():
            new_name = name_entry.get().strip()
            desc = desc_entry.get().strip()
            commands = [cmd.strip() for cmd in commands_text.get("1.0", "end").split("\n") if cmd.strip()]
            
            if not new_name:
                messagebox.showerror("Erreur", "Le nom est requis!")
                return
            
            # Supprimer l'ancienne entrée si le nom a changé
            if new_name != macro_name and macro_name in self.macros:
                del self.macros[macro_name]
            
            self.macros[new_name] = {
                "description": desc,
                "commands": commands
            }
            
            self.save_macros()
            self.update_macros_display()
            dialog.destroy()
            messagebox.showinfo("Succès", "Macro modifiée avec succès!")
        
        ctk.CTkButton(frame, text="💾 Sauvegarder", command=save_edited_macro).pack(pady=10)
    
    def delete_macro(self, macro_name):
        """Supprimer une macro"""
        if messagebox.askyesno("Confirmation", f"Supprimer la macro '{macro_name}'?"):
            if macro_name in self.macros:
                del self.macros[macro_name]
                self.save_macros()
                self.update_macros_display()
                messagebox.showinfo("Succès", "Macro supprimée!")
    
    def execute_macro(self, macro_name):
        """Exécuter une macro"""
        macro_data = self.macros.get(macro_name)
        if not macro_data:
            messagebox.showerror("Erreur", "Macro introuvable!")
            return
        
        commands = macro_data.get("commands", [])
        if not commands:
            messagebox.showwarning("Attention", "Cette macro est vide!")
            return
        
        self.execute_ahk_script(commands)
    
    def add_macro_to_queue(self, macro_name):
        """Ajouter les commandes d'une macro à la file"""
        macro_data = self.macros.get(macro_name)
        if not macro_data:
            messagebox.showerror("Erreur", "Macro introuvable!")
            return
        
        commands = macro_data.get("commands", [])
        self.command_queue.extend(commands)
        self.update_queue_display()
        messagebox.showinfo("Succès", f"{len(commands)} commande(s) ajoutée(s) à la file!")
    
    def import_macros(self):
        """Importer des macros depuis un fichier JSON"""
        filepath = filedialog.askopenfilename(
            title="Importer des macros",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )
        
        if not filepath:
            return
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                imported = json.load(f)
            
            self.macros.update(imported)
            self.save_macros()
            self.update_macros_display()
            messagebox.showinfo("Succès", f"{len(imported)} macro(s) importée(s)!")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur d'importation: {e}")
    
    def export_macros(self):
        """Exporter les macros vers un fichier JSON"""
        filepath = filedialog.asksaveasfilename(
            title="Exporter les macros",
            defaultextension=".json",
            filetypes=[("Fichiers JSON", "*.json"), ("Tous les fichiers", "*.*")]
        )
        
        if not filepath:
            return
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.macros, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Succès", "Macros exportées avec succès!")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur d'exportation: {e}")
    
    def create_settings_tab(self):
        """Créer l'onglet paramètres"""
        settings_tab = self.tabview.tab("⚙️ Paramètres")
        
        frame = ctk.CTkFrame(settings_tab)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Délai entre les commandes
        ctk.CTkLabel(frame, text="⏱️ Délai entre les commandes (ms):",
                    font=ctk.CTkFont(size=14)).pack(anchor="w", pady=10)
        
        self.delay_var = ctk.IntVar(value=100)
        delay_slider = ctk.CTkSlider(frame, from_=50, to=1000, variable=self.delay_var,
                                    number_of_steps=19)
        delay_slider.pack(fill="x", pady=5)
        
        delay_label = ctk.CTkLabel(frame, textvariable=self.delay_var)
        delay_label.pack(pady=5)
        
        # Chemin AutoHotkey
        ctk.CTkLabel(frame, text="📂 Chemin AutoHotkey:",
                    font=ctk.CTkFont(size=14)).pack(anchor="w", pady=10)
        
        ahk_frame = ctk.CTkFrame(frame)
        ahk_frame.pack(fill="x", pady=5)
        
        self.ahk_entry = ctk.CTkEntry(ahk_frame)
        self.ahk_entry.insert(0, self.ahk_path)
        self.ahk_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        ctk.CTkButton(ahk_frame, text="📁 Parcourir",
                     command=self.browse_ahk).pack(side="right")
        
        # Informations
        ctk.CTkLabel(frame, text="\n📋 Informations",
                    font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w", pady=10)
        
        info_text = f"""
Version: 2.0.0
Python: {sys.version.split()[0]}
Historique: {len(self.history)} entrée(s)
Macros: {len(self.macros)} macro(s)
Catégories: {len(self.commands_data)}
        """
        
        ctk.CTkLabel(frame, text=info_text, justify="left").pack(anchor="w", pady=5)
        
        # Bouton À propos
        ctk.CTkButton(frame, text="ℹ️ À propos",
                     command=self.show_about).pack(pady=10)
    
    def browse_ahk(self):
        """Parcourir pour trouver AutoHotkey"""
        filepath = filedialog.askopenfilename(
            title="Sélectionner AutoHotkey.exe",
            filetypes=[("Exécutables", "*.exe"), ("Tous les fichiers", "*.*")]
        )
        
        if filepath:
            self.ahk_path = filepath
            self.ahk_entry.delete(0, "end")
            self.ahk_entry.insert(0, filepath)
    
    def show_about(self):
        """Afficher la fenêtre À propos"""
        about_text = """
WorldEdit GUI v2.0.0
━━━━━━━━━━━━━━━━━━━━━━

Interface graphique pour WorldEdit 1.7.10

Fonctionnalités:
• Gestion complète des commandes WorldEdit
• Système de file d'attente
• Historique persistant
• Macros personnalisables
• Automatisation via AutoHotkey
• Interface intuitive et moderne

Créé avec Python & CustomTkinter
        """
        messagebox.showinfo("À propos", about_text)
    
    def run(self):
        """Lancer l'application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = WorldEditGUI()
    app.run()
