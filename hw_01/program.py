# Part 1
def capitalize_name(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    """
    capitalized = name.title()
    return capitalized
print(capitalize_name("james bond"))
print(capitalize_name("angelina jolie"))
print(capitalize_name("jennifer anniston"))

# Part 2
def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F, Last" where it's a capitalized first initial
    and capitalized last name
    """
    space_index = name.find(" ")
    first = name[0:space_index]
    last = name[space_index+1:]
    initial = first[:1].title() + ", " + last.title()
    return initial
print(init("james bond"))
print(init("angelina jolie"))
print(init("jennifer anniston"))

# Part 3
def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: That string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    pig_latin =  name[1:] + name[:1] + "ay"
    return pig_latin
print(part_pig_latin("sugar"))
print(part_pig_latin("name"))
print(part_pig_latin("testing"))

# Part 4
def make_out_word(out, word):
    """
    Given an "out" string length 4, such as "<<>>", and a word, return a new
    string where the word is in the middle of the out string, e.g. "<<word>>".
    """
    return out[:2] + word + out[2:]
print (make_out_word('<<>>', 'Yay'))
print (make_out_word('<<>>', 'WooHoo'))
print (make_out_word('[[]]', 'word'))

# Part 5
def make_tags(tag, word):
    """ 
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as
    italic text. In this example, the "i" tag makes <i> and </i> which surround
    the word "Yay". Given tag and word strings, create the HTML string with tags
    around the word, e.g. "<i>Yay</i>".
    """
    return "<" +  tag + ">" + word + "</" + tag + ">"
print (make_tags('i', 'Yay'))
print (make_tags('i', 'Hello'))
print (make_tags('cite', 'Yay'))