x = int(input("Введите расстояние между вами и ближайшим столбом: "))
y = int(input("Введите расстояние между столбами: "))
n = int(input("Введите номер столба: "))
z = int(input("Введите кол-во метров: "))

length = z*n
length -= x

step = length//y
if step < 0:
	step = 0
print(step)