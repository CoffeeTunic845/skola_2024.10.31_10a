import os
os.system('cls')
print("\n")

# x = int(input("X vērtība: "))
# y = int(input("Y vērtība: "))

# if x < y:
#     print("X ir mazāks par Y")
# elif x == y:
#     print("X ir vienāds ar Y")
# elif x > y:
#     print("X ir lielāks par Y")
# else:
#     print("Ir neiespējami sakitļi")

punkti = int(input("Punkti: "))

if punkti >= 90 and punkti <= 100:
    print("Vērtējums: 10")
elif punkti >=80 and punkti < 90:
    print("Vērtējums: 9")
elif punkti >=70 and punkti < 80:
    print("Vērtējums: 9")
elif punkti >=60 and punkti < 70:
    print("Vērtējums: 7")
else:
    print("Vērtējums: n/v")