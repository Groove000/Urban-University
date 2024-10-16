def test_function(x):
    d = x ** 2
    def inner_function(x):
        if d % 2 == 0:
            print ("Я в области видимости функции test_function")
    inner_function (x)
    return d

a = test_function(2)
print(a)

def test_function(x):
    global d
    d = x ** 2
    def inner_function(x):
        if d % 2 == 0:
            print ("Я в области видимости функции test_function")
    inner_function (x)
    return d

a = inner_function(2)
print(a)