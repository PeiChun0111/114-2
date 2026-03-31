import pandas as pd

class Inventory:
    def __init__(self, data):
        # Create DataFrame
        self.df = pd.DataFrame(data, columns=["ItemName", "Price", "Quantity"])

    def calculate_total_value(self):
        # Create Total_Value column
        self.df["Total_Value"] = self.df["Price"] * self.df["Quantity"]
        return self.df[["ItemName", "Total_Value"]]

N = int(input())
data = []

for _ in range(N):
    item, price, quantity = input().split()
    data.append([item, int(price), int(quantity)])

inventory = Inventory(data)
result = inventory.calculate_total_value()

for _, row in result.iterrows():
    print(row["ItemName"], int(row["Total_Value"]))