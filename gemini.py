import google.generativeai as genai
genai.configure(api_key = "AIzaSyBjKe4Wk6CUtT0oSG1pUaq4Sn0ER90JpGY")
model = genai.GenerativeModel(model_name= "gemini-1.5-flash")
response = model.generate_content(["I want to know the meaning of life"])
print(response)