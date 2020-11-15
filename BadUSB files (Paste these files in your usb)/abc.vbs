Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "I:\start.bat" & Chr(34), 0
Set WshShell = Nothing
Wscript.sleep 10000
Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "I:\server.bat" & Chr(34), 0
Set WshShell = Nothing