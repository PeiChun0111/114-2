items = input().split()
m = int(input())
for _ in range(m):
    idx = input()
    try:
        i = int(idx)
        print(items[i])
    except ValueError:
        print("Error: Invalid index type")
    except IndexError:
        print("Error: Index out of bounds")