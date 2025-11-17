# 곱셈

def multiply():
    str1 = input()
    str2 = input()

    for _ in range(2, -1, -1):
        print(int(str1) * int(str2[_]))

    print(int(str1) * int(str2))

multiply()