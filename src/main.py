from data_loader import load_data
from config_loader import load_config

from pathlib import Path

if  __name__ == "__main__":
    # Load data first
    data_set = load_data()

    print(data_set)
    
    # Inquire with user the goal to determine as the final result
    print("What would you like the program to determine as the final result?")
    print("[Option A: ]")
    print("[Option B: ]")
    choice = input("Enter your choice (A/B): ").strip().upper()

    initial_filter_config = load_config("initial_filter")

    # Determine user input
    if choice == "A":
        print("✅ You have selected option 'A'")
        selected_config = initial_filter_config["option_A"]

        data_set = data_set.drop(selected_config["remove_rows"], axis = 0) # Remove row(s)
        data_set = data_set.drop(selected_config["remove_columns"], axis = 1) # Remove column(s)
    elif choice == "B":
        print("✅ You have selected option 'B'")
        selected_config = initial_filter_config["option_B"]

        data_set = data_set.drop(selected_config["remove_rows"], axis = 0) # Remove row(s)
        data_set = data_set.drop(selected_config["remove_columns"], axis = 1) # Remove column(s)
    else:
        print("❌ Invalid choice. Please run the program again and choose A or B.")

    print(data_set)


    # Base script's pathy by script location and not working directory
    script_directory = Path(__file__).parent
    output_folder = script_directory.parent / "output"

    # Export modified data as excel in output folder
    output_file = output_folder / "output.xlsx"
    # data_set.to_excel(output_folder, index=False)