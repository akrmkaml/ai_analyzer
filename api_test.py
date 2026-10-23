import requests

# 1. ده عنوان الـ API اللي هنكلمه
url = "https://open.er-api.com/v6/latest/USD"

# 2. بنبعت طلب (Request) للموقع
response = requests.get(url)

# 3. بنتأكد إن الرد تمام (رقم 200 معناه كل حاجة شغالة)
if response.status_code == 200:
    # 4. بنحول الرد لصيغة بايثون بتفهمها (JSON)
    data = response.json()
    
    # 5. بنسحب سعر الجنيه المصري من البيانات
    egypt_price = data["rates"]["EGP"]
    
    print("1 USD =", egypt_price, "EGP")
else:
    print("Failed to get data")