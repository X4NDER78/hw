#H/W Hillel
#1 Задача: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.

first = 10
second = 30

sum = first + second
print(sum)

sub = first - second
print(sub)

multi = first * second
print(multi)

div = first / second
print(div)

div2 = first % second
print(div2)

sqr = first ** second
print(sqr)

div3 = first // second
print(div3)

#2 Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1. Виведіть на екран результат кожного порівняння.

res1 = sum > sub
print(res1)

res2 = div < multi
print(res2)

res3 = div >= div3
print(res3)

res4 = multi <= sqr
print(res4)

res5 = div3 == div2
print(res5)

res6 = div3 != multi
print(res6)

#3 Задача: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". Виведіть на екран.

str1 = 'Hello'
str2 = 'World'

S = (str1 + ' ' + str2)
print(S)
