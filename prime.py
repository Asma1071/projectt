
primzahlen = []

for zahl in range(2, 10000):
    if all(zahl % i != 0 for i in range(2, zahl)):
        primzahlen.append(zahl)

print(primzahlen[999] + 2026)