def greeter(name):
    return "Hello " + name + "!"
print(greeter("Stan"))

def repeat_string(word):
    return word+word

print(greeter ("Stan"))
print(greeter("Ollie"))
print(repeat_string("hello"))
                    
def hello_name(name):
  return "Hello " + name + "!"
print (hello_name('Bob'))
print (hello_name('Alice'))
print (hello_name('X'))

def make_abba(a, b):
  return a + b + b + a
print (make_abba('Hi', 'Bye'))
print (make_abba('Yo', 'Alice'))
print (make_abba('What', 'Up'))
                    
def make_tags(tag, word):
  return "<" +  tag + ">" + word + "</" + tag + ">"
print (make_tags('i', 'Yay'))
print (make_tags('i', 'Hello'))
print (make_tags('cite', 'Yay'))

def make_out_word(out, word):
  return out[:2] + word + out[2:]
print (make_out_word('<<>>', 'Yay'))
print (make_out_word('<<>>', 'WooHoo'))
print (make_out_word('[[]]', 'word'))
                    
def extra_end(str):
  return str[-2:] + str[-2:] + str[-2:]
print (extra_end('Hello'))
print (extra_end('ab'))
print (extra_end('Hi'))

def first_two(str):
    return str[:2]
print (first_two('Hello'))
print (first_two('abcdefg'))
print (first_two('ab'))

def first_half(str):
  return str[:len(str)/2]
print (first_half('WooHoo'))
print (first_half('HelloThere'))
print (first_half('abcdef'))
