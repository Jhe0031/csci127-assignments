def compress_word(w):
    """
    Return a new string that's formed by first taking the first letter of w and then removing the vowels from the rest of w.
    """
    w = w.lower()
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    new = []
    i = 0
    while i < len(w):
        if w[i] == w[0]:
            new.append(w[i])
        elif w[i] not in vowels:
            new.append(w[i])
        i += 1
    return ''.join(new)
print(compress_word("halloween"))
print(compress_word("Special"))
print(compress_word("apple"))

def sentence(line):
    line = compress_word(line)
    return line
print(sentence("I like to eat apple pie"))
print(sentence("Who is there"))