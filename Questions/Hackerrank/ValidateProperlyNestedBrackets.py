def areBracketsProperlyMatched(code_snippet):
    if not code_snippet:
        return False
    satck = []
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{",
    }
    for ch in code_snippet:
        if ch in pairs.values():
            satck.append(ch)
        elif ch in pairs.keys():
            if not satck:
                return False
            top = satck.pop()
            if pairs[ch] != top:
                return False
        elif ch.isalpha() or ch.isdigit():
            continue
        else:
            continue
    
    if not satck:
        return True
    else:
        return False
