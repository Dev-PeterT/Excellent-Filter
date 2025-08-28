import re
import pandas as pd
from config_loader import load_config

def sort_data(data_set):
    # Load all the sorting properties and rules
    sorting_rules = load_config("sorting_rules")
    sorting_properties = load_config("sorting_properties")

    sub_column = sorting_rules.get("sub_sorting_column", "")
    sub_categories = sorting_rules.get("sub_sorting_categories", {})

    # Builds a map to sort the data into
    sorted_categories = {}
    for group, categories in sorting_properties.items():
        for category, items in categories.items():
            for item in items:
                sorted_categories[item] = (group, category)

    # Sorts the data into the map created earlier
    sorted_data = []
    for group, categories in sorting_properties.items():
        for category in categories.keys():
            mask = data_set[sorting_rules["sorting_column"]].isin(sorting_properties[group][category])
            subset = data_set[mask]

            row_data = {
                "Group": group,
                "Category": category,
                "Total": len(subset)
            }

            # Only execute if the column exists
            if "sub_sorting_rules" in sorting_rules:
                for rule in sorting_rules["sub_sorting_rules"]:
                    sub_column = rule.get("sub_sorting_column", "")
                    sub_categories = rule.get("sub_sorting_categories", {})

                    # Only execute if the column exists
                    if sub_column and sub_column in subset.columns:
                        for sub_name, keywords in sub_categories.items():
                            # Normalize column and keywords
                            column_values = subset[sub_column].astype(str).str.strip().str.lower()
                            escaped_keywords = [kw.strip().lower() for kw in keywords]

                            # Count rows where column contains any of the keywords
                            filtering_data = column_values.apply(lambda x: any(kw in x for kw in escaped_keywords))
                            row_data[sub_name] = filtering_data.sum()

            sorted_data.append(row_data)

    # Convert to DataFrame
    sorted_data_df = pd.DataFrame(sorted_data)
    print(sorted_data_df)