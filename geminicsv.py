import pandas as pd
import google.generativeai as genai

# Configure the API key
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Load the Excel file
file_path = "D:\\ArtificialIntelligence\\Book1.xlsx"
output_file_path = "D:\\ArtificialIntelligence\\summary.xlsx"
df = pd.read_excel(file_path)

# Function to generate summary
def generate_summary(row):
    input_text = f"Change Title: {row['Change Title']}\nProblem: {row['Problem']}\nChange Objective: {row['Change Objective']}\nGenerate a 200-word summary."
    response = model.generate_content([input_text])
    return response.text  # Print the response to understand its structure
    
# Apply the function to each row in the DataFrame
df['Summary'] = df.apply(generate_summary, axis=1)

# Save the DataFrame back to the Excel file
df.to_excel(output_file_path, index=False)
