# Partners: Rachel Tieu & Jia Qi He

def vowel_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: That string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    name_start = name[0]
    if name_start in vowels:
        return(name + "ay")
    else:
        return name[1:] + name[0] + "ay"
    
print(vowel_pig_latin("apple"))
print(vowel_pig_latin("Orange"))
print(vowel_pig_latin("Hello"))
print(vowel_pig_latin("bye"))