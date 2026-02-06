; WorldEdit GUI - Exemple de script AutoHotkey
; Ce fichier montre comment les commandes sont automatisées
; Il est généré automatiquement par l'application

#NoEnv
SetWorkingDir %A_ScriptDir%

; Configuration
SetKeyDelay, 50, 50

; Exemple: Créer une sphère de pierre
Send, //sphere stone 10
Send, {Enter}
Sleep, 100

; Exemple: Définir les positions
Send, //pos1
Send, {Enter}
Sleep, 100

Send, //pos2
Send, {Enter}
Sleep, 100

; Exemple: Remplir avec un bloc
Send, //set stone
Send, {Enter}
Sleep, 100

MsgBox, Script d'exemple terminé!
ExitApp
