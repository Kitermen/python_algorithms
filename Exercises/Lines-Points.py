import math

A = int(input("Enter the A: "))
B = int(input("Enter the B: "))
C = int(input("Enter the C: "))

x = int(input("Enter the x(point): "))
y = int(input("Enter the y(point): "))

if A == 0 or B == 0 or C == 0:
    print("Podano złe wartości!!!")
    exit()
else:
    A = A * -1
    C = C * -1
    if B != 1:
        A /= B
        C /= B
        a = A
        b = C

if y == a * x + b:
    print("Punkt leży na prostej")
else:
    distance = (A * x + B * y + C) / math.sqrt(A**2 + B**2)
    print(f"Punkt leży w odległości {distance} od prostej")


print(a, b)