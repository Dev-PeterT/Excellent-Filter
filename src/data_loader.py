import pandas as pd

from pathlib import Path

def load_data():
    # Base script's pathy by script location and not working directory
    script_directory = Path(__file__).parent
    input_folder = script_directory.parent / "input"

    # Gets all the excel files within the input folder 
    excel_files = list(input_folder.glob("*.xlsx"))

    # Checks if there is more than one excel file or none
    if len (excel_files) == 0:
        raise FileNotFoundError("❌ There is no excel file found in the 'input' folder. Please add one.")
    elif len (excel_files) > 1:
        raise ValueError("❌ There are too many excel files in the 'input' folder. Only 1 file is allowed.")
    
    file_path = excel_files[0]
    print(f"📂 Loading file: {file_path.name}")

    # Load the excel file into DataFrame
    data_frame = pd.read_excel(file_path, header=None)

    return data_frame