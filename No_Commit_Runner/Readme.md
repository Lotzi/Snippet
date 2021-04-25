# Löscht Kommentare aus Datein

## Anwendung
``` PowerShell
py.exe .\no_commit.py Datei_zum_Lesen Datei_zum_schreiben
```
Es ist notwendig, dass beide Datein existieren.

## Beispiel an Datein im Ordner test

```PowerShell
py.exe .\no_commit.py .\test\test_commit.txt .\test\test_fertig.txt
```

## Output
Das Skript gibt immer die gelöschten Zeilen zurück.

```PowerShell
Delete: # Hallo Welt
```

## Neues Dateiformat

Neue Dateiformate können in der database.py nachgetragen werden.
