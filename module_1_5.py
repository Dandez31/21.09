immutable_var = ([10, 20, 30, 40, 50],"an","be","ci")
print("Незменяемый объект 'Кортеж':" + str(immutable_var))
print(type(immutable_var))
name = list(immutable_var)
name [0] = 1000, 2000, 3000
print(name)
print(type(name))
print('Кортеж (tuple) не поддерживает обращение по элементам\n')
mutable_list = [10, 20, 'an', 'brown', 'Modified']
print("Изменяемый объект 'Список':", mutable_list)
print(type(mutable_list))
mutable_list[0]='умеет'
mutable_list[1]='плавает'
mutable_list[4]='BEAR'
print("Измененный Список:", mutable_list)