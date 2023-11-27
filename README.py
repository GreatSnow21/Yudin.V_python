####################################
# краткий конспект по 1-му занятию #
####################################

# с решётки начинается комментарий

# создадим переменную a и присвоем
# ей целочисленное значение (int)
a = 10

# имя переменной может быть любым

# переменной b присвоим значение
# с плавающей точкой (float):
b = 10.5

# здесь переменной c присваивается
# строка (str):
c = "строка может быть любой"
# строки всегда берутся в кавычки.
# двойные или одинарные — без
# разницы, но принято придержи-
# ваться одного стиля внутри
# одного кода

# переопределим переменную c:
c = "строка может быть"

# значение типа список (list)
# может содержать любые типы,
# а так же другие переменные.
# элементы пишутся через запятую
# в [квадратных скобках]:
d = [10, 50, 876, "строка", b]

# список может содержать и другие
# переменные. как в примере выше,
# b без кавычек — это не строка, а
# имя переменной

# в списке и строке можно брать
# отдельный элемент, указывая его
# индекс в квадратных скобках
# (начиная с нуля), например:
c[1]
# вернёт строку "т"
d[4]
# вернёт 10.5 (переменная b)

# можно указать диапазон, тогда
# получим часть последовательности
# того же типа
print(c[0:4])
# выведет в консоль строку "стро"
print(d[2:4])
# выведет список [876, 'строка']

# обратите внимание: print() — это
# функция. для вызова функции надо
# написать скобки после имени,
# даже если они пустые. print() с
# пустыми скобочками напечатает в
# консоль пустую строку, а без
# скобок не выполнится

# создадим список строк
bag = ["apple", "pineapple", "lemon"]

# теперь мы можем пробегать по
# нему с помощью конструкции
# for элемент in переменная:
for fruit in bag:
    print(fruit)
# слову fruit по очереди при-
# сваивается значение с каждого
# элемента (как в объявлении
# переменной). а потом для каждого
# взятого значения выполняется код
# print(fruit)

# помощью дополнительного отступа
# можно можно вызывать вложенный
# цикл внутри каждой итерации
# верхнего цикла:
for fruit in bag:
    for letter in fruit:
        print(letter)
    print()
# напечатает каждый фрукт, по букве
# на строку.
# в конце каждого фрукта — пустую
# строку (отступ вызова print()
# вернулся на уровень назад)


#################################
# а теперь немного drawbot-skia #
#################################

# для использования функций из
# библиотеки drawbot-skia нам
# нужно сначала импортировать их
# в наш код:
from drawbot_skia.drawbot import rect

# здесь мы импортируем функцию
# rect, рисующую прямоугольник

# теперь мы можем её вызвать,
# указыв положение и размер
# прямоугольника
#    x    y   w    h
rect(500, 50, 100, 100)

# но чтобы увидеть его, нам надо
# сохнанить файл в pdf, а для
# этого импортировать ещё одну
# функцию — saveImage
from drawbot_skia.drawbot import saveImage

# можно было бы дописать её в
# первый импорт, вот так:
# from drawbot_skia.drawbot import rect, saveImage
# но мы уже импортировали её
# отдельным выражением

# теперь можем сохранить pdf:
saveImage("output-01.pdf")

# нарисуем ещё несколько квадратов
# циклом! для этого создадим пере-
# менную x с начальной позицией
x = 150
# определим величину шага
step = 150
# напишем цикл для рисования:
for i in range(5):
    rect(x, 400, 100, 100)
    # врнутри каждой итерации
    # будем увеличивать x на step
    x = x + step

# сохраним под новым именем
saveImage("output-02.pdf")

# список поддерживаемых функций:
# https://github.com/justvanrossum/drawbot-skia/issues/5
# информацию о них можно читать на
# https://www.drawbot.com/
# например, справка по примитивам:
# https://www.drawbot.com/content/shapes/primitives.html

# чтобы добавить функцию в свой
# код, сначала добавте её в импорт

#############
# задание 1 #
#############

# напишите цикл, рисующий по
# вертикали фигуры (квадраты
# или другие из ссылки выше)

#############
# задание 2 #
#############

# напишите вложенный (двойной)
# цикл, заполняющий холст фигурами
# полностью, по вертикали и
# горизонтали

##########################
# задание дополнительное #
# творческое, свободное  #
##########################
