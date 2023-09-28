print('1 - прямоугольник 2 - треугольник 3 - круг')
a = int(input('Выберите фигуру: '))

if a == 1:
        print("Введите стороны прямоугольника:")
        b = int(input("b = "))
        c = int(input("c = "))
        a = b*c
        print (a)

elif a == 2:
        print("Введите высоту и основание треугольника:")
        h = int(input("h = "))
        c = int(input("c = "))
        a  = (c*h)/2
        print (a)

elif a == 3:
        r = int(input(" Введите радиус = "))
        print((3.14 * r ** 2))
        print (r)
elif a >= 4:
        print("ошибка")
