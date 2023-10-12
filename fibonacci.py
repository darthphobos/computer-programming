how_deep = int(input("how deep do you want to go into the fibonacci?"))
x = 0
y = 1 
z = y
count = 1

while count <= how_deep:
    print(f"{z}")
    count += 1
    x, y = y, z
    z = x + y 