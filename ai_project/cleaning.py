import pandas as pd
import numpy as np

# 1. بنعمل جدول فيه بيانات ناقصة (بنستخدم None عشان نمثل القيمة الناقصة)
data = {
    "Name": ["Ahmed", "Sara", "Ali", None, "Mona"],
    "Age": [25, np.nan, 22, 30, 28],
    "City": ["Cairo", "Alexandria", None, "Giza", "Luxor"]
}

df = pd.DataFrame(data)
print("--- Original Data ---")
print(df)
# بنحذف أي صف فيه أي قيمة ناقصة
df_cleaned = df.dropna()
print("\n--- After Dropping Missing Values ---")
print(df_cleaned)
# بنعوض القيم الناقصة بقيمة افتراضية (مثلاً "Unknown" للأسماء والمدن)
df_filled = df.fillna("Unknown")
print("\n--- After Filling Missing Values ---")
print(df_filled)
# بنحسب متوسط الأعمار ونعوض بيه القيمة الناقصة
avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)
print("\n--- After Filling Age with Average ---")
print(df)
# عمل جدول فيه تكرار
data_dup = {
    "Name": ["Ahmed", "Sara", "Ahmed", "Ali"],
    "Age": [25, 30, 25, 22]
}

df_dup = pd.DataFrame(data_dup)
print("\n--- Data with Duplicates ---")
print(df_dup)

# حذف التكرار
df_no_dup = df_dup.drop_duplicates()
print("\n--- After Removing Duplicates ---")
print(df_no_dup)
# عمود الأعمار كنصوص
df_types = pd.DataFrame({"Age": ["25", "30", "22"]})
print("\nData Types Before:\n", df_types.dtypes)

# تحويل النص لرقم
df_types["Age"] = pd.to_numeric(df_types["Age"])
print("\nData Types After:\n", df_types.dtypes)
df_rename = pd.DataFrame({"First Name": ["Ahmed"], "Age (Years)": [25]})

# تغيير الأسماء
df_rename = df_rename.rename(columns={"First Name": "Name", "Age (Years)": "Age"})
print("\n--- After Renaming ---")
print(df_rename)