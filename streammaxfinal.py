import pandas as pd
import google.generativeai as genai
import streamlit as st
import io

# Configure the API key
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Define prompts list
prompts = [
    "Generate summary in 100 words for CR_NO: {CR_NO}, Change Description: {Change_Description}, Justification: {Justification}.",
    "Provide a brief overview in 100 words for CR_NO: {CR_NO}, Change Description: {Change_Description}, Justification: {Justification}.",
    "Summarize in 100 words CR_NO: {CR_NO}, Change Description: {Change_Description}, Justification: {Justification}."
]

# Function to generate summary
def generate_summary(prompt_text):
    response = model.generate_content([prompt_text])
    return response.text

def generate_summary_from_text(text_file):
    prompt = f"Generate summary in 100 words{text_file}"
    response = model.generate_content([prompt])
    return response.text

# Streamlit UI
st.title("Summary Generator")

# Button creation
option = st.selectbox(
    "Choose input type",
    ("Text", "Excel", "CSV")
)

if option == "Excel":
    file = st.file_uploader("Choose an Excel file", type=["xlsx"])
    if file:
        if st.button("Upload and Generate Summary"):
            buffer = io.BytesIO()
            df = pd.read_excel(file)  # Read the Excel file

            # Iterate through rows and generate summaries for each prompt
            for index, row in df.iterrows():
                for i, prompt in enumerate(prompts):
                    prompt_text = prompt.format(
                        CR_NO=row.get('CR_NO', ''),
                        Change_Description=row.get('Change Description', ''),
                        Justification=row.get('Justification', '')
                    )
                    summary = generate_summary(prompt_text)
                    summary_column = f'Summary {i+1}'
                    df.at[index, summary_column] = summary

            df.to_excel(buffer, index=False, engine='openpyxl')
            buffer.seek(0)
            st.write(df.head())
            st.download_button(
                label="Download Summary",
                data=buffer,
                file_name="summary.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

elif option == "CSV":
    file = st.file_uploader("Choose a CSV file", type=["csv"])
    if file:
        if st.button("Upload and Generate Summary"):
            buffer = io.BytesIO()
            df = pd.read_csv(file)  # Read the CSV file

            # Iterate through rows and generate summaries for each prompt
            for index, row in df.iterrows():
                for i, prompt in enumerate(prompts):
                    prompt_text = prompt.format(
                        CR_NO=row.get('CR_NO', ''),
                        ChangeDescription=row.get('Change Description', ''),
                        Justification=row.get('Justification', '')
                    )
                    summary = generate_summary(prompt_text)
                    summary_column = f'Summary {i+1}'
                    df.at[index, summary_column] = summary

            df.to_csv(buffer, index=False)
            buffer.seek(0)
            st.write(df.head())
            st.download_button(
                label="Download Summary",
                data=buffer,
                file_name="summary.csv",
                mime="text/csv"
            )

elif option == 'Text':
    text_input = st.text_area("Paste your text here")
    if st.button("Generate Summary"):
        if text_input:
            summary = generate_summary_from_text(text_input)
            st.write("Summary:")
            st.write(summary)
        else:
            st.warning("Please paste some text to generate a summary.")
