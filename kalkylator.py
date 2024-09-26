#int
numder = 6
#float
fnumber = 5.8
#str
name = "Denis"
#bool
status = True
#coments

a = 10
b = 2
c = a % 3

a = 10
#унарный минус
a = -a
a = a


what = input ("Что делать? (+, -, *, /): ")
a = float(input("введи первое число: "))
b = float(input("введи второе число: "))

if what == "+":
    c = a + b
    print(" Результат: " + str(c))
elif what == "-":
    c = a - b
    print(" Результат: " + str(c))
elif what == "*":
    c = a * b
    print(" Результат: " + str(c))
elif what == "/":
    c = a / b
    print(" Результат: " + str(c))
else:
    print("Выбрана не верная операция!")



