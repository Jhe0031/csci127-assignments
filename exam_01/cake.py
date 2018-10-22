def divide(A, B, u):
    slice = (A/B)*u
    i = 0
    even_odd = 0
    while i < 10:
        if i*slice == 1:
            even_odd += 1
            invitees = i
        i += 1
    if even_odd == 0:
        return "None. If the cake is not even, there is no party."
    elif even_odd > 0:
        return invitees
print('Invitees:', divide(5, 10, 1))
print('Invitees:', divide(4, 8, 2))
print('Invitees:', divide(5, 10, .5))
print('Invitees:', divide(3, 9, 1))
print('Invitees:', divide(3, 4, 1))