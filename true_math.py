from math import inf

def true_divide(first, second):
    if second == 0:
        return inf
    else:
        return (first / second)

result1 = true_divide(49, 7)
result2 = true_divide(15, 0)
print(result1)
print(result2)