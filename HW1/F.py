class LibraryItem:
    def __init__(self, title, days_overdue):
        self.title = title
        self.days_overdue = days_overdue
    def calculate_late_fee(self):
        return self.days_overdue * 5
class Book(LibraryItem):
    def calculate_late_fee(self):
        if self.days_overdue <= 7:
            return self.days_overdue * 5
        else:
            return 7 * 5 + (self.days_overdue - 7) * 10
class DVD(LibraryItem):
    def calculate_late_fee(self):
        return self.days_overdue * 20
class Magazine(LibraryItem):
    def calculate_late_fee(self):
        fee = self.days_overdue * 5
        return min(fee, 50)
n = int(input())
items = []
for _ in range(n):
    data = input().split()
    item_type = data[0]
    title = data[1]
    days = int(data[2])
    if item_type == "Book":
        item = Book(title, days)
    elif item_type == "DVD":
        item = DVD(title, days)
    elif item_type == "Magazine":
        item = Magazine(title, days)
    items.append(item)
for item in items:
    print(f"{item.title} Fee: ${item.calculate_late_fee()}")