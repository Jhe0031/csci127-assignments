#Partners: Christopher He & Jia Qi He

i = 1
fizz = 0
buzz = 0
fizzbuzz = 0
while  i <= 100:
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
print("fizzbuzz done!")
print("# of fizz = " + str(fizz))
print("# of buzz = " + str(buzz))
print("# of fizzbuzz = " + str(fizzbuzz))