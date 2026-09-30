zahl = int(input("Gib eine Primzahl ein: "))

ist_prim = zahl > 1
for i in range(2, int(zahl ** 0.5) + 1):
    if zahl % i == 0:
        ist_prim = False
        break

print(ist_prim)
