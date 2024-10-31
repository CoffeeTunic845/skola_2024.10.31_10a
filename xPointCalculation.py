import os
os.system('cls')
print("\n")
import math

a = float(input("A vērtība: "))
b = float(input("B vērtība: "))
c = float(input("C vērtība: "))

d = b**2 - 4 * a * c

if d > 0:
    r1 = (-b + math.sqrt(d)) / (2 * a)
    r2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"X1: {r1} un X2: {r2}")
elif d == 0:
	r = -b / (2 * a)
	print(f"X: {r}")
else:
    print("Sakņu nav!")