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
print( c )

a = 10
#унарный минус
a = -a
a = a
print( a )


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

what = input ("Что делать? (+, -, *, /")
a = input("введи первое число: ")
b = input("введи первое число: ")
