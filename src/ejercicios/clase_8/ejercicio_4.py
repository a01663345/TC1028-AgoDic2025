"""
N = 6

*
**
***
****
*****
******
"""


def main():
    n = int(input("N: "))
    fila = 1
    while fila <= n:
        # print("*" * fila)
        res = ""
        x = 1
        while x <= fila:
            res += "*"
            x += 1

        print(res)
        fila += 1


main()
