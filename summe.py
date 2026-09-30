summe = 0

for zahl in range(1, 1001):
    if zahl % 4 == 0 and zahl % 6 != 0:
        summe += zahl

print("Summe:", summe)
