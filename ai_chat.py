from google import genai

# حط المفتاح بتاعك هنا
client = genai.Client(api_key="YOUR_API_KEY")

# ابعت السؤال
response = client.models.generate_content(
    model="gemini-3.5-flash-lite", # الموديل ده مجاني وسريع
    contents="قولي جملة واحدة عن فايدة البرمجة"
)

# اطبع الرد
print(response.text)