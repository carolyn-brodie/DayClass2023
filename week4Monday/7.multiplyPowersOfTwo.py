#multiply the first n powers of 2

base = 2
total = 1
numberOfPowers = 50
for exponent in range(numberOfPowers):
    total = total * (base ** exponent)
print("total =", total)
