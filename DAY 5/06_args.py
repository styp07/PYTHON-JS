def suma(*args):
    total = 0
    for i in args:
        total +=  i
    return total

print(suma(2, 6, 7))