class InvalidDataError(Exception):
    pass
n = int(input())
for i in range(1, n + 1):
    data = input()
    try:
        name, age, height = data.split(",")
        age = int(age)
        height = float(height)
        if age < 0 or height <= 0.0:
            raise InvalidDataError
        print(f"Row {i}: Success")
    except ValueError:
        print(f"Row {i}: Format Error")
    except InvalidDataError:
        print(f"Row {i}: Logical Error")