import json
import pandas as pd
import os
from pandas import json_normalize

def flatten_json_to_excel(json_data, excel_file_path, num_columns=10):
    """
    Converts a JSON object to an Excel file with the specified number of columns.
    Handles nested JSON data by flattening it.

    Parameters:
        json_data (dict or list): The JSON data to convert.
        excel_file_name (str): The name of the output Excel file.
        num_columns (int): The maximum number of columns to include in the Excel.
    """
    # Flatten the JSON data using json_normalize
    if isinstance(json_data, list):
        flat_data = json_normalize(json_data)
    else:
        flat_data = json_normalize([json_data])
    
    # Truncate or limit columns to the specified number
    if len(flat_data.columns) > num_columns:
        flat_data = flat_data.iloc[:, :num_columns]

    # Create the directory if it doesn't exist
    output_dir = os.path.dirname(excel_file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save the data to an Excel file
    flat_data.to_excel(excel_file_path, index=False)
    print(f"Data successfully written to {excel_file_path}")
    print(flat_data)
    return flat_data

# Example JSON (replace with your generative AI JSON output)
json_data = [
    {
        "name": "John Doe",
        "age": 30,
        "skills": {
            "technical": ["Python", "SQL"],
            "soft": ["Communication", "Problem-solving"]
        },
        "projects": [
            {"title": "AI Research", "year": 2023},
            {"title": "Data Science", "year": 2022}
        ]
    },
    {
        "name": "Jane Smith",
        "age": 28,
        "skills": {
            "technical": ["R", "Tableau"],
            "soft": ["Leadership", "Critical Thinking"]
        },
        "projects": [
            {"title": "Healthcare Analytics", "year": 2021}
        ]
    }
]


            
excel_file_path = "Downloads\\output.xlsx"
# Convert the JSON to Excel
flatten_json_to_excel(json_data, excel_file_path, num_columns=10)
