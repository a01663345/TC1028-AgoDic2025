def suma(a: int, b: int) -> tuple[int, int]:
    a = a + 1
    b = b + 2
    print(a, b)
    return a, b


p = 1
q = 2
p, q = suma(p, q)
print(p, q)  # 1, 2
