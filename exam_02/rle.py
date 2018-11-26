def encode(s):
    list = []
    count = 0
    i = 0
    while i <= len(s)-1:
        if i == len(s)-1:
            count += 1
            list.append([s[i], str(count)])
        elif s[i] == s[i+1]:
            count += 1
        elif s[i] != s[i+1]:
            count += 1
            list.append([s[i], str(count)])
            count = 0
        i += 1
    return list
print(encode("abbaaacddaaa"))
print(encode("abcd"))
print(encode("cbbbbbdee"))

##Not complete
##new_s = []
##def decode():

### In class solution
def rle1(line):
    encoded = []
    i = 0
    while i < len(line)-1:
        next_letter = i+1
        while next_letter < len(line) and line[next_letter] == line[i]:
            next_letter = next_letter + 1
        encoded.append([next_letter-i, line[i]])
        i = next_letter
    if i == len(line)-1:
        encoded.append([1, line[i]])
    return encoded
print(rle1("abbaaacddaaa"))
print(rle1("abcd"))
print(rle1("cbbbbbdee"))

def rle2(line):
    encoded = []
    count = 1
    prevchar = line[0]
    for c in line[1:]:
        if c == prevchar:
            count += 1
        else:
            encoded.append([count, prevchar])
            count = 1
            prevchar = c
    encoded.append([count, prevchar])
    return encoded
print(rle2("abbaaacddaaa"))
print(rle2("abcd"))
print(rle2("cbbbbbdee"))

def decode(encoded):
    result = ""
    for item in encoded:
        result = result + item[0] * item[1]
    return result
x = rle2("abbbbbcddeeaabbaaffe")
print(decode(x))