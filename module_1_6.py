#2. Работа со словарями:
  #- Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
#Например: Имя(str)-Год рождения(int).
  #- Выведите на экран словарь my_dict.
  #- Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
  #- Добавьте ещё две произвольные пары того же формата в словарь my_dict.
 #- Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
 # - Выведите на экран словарь my_dict.
#3. Работа с множествами:
 # - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
 # - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
 # - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
  #- Удалите один любой элемент из множества my_set.
 # - Выведите на экран измененное множество my_set.

#Примечания:
#- Для вывода значений на экран используйте функцию print().
#- Помните, что словарь и множество - неупорядоченные коллекции.
#- Больше о методах словарей тут, множеств тут.

#Пример результата выполнения программы:
#Dict: {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
#Existing value: 2002
#Not existing value: None
#Deleted value: 1999
#Modified dictionary: {'Vasya': 1975, 'Kamila': 1981, 'Artem': 1915, 'Masha': 2002}

#Set: {1, 'Яблоко', 42.314}
#Modified set: {'Яблоко', 42.314, 13, (5, 6, 1.6)}
my_dict = {"Denis": 1998, "Richard": 1996, "Smit": 1995}
print("Dict: " + str(my_dict) )
print("Existing value: " + str(my_dict["Richard"]))
print("Not existing value: " + str(my_dict.get("Kamila")))
print("Deleted value: " + str(my_dict.pop("Smit")))
my_dict.update({"Kamila": 1994, "Serg": 1993})
print("Modified dictionary: " + str(my_dict) + "\n")

my_set = {1, "Pineapple", 3.14,}
print("Set: " + str(my_set))
my_set.add(5)
my_set.add(111)
my_set.add((1, 5, 6))
my_set.discard(3.14)
#my_set.remove(1)
print("Modified set: " + str(my_set))


