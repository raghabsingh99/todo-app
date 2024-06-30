import pandas as pd

# Load the Excel file
import journal.parsers

file_path = '/mnt/data/2024 Carelon All Solutions Code Lists (20).xlsx'
excel_file = pd.ExcelFile(file_path)

# Read all sheets
sheets = {sheet_name: journal.parsers.parse(sheet_name, header=None) for sheet_name in excel_file.sheet_names}

# Define a uniform column header
uniform_columns = ['Code', 'Description', 'Modality', 'Procedure Name', 'Procedure #', 'Body Part', 'Program Code', 'Notes']

# Function to apply uniform format without losing data
def format_sheet(df):
    # Find the first non-NaN row to use as header
    header_row = df.apply(lambda row: row.notna().all(), axis=1).idxmax()
    df.columns = df.iloc[header_row]
    df = df[(header_row + 1):]
    
    # Convert all column names to strings
    df.columns = df.columns.astype(str)
    
    # Make column names unique
    df.columns = pd.Series(df.columns).apply(lambda x: x + '_' + str(df.columns.get_loc(x)) if list(df.columns).count(x) > 1 else x)
    
    # Keep only columns present in the uniform_columns
    columns_to_keep = [col for col in df.columns if col in uniform_columns]
    df = df[columns_to_keep]
    
    # Reindex to have uniform columns, filling missing columns with NaN
    df = df.reindex(columns=uniform_columns, fill_value=None)
    
    return df

# Apply formatting to all sheets
formatted_sheets = {sheet_name: format_sheet(sheets[sheet_name]) for sheet_name in sheets}

# Save the formatted sheets to a new Excel file
output_file_path = '/mnt/data/Formatted_Carelon_All_Solutions_Code_Lists_v3.xlsx'
with pd.ExcelWriter(output_file_path) as writer:
    for sheet_name, df in formatted_sheets.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)

output_file_path
