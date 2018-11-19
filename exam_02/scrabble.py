def score(w):
    value = {'AEIOULNRST': 1, 'DG': 2, 'BCMP': 3, 'FHVWY': 4, 'K': 5, 'JX': 8, 'QZ': 10}
    w = w.upper()
    value = 0
    for letter in w:
        if letter in 'AEIOULNRST':
            value += 1
        elif letter in 'DG':
            value += 2
        elif letter in 'BCMP':
            value += 3
        elif letter in 'FHVWY':
            value += 4
        elif letter in 'K':
            value += 5
        elif letter in 'JX':
            value += 8
        elif letter in 'QZ':
            value += 10
    return value
print("Hello,", score("Hello"))
print("Goodbye,", score("Goodbye"))
print("Bonjour,", score("Bonjour"))