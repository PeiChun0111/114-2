import pandas as pd

class SalesManager:
    def __init__(self, data):
        # Create DataFrame
        self.df = pd.DataFrame(data, columns=["Region", "SalesAmount"])

    def sales_report(self):
        # Group by Region and sum sales
        result = self.df.groupby("Region", as_index=False)["SalesAmount"].sum()
        
        # Sort by total sales in descending order
        result = result.sort_values(by="SalesAmount", ascending=False)
        
        return result

N = int(input())
data = []

for _ in range(N):
    region, amount = input().split()
    data.append([region, int(amount)])

manager = SalesManager(data)
report = manager.sales_report()

for _, row in report.iterrows():
    print(row["Region"], int(row["SalesAmount"]))