import pandas as pd

# 1. اقرأ الملف
df = pd.read_csv("sales.csv")
print("--- Data ---")
print(df)

# 2. احسب إجمالي كل منتج
df["Total"] = df["Price"] * df["Quantity"]
print("\n--- Data with Total ---")
print(df)

# 3. إجمالي المبيعات
print("\nTotal Sales:", df["Total"].sum())

# 4. أعلى منتج مبيعاً
best_seller = df.loc[df["Total"].idxmax(), "Product"]
print("Best Seller:", best_seller)