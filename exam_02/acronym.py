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