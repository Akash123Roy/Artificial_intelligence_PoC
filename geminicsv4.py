import pandas as pd
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Load the Excel file
file_path = "D:\\ArtificialIntelligence\\Book1.xlsx"
output_file_path = "D:\\ArtificialIntelligence\\summary.xlsx"
df = pd.read_excel(file_path)
print("DataFrame loaded successfully:")
print(df.head())

# Function to generate summary
def generate_summary(input_text):
    response = model.generate_content([input_text])
    print("Response from API:")
    print(response)
    
    # Check the response structure and extract the generated text
    if response and 'content' in response and isinstance(response['content'], list) and len(response['content']) > 0:
        return response['content'][0].get('text', '')
    return ""

# Add a new column 'Summary' with default empty string
df['Summary'] = ''

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    input_text = f"Change Title: {row['Change Title']}\nProblem: {row['Problem']}\nChange Objective: {row['Change Objective']}\nGenerate a 200-word summary."
    summary = generate_summary(input_text)
    df.at[index, 'Summary'] = summary
    print(f"Row {index} updated with summary: {summary}")

# Save the DataFrame back to the Excel file
df.to_excel(output_file_path, index=False, engine='openpyxl')

print("Summaries generated and saved successfully.")
