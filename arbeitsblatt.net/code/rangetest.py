z = 10 * 1000 * 1000
show_n = 1000000

print("range:")
for i in range(0, z):
    if i % show_n == 0:
        print(i)

print("while:")
i = 0
while i < z:
    if i % show_n == 0:
        print(i)
    i = i + 1
