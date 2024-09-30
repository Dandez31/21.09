#Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
from module_1_2 import numder

#Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
#Например: 'Aaron' - [5, 3, 3, 5, 4]
#Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

#Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика, а значением - его средний балл.

#Вывод в консоль:
#{'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}    # Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
averagescores = {}  # создадим пустой словарь (средних баллов)
# Упорядочим имена учеников из Множества students для создания ключей словаря
names = list(students)  # преобразуем множество
names.sort()            # в упорядоченный список
# Заполним словарь средними баллами учеников
averagescores.update({names[0]:sum(grades[0])/len(grades[0]), names[1]:sum(grades[1])/len(grades[1])})
averagescores.update({names[2]:sum(grades[2])/len(grades[2]), names[3]:sum(grades[3])/len(grades[3])})
averagescores.update({names[4]:sum(grades[4])/len(grades[4])})
print('Средние баллы учеников -', averagescores)
numbers = [4, 8, 6, 5, 3, 2], [1, 2, 6, 7, 8,]
students = {'John', 'Bilbo'}
average = {}
names = list(students)
names.sort()
average.update({names[0]:sum(numbers[0]) / len(numbers[0]), names[1]:sum(numbers[1]) / len(numbers[1])})
print(average)
