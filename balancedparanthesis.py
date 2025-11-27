def checkBalancedPranthesis(s):
    stack = []
    pairs = {")":"(", "}":"{","]":"[" }
    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs.keys():
            if not stack:
                return "Not Balanced"
            top = stack.pop()
            if pairs[char] != top:
                return "Not Balanced"
    
    if not stack:
        return "Balanced"
    else:
        return "Not Balanced"
    
s = "{[()]}"
print(checkBalancedPranthesis(s))
            