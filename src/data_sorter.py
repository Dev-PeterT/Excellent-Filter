import re
import pandas as pd
from config_loader import load_config

def sort_data(config_option, data_set):
    # Work on a copy so original dataset is untouched
    working_sorted_data = data_set.copy()

    # Load the sorting properties config
    sorting_properties = load_config("sorting_properties")

    # Build the key dynamically
    sort_key = "sorting_properties_" + config_option

    # Exit early if no sorting instructions for this config
    if sort_key not in sorting_properties:
        print(f"⚠️ No sorting instructions found for '{config_option}'. Exiting module.")
        return {
            "filtered_data": working_sorted_data
        }

    sorted_data = []

    # Loop through each sorting category defined in JSON for this config
    for category_config in sorting_properties[sort_key].get("sorting_category", []):
        sorting_name = category_config.get("sorting_name", "")
        filtering_column = category_config.get("filtering_column", "")
        filtering_information = category_config.get("filtering_information", [])
        sub_sorting_rules = category_config.get("sub_sorting_rules", [])

        # Skip if the filtering column doesn't exist in dataset
        if not filtering_column or filtering_column not in working_sorted_data.columns:
            continue

        # Normalize both column values and filtering information
        column_values = working_sorted_data[filtering_column].astype(str).str.strip().str.lower()
        escaped_keywords = [kw.strip().lower() for kw in filtering_information]

        # Filter rows where column contains ANY of the keywords
        mask = column_values.apply(lambda x: any(kw in x for kw in escaped_keywords))
        subset = working_sorted_data[mask]

        # Skip empty subsets
        if subset.empty:
            continue

        row_data = {
            "Category": sorting_name,
            "Total": len(subset)
        }

        # Process sub-sorting rules if any
        for rule in sub_sorting_rules:
            sub_column = rule.get("sub_filtering_column", "")
            sub_categories = rule.get("sub_filtering_categories", {})

            if sub_column and sub_column in subset.columns:
                column_values = subset[sub_column].astype(str).str.strip().str.lower()

                for sub_name, keywords in sub_categories.items():
                    escaped_keywords = [kw.strip().lower() for kw in keywords]
                    filtering_data = column_values.apply(lambda x: any(kw in x for kw in escaped_keywords))
                    row_data[sub_name] = filtering_data.sum()

        sorted_data.append(row_data)

        # Remove the matched rows from working_data
        working_sorted_data = working_sorted_data.drop(subset.index)

    # Convert results to DataFrame
    sorted_data = pd.DataFrame(sorted_data)
    print(sorted_data)
    
    print(working_sorted_data)

    return {
        "sorted_data": sorted_data,
        "working_sorted_data": working_sorted_data
    }