import pandas as pd
from google import genai

# 1. Setup AI
API_KEY = "YOUR_API_KEY_HERE"client = genai.Client(api_key=API_KEY)

# 2. Read and Clean Data
print("1. Reading and cleaning data...")
df = pd.read_csv("big_sales_data.csv")

# Remove duplicates
df = df.drop_duplicates()
# Fill missing values (Price with mean, Quantity with 0)
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Quantity"] = df["Quantity"].fillna(0)

# Calculate total sales per product
df["Total"] = df["Price"] * df["Quantity"]

# Save clean data
df.to_csv("sales_clean.csv", index=False)
print("   -> Clean data saved as 'sales_clean.csv'")

# 3. Prepare summary for AI
total_sales = df["Total"].sum()
best_product = df.loc[df["Total"].idxmax(), "Product"]
summary_data = f"Total Sales: {total_sales} EGP. Best product: {best_product}. Full data:\n{df.to_string()}"

# 4. Send data to AI
print("\n2. Asking AI to analyze the data...")
prompt = f"You are a data analyst. Based on this sales data, write a short professional report in English:\n{summary_data}"

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

# 5. Print and save report
print("\n--- AI REPORT ---")
print(response.text)

# Save report to a file
with open("Final_Report.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("\n3. Report saved as 'Final_Report.txt'")