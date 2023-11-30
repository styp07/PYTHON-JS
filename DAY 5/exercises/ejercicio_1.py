def devolver_distintos(a, b, c):
    list = [a, b, c]
    suma = sum(list)
    if suma > 15:
        return max(list)
    elif suma < 10:
        return min(list)
    else:
        list.sort()
        return list[1]
    
print(devolver_distintos(1,8,3))