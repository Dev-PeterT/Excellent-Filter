from data_loader import load_data
from data_filter import filter_data

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

    # Determine user input
    if choice == "A":
        config_choice = "option_A"
        print("✅ You have selected option 'A'")

    elif choice == "B":
        config_choice = "option_B"
        print("✅ You have selected option 'B'")    

    else:
        print("❌ Invalid choice. Please run the program again and choose A or B.")


    data_set = filter_data(config_choice, data_set)
    print(data_set)


    # Base script's pathy by script location and not working directory
    script_directory = Path(__file__).parent
    output_folder = script_directory.parent / "output"

    # Export modified data as excel in output folder
    output_file = output_folder / "output.xlsx"
    data_set.to_excel(output_file, index=False)
    print(f"✅ File saved to: {output_file}")