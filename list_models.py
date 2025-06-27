import google.generativeai as genai

genai.configure(api_key="AIzaSyDBEOkkn3tkrAWbj-EDepT9yOOkl2j74jY")

model = genai.GenerativeModel("models/gemini-1.5-flash")
response = model.generate_content("Give me 3 Spanish words with translations.")

print(response.text)
