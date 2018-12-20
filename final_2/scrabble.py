def canMakeWord(letters, word):
    lett = []
    for alpha in letters:
        lett.append(alpha)
    for alpha in word:
        if alpha in lett:
            lett.remove(alpha)
        else:
            return False
    return True
print(canMakeWord("ladilmy", "daily"))
print(canMakeWord("eerriin", "eerie"))
print(canMakeWord("orrpgma", "program"))
print(canMakeWord("orppgma", "program"))

print('-------------')

def withWild(letters, word):
    lett = []
    wild = 0
    for alpha in letters:
        if alpha == "?":
            wild += 1
        else:
            lett.append(alpha)
    for alpha in word:
        if alpha in lett:
            lett.remove(alpha)
        else:
            if wild >= 1:
                wild -= 1
            else:
                return False
    return True
print(withWild("ladilmy", "daily"))
print(withWild("e?erriin", "eerie"))
print(withWild("orrpgma", "program"))
print(withWild("orppgma", "program"))
print(withWild("?????", "apple"))