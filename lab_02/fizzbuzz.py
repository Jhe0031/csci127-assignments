#Partners: Christopher He & Jia Qi He

def fizzbuzz(max_value):
    i = 1
    count = 0
    while  i <= max_value:
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end = ", ")
            count = count + 1
        elif i % 3 == 0:
            print("Fizz", end = ", ")
        elif i % 5 == 0:
            print("Buzz", end = ", ")
        else:
            print(i, end = ", ")
        i = i + 1
    return(count)
print("# of 'FizzBuzz' = " + str(fizzbuzz(100)))