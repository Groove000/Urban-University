def print_params(a = 1, b = "Строка", c = True):
    print(a, b, c)
    print(a, b)
    print(c)
    print()

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = ("Дмитрий", False, 777)
values_dict = {"a": True, "b": 4, "c": "Столбец"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)
