import google.generativeai as genai
genai.configure(api_key = "")
model = genai.GenerativeModel(model_name= "gemini-1.5-flash")
response = model.generate_content(["I want to know the meaning of life"])
print(response)
