import json

data = {
    "selection": {
        "name": "Sélection",
        "icon": "selection.png",
        "commands": [
            {"name": "//wand", "description": "Obtenir l'outil de sélection", "syntax": "//wand", "params": []},
            {"name": "//pos1", "description": "Définir la première position", "syntax": "//pos1", "params": []},
            {"name": "//pos2", "description": "Définir la deuxième position", "syntax": "//pos2", "params": []},
            {"name": "//hpos1", "description": "Définir la première position sur le bloc visé", "syntax": "//hpos1", "params": []},
            {"name": "//hpos2", "description": "Définir la deuxième position sur le bloc visé", "syntax": "//hpos2", "params": []},
            {"name": "//sel", "description": "Changer le type de sélection", "syntax": "//sel [type]", "params": [
                {"name": "type", "type": "choice", "choices": ["cuboid", "extend", "poly", "ellipsoid", "sphere", "cyl", "convex", "cylinder", "line", "polyhedron"], "default": "cuboid", "required": False}
            ]},
            {"name": "//chunk", "description": "Sélectionner le chunk entier", "syntax": "//chunk", "params": []},
            {"name": "//expand", "description": "Étendre la sélection dans une direction", "syntax": "//expand <montant> [direction] [montant-inverse]", "params": [
                {"name": "montant", "type": "number", "default": 10, "required": True},
                {"name": "direction", "type": "choice", "choices": ["up", "down", "north", "south", "east", "west", "me", "forward", "back"], "default": "me", "required": False},
                {"name": "montant_inverse", "type": "number", "default": None, "required": False}
            ]},
            {"name": "//contract", "description": "Réduire la sélection", "syntax": "//contract <montant> [direction]", "params": [
                {"name": "montant", "type": "number", "default": 10, "required": True},
                {"name": "direction", "type": "choice", "choices": ["up", "down", "north", "south", "east", "west", "me", "forward", "back"], "default": "me", "required": False}
            ]},
            {"name": "//size", "description": "Afficher la taille de la sélection", "syntax": "//size", "params": []},
            {"name": "//count", "description": "Compter les blocs d'un type", "syntax": "//count <bloc>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True}
            ]}
        ]
    },
    "blocks": {
        "name": "Manipulation de blocs",
        "icon": "blocks.png",
        "commands": [
            {"name": "//set", "description": "Remplir la sélection avec un bloc", "syntax": "//set <bloc>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True}
            ]},
            {"name": "//replace", "description": "Remplacer un bloc par un autre", "syntax": "//replace <bloc-source> <bloc-destination>", "params": [
                {"name": "bloc_source", "type": "block", "default": None, "required": False},
                {"name": "bloc_destination", "type": "block", "default": "stone", "required": True}
            ]},
            {"name": "//overlay", "description": "Recouvrir avec un bloc", "syntax": "//overlay <bloc>", "params": [
                {"name": "bloc", "type": "block", "default": "grass", "required": True}
            ]},
            {"name": "//walls", "description": "Créer des murs", "syntax": "//walls <bloc>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True}
            ]},
            {"name": "//faces", "description": "Construire les faces", "syntax": "//faces <bloc>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True}
            ]},
            {"name": "//smooth", "description": "Lisser le terrain", "syntax": "//smooth [iterations]", "params": [
                {"name": "iterations", "type": "number", "default": 1, "required": False}
            ]},
            {"name": "//naturalize", "description": "Naturaliser le terrain", "syntax": "//naturalize", "params": []},
            {"name": "//center", "description": "Placer un bloc au centre", "syntax": "//center <bloc>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True}
            ]}
        ]
    },
    "generation": {
        "name": "Génération",
        "icon": "generation.png",
        "commands": [
            {"name": "//sphere", "description": "Générer une sphère pleine", "syntax": "//sphere <bloc> <rayon> [raised]", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 5, "required": True},
                {"name": "raised", "type": "choice", "choices": ["yes", "no"], "default": "no", "required": False}
            ]},
            {"name": "//hsphere", "description": "Générer une sphère creuse", "syntax": "//hsphere <bloc> <rayon>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 5, "required": True}
            ]},
            {"name": "//cyl", "description": "Générer un cylindre", "syntax": "//cyl <bloc> <rayon> [hauteur]", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 5, "required": True},
                {"name": "hauteur", "type": "number", "default": 1, "required": False}
            ]},
            {"name": "//hcyl", "description": "Générer un cylindre creux", "syntax": "//hcyl <bloc> <rayon> [hauteur]", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 5, "required": True},
                {"name": "hauteur", "type": "number", "default": 1, "required": False}
            ]},
            {"name": "//pyramid", "description": "Générer une pyramide", "syntax": "//pyramid <bloc> <taille>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "taille", "type": "number", "default": 5, "required": True}
            ]},
            {"name": "//hpyramid", "description": "Générer une pyramide creuse", "syntax": "//hpyramid <bloc> <taille>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "taille", "type": "number", "default": 5, "required": True}
            ]},
            {"name": "//generate", "description": "Générer avec expression mathématique", "syntax": "//generate <bloc> <expression>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "expression", "type": "text", "default": "r2sin(0.5z)^2sin(0.5x)^2<0.1", "required": True}
            ]}
        ]
    },
    "clipboard": {
        "name": "Presse-papier",
        "icon": "clipboard.png",
        "commands": [
            {"name": "//copy", "description": "Copier la sélection", "syntax": "//copy [-e]", "params": [
                {"name": "entities", "type": "choice", "choices": ["-e", ""], "default": "", "required": False}
            ]},
            {"name": "//cut", "description": "Couper la sélection", "syntax": "//cut [bloc]", "params": [
                {"name": "bloc_remplacement", "type": "block", "default": "air", "required": False}
            ]},
            {"name": "//paste", "description": "Coller le contenu", "syntax": "//paste [-a] [-o]", "params": [
                {"name": "skip_air", "type": "choice", "choices": ["-a", ""], "default": "", "required": False},
                {"name": "origin", "type": "choice", "choices": ["-o", ""], "default": "", "required": False}
            ]},
            {"name": "//rotate", "description": "Faire pivoter", "syntax": "//rotate <angle>", "params": [
                {"name": "angle", "type": "number", "default": 90, "required": True}
            ]},
            {"name": "//flip", "description": "Retourner", "syntax": "//flip [direction]", "params": [
                {"name": "direction", "type": "choice", "choices": ["north", "south", "east", "west", "up", "down", "me", "forward", "back"], "default": "me", "required": False}
            ]},
            {"name": "//load", "description": "Charger un schematic", "syntax": "//load <fichier>", "params": [
                {"name": "fichier", "type": "text", "default": "mon_schematic", "required": True}
            ]},
            {"name": "//save", "description": "Sauvegarder la sélection", "syntax": "//save <fichier>", "params": [
                {"name": "fichier", "type": "text", "default": "mon_schematic", "required": True}
            ]},
            {"name": "//schematic list", "description": "Lister les schematics", "syntax": "//schematic list [page]", "params": [
                {"name": "page", "type": "number", "default": 1, "required": False}
            ]}
        ]
    },
    "history": {
        "name": "Historique",
        "icon": "history.png",
        "commands": [
            {"name": "//undo", "description": "Annuler", "syntax": "//undo [nombre]", "params": [
                {"name": "nombre", "type": "number", "default": 1, "required": False}
            ]},
            {"name": "//redo", "description": "Refaire", "syntax": "//redo [nombre]", "params": [
                {"name": "nombre", "type": "number", "default": 1, "required": False}
            ]},
            {"name": "//clearhistory", "description": "Effacer l'historique", "syntax": "//clearhistory", "params": []}
        ]
    },
    "utilities": {
        "name": "Utilitaires",
        "icon": "utilities.png",
        "commands": [
            {"name": "//drain", "description": "Drainer l'eau/lave", "syntax": "//drain <rayon>", "params": [
                {"name": "rayon", "type": "number", "default": 10, "required": True}
            ]},
            {"name": "//fixwater", "description": "Corriger l'eau", "syntax": "//fixwater <rayon>", "params": [
                {"name": "rayon", "type": "number", "default": 10, "required": True}
            ]},
            {"name": "//fixlava", "description": "Corriger la lave", "syntax": "//fixlava <rayon>", "params": [
                {"name": "rayon", "type": "number", "default": 10, "required": True}
            ]},
            {"name": "//removeabove", "description": "Retirer les blocs au-dessus", "syntax": "//removeabove [taille] [hauteur]", "params": [
                {"name": "taille", "type": "number", "default": 1, "required": False},
                {"name": "hauteur", "type": "number", "default": 256, "required": False}
            ]},
            {"name": "//removebelow", "description": "Retirer les blocs en-dessous", "syntax": "//removebelow [taille] [hauteur]", "params": [
                {"name": "taille", "type": "number", "default": 1, "required": False},
                {"name": "hauteur", "type": "number", "default": 256, "required": False}
            ]},
            {"name": "//removenear", "description": "Retirer les blocs proches", "syntax": "//removenear <bloc> [rayon]", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 50, "required": False}
            ]},
            {"name": "//fill", "description": "Remplir les trous", "syntax": "//fill <bloc> <rayon> [profondeur]", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 10, "required": True},
                {"name": "profondeur", "type": "number", "default": 1, "required": False}
            ]},
            {"name": "//fillr", "description": "Remplir récursivement", "syntax": "//fillr <bloc> <rayon>", "params": [
                {"name": "bloc", "type": "block", "default": "stone", "required": True},
                {"name": "rayon", "type": "number", "default": 10, "required": True}
            ]},
            {"name": "//snow", "description": "Simuler la neige", "syntax": "//snow [rayon]", "params": [
                {"name": "rayon", "type": "number", "default": 10, "required": False}
            ]},
            {"name": "//thaw", "description": "Faire fondre la neige", "syntax": "//thaw [rayon]", "params": [
                {"name": "rayon", "type": "number", "default": 10, "required": False}
            ]},
            {"name": "//green", "description": "Transformer en herbe", "syntax": "//green [rayon]", "params": [
                {"name": "rayon", "type": "number", "default": 10, "required": False}
            ]},
            {"name": "//ex", "description": "Éteindre le feu", "syntax": "//ex [rayon]", "params": [
                {"name": "rayon", "type": "number", "default": 40, "required": False}
            ]},
            {"name": "//butcher", "description": "Tuer les mobs", "syntax": "//butcher [rayon]", "params": [
                {"name": "rayon", "type": "number", "default": -1, "required": False}
            ]},
            {"name": "//remove", "description": "Retirer les entités", "syntax": "//remove <type> <rayon>", "params": [
                {"name": "type", "type": "choice", "choices": ["items", "arrows", "boats", "minecarts", "tnt", "xp", "paintings"], "default": "items", "required": True},
                {"name": "rayon", "type": "number", "default": -1, "required": True}
            ]}
        ]
    },
    "region": {
        "name": "Régions",
        "icon": "region.png",
        "commands": [
            {"name": "//move", "description": "Déplacer la sélection", "syntax": "//move <montant> [direction] [bloc]", "params": [
                {"name": "montant", "type": "number", "default": 1, "required": True},
                {"name": "direction", "type": "choice", "choices": ["up", "down", "north", "south", "east", "west", "me", "forward", "back"], "default": "me", "required": False},
                {"name": "bloc_remplacement", "type": "block", "default": "air", "required": False}
            ]},
            {"name": "//stack", "description": "Empiler la sélection", "syntax": "//stack <count> [direction]", "params": [
                {"name": "count", "type": "number", "default": 1, "required": True},
                {"name": "direction", "type": "choice",