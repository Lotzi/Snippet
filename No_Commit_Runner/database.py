def getTrennzeichen(e):
    if e == "txt":
        return "#"
    elif e == "java":
        return "//"
    elif e == "pgn":
        return "%"    
    elif e == "gitignore":
        return "#"
    else: 
        return False
