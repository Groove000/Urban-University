data_structure = [
[1, 2, 3],                                  # 6
{'a': 4, 'b': 5},                           # 11
(6, {'cube': 7, 'drum': 8}),                # 29
"Hello",                                    # 5
((), [{(2, 'Urban', ('Urban2', 35))}])      # 48
]


def calculate_structure_sum(arg):
    total = 0
    if isinstance(arg, (int, float)):
        total += arg
    elif isinstance(arg, str):
        total += len(arg)
    elif isinstance(arg, (list, tuple, set)):
        for element in arg:
            total += calculate_structure_sum(element)
    elif isinstance(arg, dict):
        for key, value in arg.items():
            total = total + calculate_structure_sum(value) + calculate_structure_sum(key)
    return total


result = calculate_structure_sum(data_structure)
print('Cумма всех чисел и длин всех строк:',result)