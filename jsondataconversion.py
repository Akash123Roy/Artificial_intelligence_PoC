import pandas as pd
import json

# Sample JSON input
json_data = {
"title": "",
"intro": "",
"recovery process": [{"wfid":["stage1:this is my data","stage2:this is my data","stage3:this is my data"], "wfid2":["stage1:this is my data","strage2:this is my data","stage3:this is my data"]},{"wfid3":["stage1:this is my data","stage2:this is my data","stage3:this is my data"],"wfid4":["stage1: this is my data","stage2:this is my data","stage3:this is my data"]}],
"appendices": ""
}

# Parse recovery process
recovery_process = json_data["recovery process"]

# Prepare data for the Excel file
def create_excel_structure(json_data):
    rows = []

    for item in json_data:
        for wfid, stages in item.items():
            rows.append([wfid])  # Add WFID as a separate row
            stage_headers = []
            stage_values = []
            
            for stage in stages:
                key, value = stage.split(":")
                stage_headers.append(key)
                stage_values.append(value)

            # Append stage headers and values as separate rows
            rows.append(stage_headers)
            rows.append(stage_values)

            # Add empty rows for separation
            rows.append([])
            rows.append([])

    # Create a DataFrame
    df = pd.DataFrame(rows)

    return df

# Generate the structured DataFrame
data = create_excel_structure(recovery_process)

# Save to Excel
output_file = "Downloads\\replicated_structure.xlsx"
data.to_excel(output_file, index=False, header=False)

output_file
