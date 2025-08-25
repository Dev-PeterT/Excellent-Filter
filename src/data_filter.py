from config_loader import load_config

def filter_data(config_option: str, data_set):
    # Loads the desired filters
    filter_config = load_config("filter")
    selected_config = filter_config[config_option]

    # Remove unnecessary rows and columns
    data_set = data_set.drop(selected_config.get("initial_remove_row", []), axis=0).reset_index(drop=True) # Remove row(s)
    data_set = data_set.drop(selected_config.get("initial_remove_columns", []), axis=1) # Remove column(s)

    # Remove unnecessary and "blank/empty" data
    filter_column = data_set[selected_config["initial_filter_column"]]
    filter_values = filter_column.isin(selected_config["initial_filter_options"]) | filter_column.isna()
    data_set = data_set[~filter_values].reset_index(drop=True)

    # Specific data filtering by config option
    if config_option == "option_A":
        print("Testing")

    elif config_option == "option_B":
        filter_column = data_set[selected_config["secondary_filter_column"]]
        filter_values = filter_column.isin(selected_config["secondary_filter_options"]) | filter_column.isna()
        data_set = data_set[~filter_values].reset_index(drop=True)

        filter_column = data_set[selected_config["tertiary_filter_column"]]
        filter_values = filter_column.str.contains('|'.join(selected_config["tertiary_filter_options"]), na=False)
        data_set = data_set[~filter_values].reset_index(drop=True)

    return data_set