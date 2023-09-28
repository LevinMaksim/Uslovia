x = int(input('Введите 1 число: '))
y = int(input('Введите 2 число: '))
z = int(input('Введите 3 число: '))

if (x > y and x < z) or (x > z and x < y):
        print(x)
elif (y > x and y < z) or (y > z and y < x):
        print(y)
elif (z > x and z < y) or (z > y and z < x):
        print(z)
elif x == y or x == z or y == z:
        print("Нет")
