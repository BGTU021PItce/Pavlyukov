x = int(input("Введите расстояние между вами и ближайшим столбом: "))
y = int(input("Введите расстояние между столбами: "))
n = int(input("Введите номер столба: "))

for i in range(n-1):
	print(i, x)
	x += y
print(x)