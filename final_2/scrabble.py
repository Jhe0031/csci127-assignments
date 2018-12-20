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

