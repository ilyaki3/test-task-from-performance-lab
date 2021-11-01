"""
				Task2
	Напишите программу, которая рассчитывает положение точки относительно окружности.
Координаты центра окружности и его радиус считываются из файла1.
Пример:
1 1
5
	Координаты точек считываются из файла2.
Пример:
0 0
1 6
6 6
	Файлы передаются программе в качестве аргументов. Файл с координатами и радиусом окружности - 1 аргумент,
файл с координатами точек - 2 аргумент.
Координаты в диапазоне float. Количество точек от 1 до 100.
Вывод каждого положения точки заканчивается символом новой строки.
	Соответствия ответов:
0 - точка лежит на окружности
1 - точка внутри
2 - точка снаружи
"""


def in_circle(circle_coord, dot_coord):
	circle_radius = circle_coord[2]
	x_dot = dot_coord[0] - circle_coord[0]
	y_dot = dot_coord[1] - circle_coord[1]

	if circle_radius >= ((x_dot ** 2 + y_dot ** 2) ** 0.5):
		return 0
	elif circle_radius > ((x_dot ** 2 + y_dot ** 2) ** 0.5):
		return 1
	else:
		return 2


circle = []
radius = []
dot = []
with open('file1.txt', 'r', encoding='utf-8') as f1:
	n = True
	for line in f1:
		if n:
			circle.append(list(map(float, line.split())))
			n = False
		else:
			radius.append(float(line.strip('\n')))
			n = True
for i in range(len(circle)):
	circle[i].append(radius[i])

with open('file2.txt', 'r', encoding='utf-8') as f2:
	for line in f2:
		dot.append(list(map(float, line.split())))

for j in range(len(circle)):
	for k in range(len(dot)):
		print(in_circle(circle[j], dot[k]))
