n = int(input())
for _ in range(n):
    x, y = input().split()
    try:
        a = int(x)
        b = int(y)
        print(a // b)
    except ValueError:
        print("Error: Invalid input")
    except ZeroDivisionError:
        print("Error: Division by zero")