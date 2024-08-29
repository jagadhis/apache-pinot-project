import pandas as pd
import json
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the input and output file paths
input_csv = os.path.join(current_dir, 'Electric_Vehicle_Population_Data.csv')
output_json = os.path.join(current_dir, 'Electric_Vehicle_Population_Data.json')

# Read the CSV file
df = pd.read_csv(input_csv)

# Convert the DataFrame to a list of dictionaries
records = df.to_dict('records')

# Write the JSON file
with open(output_json, 'w') as f:
    json.dump(records, f)

print(f"Conversion complete. JSON file saved as {output_json}")