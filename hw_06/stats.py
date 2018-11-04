import random

def build_random_list(items, max_value):
    """
    create and return a list filled with items number of element
    each element should be a random integer value
    between 0 and 99
    """
    l = []
    while len(l) < items:
        l.append(random.randint(1, max_value))
        l = l + [random.randint(1, max_value)]
    return l
l = build_random_list(100, 10)
print(l)

def max(l):
    largest = 0
    for item in l:
        if item > largest:
            largest = item
    return largest
print('Largest Number:', max(l))

def freq(l, val):
    count = 0
    for item in l:
        if item == val:
            count += 1
    return count
print('Frequency of 10:', freq(l, 10))
print('Frequency of 9:', freq(l, 9))
print('Frequency of 8:', freq(l, 8))
print('Frequency of 7:', freq(l, 7))
print('Frequency of 6:', freq(l, 6))
print('Frequency of 5:', freq(l, 5))
print('Frequency of 4:', freq(l, 4))
print('Frequency of 3:', freq(l, 3))
print('Frequency of 2:', freq(l, 2))
print('Frequency of 1:', freq(l, 1))

def mode(l):
    most = 0
    for number in l:
        if freq(l, number) >= most:
            most = freq(l, number)
            a_mode = number
    return a_modeca
print('Mode:', mode(l))

