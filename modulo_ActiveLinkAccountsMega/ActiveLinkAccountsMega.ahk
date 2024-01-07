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
SendRaw, confirm %1% %2%
Sleep, 300
Send, {Enter}
Sleep, 3000
SendRaw, %2%
Sleep, 300
Send, {Enter}
Sleep, 7000
SendRaw, exit
Sleep, 300
Send, {Enter}
ExitApp
Return

