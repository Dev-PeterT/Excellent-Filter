from config_loader import load_config

def filter_data(config_option: str, data_set):
    # Loads the desired filters
    filter_config = load_config("filter")
    selected_config = filter_config[config_option]

    # Remove unnecessary rows and columns
    data_set = data_set.drop(selected_config["initial_remove_row"], axis = 0) # Remove row(s)
    data_set = data_set.drop(selected_config["initial_remove_columns"], axis = 1) # Remove column(s)

    # Remove unnecessary and "blank/empty" data
    filter_column = data_set.iloc[:, selected_config["initial_filter_column"]]
    filter_values = filter_column.isin(selected_config["initial_filter_options"]) | filter_column.isna()
    data_set = data_set[~filter_values].reset_index(drop=True)

    return data_set
