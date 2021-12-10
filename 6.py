a = int(input("Введите номер квартиры: "))
pod = a/36+1
etaz = (a-(pod-1)*36)/4+1
print("Подъезд: ", pod," , этаж: ", etaz)