def suma_dobles(n):
    if n == 1:
        return 2
    else:
        return 2*n + suma_dobles(n-1)

print(suma_dobles(4))