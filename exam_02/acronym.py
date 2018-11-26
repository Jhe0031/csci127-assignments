def makeacronym(w):
    w = w.lower()
    new_w = []
    for word in w.split():
        new_w.append(word[:1])
    return "".join(new_w)
print(makeacronym("Laugh Out Loud"))
print(makeacronym("Read the... fine manual"))
print(makeacronym("In my humble opinion"))
print(makeacronym("In my not so humble opinion"))

### In class solution
def make_acronym(line):
    result = ""
    for word in line.split():
        result = result + word[0]
    return result
print(make_acronym("Laugh Out Loud"))
print(make_acronym("Read the... fine manual"))
print(make_acronym("In my humble opinion"))
print(make_acronym("In my not so humble opinion"))