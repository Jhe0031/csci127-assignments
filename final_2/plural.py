def countPlurals(line):
    line = line.lower()
    plural = []
    for item in line.split():
        length = len(item)
        if item[length-1] == "s":
            plural.append(item)
    return plural

print(countPlurals("Hello these words are plural dogs mew cats"))
print(countPlurals("tests and finals"))
print(countPlurals("pigs Rats are a type of rodent"))

def notPossessive(line):
    line = line.lower()
    plural = []
    for item in line.split():
        length = len(item)
        if item[length-1] == "s":
            if item[length-2] == "'":
                continue
            else:
                plural.append(item)
    return plural
print(notPossessive("gorillas gorilla's cats"))
print(notPossessive("Ivy's cats love to play with their toys"))
print(notPossessive("Kites are all made by Nancy's dad"))