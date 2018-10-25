import random

def build_random_list(items, max_value):
    """
    create and return a list filled with items number of element
    each element should be a random integer value
    between 0 and 99
    """
    l = []
    while len(l) < items:
        l.append(random.randint(0, max_value))
        l = l + [random.randint(0, max_value)]
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

def freq(l, number):
    count = 0
    for item in l:
        if item == number:
            count += 1
    return count
print('Frequency of 10:', freq(l, 10))