
numbers = [4, 8, 6, 5, 3, 2], [1, 2, 6, 7, 8,], [4,5,3,4,5]
students = {'John', 'Bilbo', 'Gloria'}
average = {}
names = list(students) #множество в список
names.sort()
average.update({names[0]:sum(numbers[0]) / len(numbers[0]), names[1]:sum(numbers[1]) / len(numbers[1])})
average.update({names[2]:sum(numbers[2]) / len(numbers[2])})
print(average)

numbers = [4, 8, 6, 5, 3, 2]
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

average = sum(numbers) / len(numbers)
print(average)