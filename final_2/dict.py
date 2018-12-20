dict = {}

def addline(d, line):
    line.lower()
    for word in line.split():
        if word[0] not in d:
            d[word[0]] = [word]
        elif word[0] in d:
            d[word[0]] += [word]
    return d
print(addline(dict, "cat mew dog cow"))
print(addline(dict, "sad life happy so"))
print(addline(dict, "test take finals"))
print(addline(dict, "sabrina nancy mario"))
print(addline(dict, "something abc bracadabra"))

print("---------------")

def spellcheck(d, word):
    word.lower()
    if word[0] in d:
        if word in d[word[0]]:
            return True
    return False
print(spellcheck(dict, "cat"))
print(spellcheck(dict, "so"))
print(spellcheck(dict, "nope"))
print(spellcheck(dict, "pizza"))