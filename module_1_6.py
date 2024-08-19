my_dict = {'Dima': 1996, 'Artem': 1996, 'Lisa': 1997, 'Nadya': 1987}
print(my_dict)
print(my_dict ['Dima'])
print(my_dict.get('Yakov'))
my_dict ['Irina'] = 1974
print(my_dict)

my_dict.update({'Boris': 2002,
                'Ivan': 2004})
print(my_dict)

a=my_dict.pop('Dima')
print(a)
print(my_dict)

#множества
my_set = {3, 5, 3, 7, 1, 2, 5, 9, 5, 7, 'Apple', 'Coconut', 'Apple', 'Peach', 'Coconut', (34, 56)}
print(my_set)
print(my_set.remove(3))
print(my_set)
print(my_set.add(11))
print(my_set)