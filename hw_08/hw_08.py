#Partners: Jia Qi He & Kyra Abbu

def build_word_count(words):
    d={}
    for word in words.split():
        d.setdefault(word,0)
        d[word]=d[word]+1
    return d

def clean_apos(string):
    result = ""
    result = result + string[0]
    for i in range(1,len(string)):
        if string[i] == "'":
            if string[i+1] == "s":
                result = result + ""
        elif string[i] == "s":
            if string[i-1] == "'":
                result = result + ""
            else:
                result = result + string[i]
        else:
            result = result + string[i]
    return result

def clean_data(string):
    alphabet = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    punctuations = """`~!@#$%^&*()_+{}[]|\:"<>?;',./"""
    result = "" #string
    string = clean_apos(string)
    for a in string:
        if a in alphabet:
            result = result + a.lower()
        elif a in punctuations:
            result = result + ""
        else:
            result = result + " "
    return result

filename="moby-small.txt"

f = open(filename)
s = f.read()

words_uncleaned = build_word_count(s)

words_cleaned = clean_apos(s)

words_cleanagain = clean_data(words_cleaned)

words_count = build_word_count(words_cleanagain)

vals = words_count.values()
vals = sorted(vals)

common_words = []
key_words = []
for key in words_count:
    if words_count[key] > 1:
        common_words.append([key,words_count[key]])
        key_words.append(key)
print("COMMON WORDS COUNT:",common_words)

word_after = {}
cleaned = words_cleanagain.split()
key_words = key_words
print("\nCOMMON WORDS:",key_words)

for i in range(1,len(cleaned)-1):
    if cleaned[i] in key_words:
        element = cleaned[i]
        word_after.setdefault(element,[])
        word_after[element].append(cleaned[i+1])
print("\nWORD(S) AFTER COMMON WORDS:",word_after)