import pandas as pd
import numpy as np

class DataPipeline:
    def __init__(self, data):
        # Create DataFrame
        self.df = pd.DataFrame(data, columns=["Category", "Item", "Price"])
        # Convert Price to numeric, coerce 'NaN' strings to actual NaN
        self.df["Price"] = pd.to_numeric(self.df["Price"], errors="coerce")

    def process(self):
        # Fill NaN with mean price per Category
        self.df["Price"] = self.df.groupby("Category")["Price"] \
                                  .transform(lambda x: x.fillna(x.mean()))
        
        # Group by Category and sum prices
        result = self.df.groupby("Category", as_index=False)["Price"].sum()
        
        # Sort alphabetically by Category
        result = result.sort_values(by="Category")
        
        return result

N = int(input())
data = []

for _ in range(N):
    category, item, price = input().split()
    data.append([category, item, price])

pipeline = DataPipeline(data)
result = pipeline.process()

for _, row in result.iterrows():
    print(row["Category"], int(round(row["Price"])))