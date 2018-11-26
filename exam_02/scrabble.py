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

### In class solution
composite_scores = {('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1, ('D', 'G'): 2, ('B', 'C', 'M', 'P'): 3, ('F', 'H', 'V', 'W', 'Y'): 4, ('K'): 5, ('J', 'X'): 8, ('Q', 'Z'): 10}
def score1(word,scores):
    score = 0
    for letter in word:
        for k in scores:
            if letter in k:
                score = score + scores[k]
    return score
                
def score2(word,scores_raw):
    scores = {}
    for k in scores_raw:
        for letter in k:
            scores[letter] = scores_raw[k]
    score = 0
    for letter in word:
        score = score + scores[letter]
    return score

print("Hello,", score1("Hello", composite_scores))
print("Goodbye,", score1("Goodbye", composite_scores))
print("Bonjour,", score1("Bonjour", composite_scores))
print("Hello,", score2("Hello", composite_scores))
print("Goodbye,", score2("Goodbye", composite_scores))
print("Bonjour,", score2("Bonjour", composite_scores))