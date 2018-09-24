#Partners: Christopher He & Jia Qi He

def fizzbuzz(max_value):
    i = 1
    fizzbuzz = 0
    while  i <= max_value:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            fizzbuzz = fizzbuzz + 1
        elif i % 3 == 0:
            print("fizz")
            fizz = fizz + 1
        elif i % 5 == 0:
            print("buzz")
            buzz = buzz + 1
        else:
            print(i)
        i = i + 1
    return(fizzbuzz)
print("# of 'fizzbuzz' = " + str(fizzbuzz(100)))