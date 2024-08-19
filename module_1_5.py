immutable_var_ = 1, False, 'hello'
print(immutable_var_)
immutable_var_

#нельзя изменить значения элемента кортеж, так как кортеж не поддерживает обращение по элементам

mutable_list = [1, False, 'hello']
print(mutable_list)
mutable_list[0]=[2]
mutable_list.append(True)
mutable_list.remove(False)
mutable_list.reverse()
print(mutable_list)