n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    coef = 1
    for j in range(i + 1):
        print(coef, end=" ")
        coef = coef * (i - j) // (j + 1)
    print()
