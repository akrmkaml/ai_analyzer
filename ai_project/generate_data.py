import pandas as pd
import random
import numpy as np

# قائمة منتجاتنا
products = ["Laptop", "Phone", "Tablet", "Headphones", "Keyboard", "Mouse", "Monitor", "Printer", "Camera", "Speaker"]
prices = {"Laptop": 1000, "Phone": 500, "Tablet": 300, "Headphones": 50, "Keyboard": 80, "Mouse": 20, "Monitor": 200, "Printer": 150, "Camera": 400, "Speaker": 100}

# هنعمل 200 سطر بيانات
data = []
for _ in range(200):
    product = random.choice(products)
    price = prices[product]
    
    # بنحط نسبة 10% إن السعر يكون ناقص (None)
    if random.random() < 0.1:
        price = np.nan
        
    quantity = random.randint(1, 20)
    
    # بنحط نسبة 5% إن الكمية تكون ناقصة
    if random.random() < 0.05:
        quantity = np.nan
        
    data.append({"Product": product, "Price": price, "Quantity": quantity})

# بنعمل جدول
df = pd.DataFrame(data)

# بنضيف شوية صفوف مكررة عمداً (10 صفوف من أول 10)
df = pd.concat([df, df.head(10)], ignore_index=True)

# بنحفظ الملف
df.to_csv("big_sales_data.csv", index=False)
print("Done! Generated big_sales_data.csv with 210 rows.")