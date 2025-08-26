from config_loader import load_config

def filter_data(config_option: str, data_set):
    # Loads the desired filters
    filter_config = load_config("filter")[config_option]
    filters = filter_config.get("filters", [])

    # Remove unnecessary rows and columns
    data_set = data_set.drop(filter_config.get("remove_row", []), axis=0).reset_index(drop=True) # Remove row(s)
    data_set = data_set.drop(filter_config.get("remove_columns", []), axis=1) # Remove column(s)

    # Loop through the filter steps based on the config option
    for filter_step in filters:

        # Checks if the column exists
        if filter_step["column"] in data_set.columns:
            filtering_column = data_set[filter_step["column"]]

            # Checks for json flag (0 / 1) to check by value or check by containing
            if filter_step["contains_flag"] == 1:
                filtering_data = filtering_column.str.contains('|'.join(filter_step["filtering"]), na=False)
            else:
                filtering_data = filtering_column.isin(filter_step["filtering"]) | filtering_column.isna()
                
            data_set = data_set[~filtering_data].reset_index(drop=True)


    return data_set