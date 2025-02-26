import pandas as pd
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyBjKe4Wk6CUtT0oSG1pUaq4Sn0ER90JpGY")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Load the Excel file
file_path = "D:\\ArtificialIntelligence\\Book1.xlsx"
output_file_path = "D:\\ArtificialIntelligence\\summary.xlsx"
df = pd.read_excel(file_path)
print("DataFrame loaded successfully:")
print(df.head())

# Function to generate summary and inspect the response
def generate_summary(input_text):
    response = model.generate_content([input_text])
    print("Response from API:")
    print(response)
    return response

# Loop through each row in the DataFrame to inspect the response
for index, row in df.iterrows():
    input_text = f"Change Title: {row['Change Title']}\nProblem: {row['Problem']}\nChange Objective: {row['Change Objective']}\nGenerate a 200-word summary."
    response = generate_summary(input_text)
    break  # Stop after the first request to inspect the response

# Assuming the structure of the response is known now, modify the generate_summary function accordingly
def generate_summary(input_text):
    response = model.generate_content([input_text])
    print("Response from API:")
    print(response)
    
    # Extract the generated text from the response
    if hasattr(response, 'generations') and len(response.generations) > 0:
        return response.generations[0].text
    return ""

# Loop through each row in the DataFrame to update the summary column
for index, row in df.iterrows():
    input_text = f"Change Title: {row['Change Title']}\nProblem: {row['Problem']}\nChange Objective: {row['Change Objective']}\nGenerate a 200-word summary."
    summary = generate_summary(input_text)
    df.at[index[-1], 'Summary'] = summary
    print(f"Row {index} updated with summary: {summary}")

# Save the DataFrame back to the Excel file
df.to_excel(output_file_path, index=False)

print("Summaries generated and saved successfully.")
