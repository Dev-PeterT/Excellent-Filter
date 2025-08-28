import pandas as pd
from config_loader import load_config

def sort_data(data_set):
    # Load all the sorting properties and rules
    sorting_rules = load_config("sorting_rules")
    sorting_properties = load_config("sorting_properties")

    # Builds a map to sort the data into
    sorted_categories = {}
    for group, categories in sorting_properties.items():
        for category, items in categories.items():
            for item in items:
                sorted_categories[item] = (group, category)

    # Sorts the data into the map created earlier
    sorted_data = {}
    for group, categories in sorting_properties.items():
        sorted_data[group] = {}
        for category in categories.keys():
            # Filter rows for the group/category
            mask = data_set[sorting_rules["sorting_column"]].isin(sorting_properties[group][category])
            subset = data_set[mask]

            # Always store total count
            sorted_data[group][category] = {"total": len(subset)}

    print(sorted_data)