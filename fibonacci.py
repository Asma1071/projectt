MIN_STELLEN = 100

a, b = 0, 1  
index = 0

while len(str(a)) < MIN_STELLEN:
    a, b = b, a + b
    index += 1

print(index)
