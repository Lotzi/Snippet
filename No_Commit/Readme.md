# Deletes comments from files

## Application
``` PowerShell
py.exe .\no_commit.py Datei_zum_Lesen Datei_zum_schreiben
```
It is necessary that both files exist.

## Example of files in the test folder

```PowerShell
py.exe .\no_commit.py .\test\test_commit.txt .\test\test_fertig.txt
```

## Output
The script always returns the deleted lines.

```PowerShell
Delete: # Hallo Welt
```

## New file format

New file formats can be added in database.py.
