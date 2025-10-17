def harmonic(n):
    if n < 2:
        return 1
    else:
        return 1 / n + harmonic(n-1)
    
print(harmonic(3))