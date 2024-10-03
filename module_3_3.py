def print_params(a, b, c):
    print(a, 25, [1,2,3])
    print(a, b, c)
    print(b)
    print()

print_params(1, "Строка", True)
values_list = ("Дмитрий", False, 777)
values_dict = {"a": True, "b": 4, "c": "Столбец"}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = (4, "Крест")
print_params(*values_list_2, 42)