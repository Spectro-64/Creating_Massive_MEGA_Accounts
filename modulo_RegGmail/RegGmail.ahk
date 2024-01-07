; This script was created using Pulover's Macro Creator
; www.macrocreator.com

#NoEnv
SetWorkingDir %A_ScriptDir%
CoordMode, Mouse, Window
SendMode Input
#SingleInstance Force
SetTitleMatchMode 2
#WinActivateForce
SetControlDelay 1
SetWinDelay 0
SetKeyDelay -1
SetMouseDelay -1
SetBatchLines -1


Macro1:
Run, MEGAcmd\MEGAcmdShell.exe
Sleep, 2000
SendRaw, signup %1% %2% --name="user user"
Sleep, 300
Send, {Enter}
Sleep, 5000
SendRaw, exit
Sleep, 300
Send, {Enter}
Sleep, 300
ExitApp
Return

