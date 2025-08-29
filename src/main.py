from data_loader import load_data
from data_filter import filter_data
from data_sorter import sort_data

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
        config_choice = "A"
        print("✅ You have selected option 'A'")

    elif choice == "B":
        config_choice = "B"
        print("✅ You have selected option 'B'")  

    else:
        print("❌ Invalid choice. Please run the program again and choose A or B.")

    # Filter and sort excel data
    filtered_data = filter_data(config_choice, data_set)
    results = sort_data(config_choice, filtered_data)

    # Base script's pathy by script location and not working directory
    script_directory = Path(__file__).parent
    output_folder = script_directory.parent / "output"
    
    # Export data
    for name, data_files in results.items():
        output_path = output_folder / f"{name}.xlsx"
        data_files.to_excel(output_path, index=False)

    print(f"✅ Files saved to: {output_folder}")