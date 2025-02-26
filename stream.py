import pandas as pd
import google.generativeai as genai
import streamlit as st
import io

# Configure the API key
genai.configure(api_key="")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to generate summary
def generate_summary(row):
    input_text = f"Change Title: {row['Change Title']}\nProblem: {row['Problem']}\nChange Objective: {row['Change Objective']}\nGenerate summary in 100 words."
    response = model.generate_content([input_text])
    return response.text

def generate_summary_from_text(text_file):
     prompt = f"Generate summary in 100 words\n{text_file}"
     response = model.generate_content([prompt])
     return response.text

# Streamlit UI
st.title("Summary Generator")


# File uploader
uploaded_file = st.file_uploader("Choose a file to generate summary ", type=["xlsx", "csv", "txt"])

if uploaded_file:

    file_type = uploaded_file.name.split(".")[-1]

    if file_type == 'xlsx':
        output = io.BytesIO()
        df = pd.read_excel(uploaded_file)  # Read the Excel file
        with st.spinner("Generating summaries, Please wait a While..."):
            df['Summary'] = df.apply(generate_summary, axis=1)
        df.to_excel(output, index=False, engine='openpyxl')
        mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        output.seek(0)
        st.write(df.head())


    elif file_type =='csv':
        output = io.BytesIO()
        df = pd.read_csv(uploaded_file)  #Read the csv file
        with st.spinner("Generating summaries, Please wait a While..."):
            df['Summary'] = df.apply(generate_summary, axis=1)
        df.to_csv(output, index=False)
        output.seek(0)
        mime_type = "text/csv"
        st.write(df.head())

            
    elif file_type == 'txt':
        output = io.BytesIO()
        df = pd.read_csv(uploaded_file, delimiter= '\t')
        with st.spinner("Generating summaries, Please wait a While..."):
             summary = df.apply(generate_summary_from_text)
        summary.to_csv(output, index = False, sep = '\t')
        mime_type = "text/plain"
        output.seek(0)
        st.write(summary)

    st.write("Data uploaded successfully")

    # Provide a download button
    st.download_button(
        label="Download Summary",
        data=output,
        file_name=f"summary.{file_type}",
        mime= mime_type
    )

