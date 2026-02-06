; WorldEdit GUI - Exemple de script AutoHotkey (v2)
; Envoie une liste de commandes dans Minecraft en respectant les délais.

#Requires AutoHotkey v2.0+
#SingleInstance Force

; === Configuration utilisateur ===
commands := ["//set stone", "//replace stone dirt", "//undo"]
delay := 2000
hotkey := "F8"
stepDelay := 200

; Applique le hotkey configurable.
Hotkey(hotkey, RunCommandSequence)

RunCommandSequence(*) {
    if !WinActive("ahk_exe javaw.exe") {
        return
    }

    for _, cmd in commands {
        Send("{Esc}")
        Sleep(stepDelay)
        Send("t")
        Sleep(stepDelay)
        A_Clipboard := cmd
        Send("^v")
        Sleep(stepDelay)
        Send("{Enter}")
        Sleep(delay)
    }
}
