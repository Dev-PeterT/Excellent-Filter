from data_loader import load_data
from config_loader import load_config

if  __name__ == "__main__":
    data_set = load_data()
    
    initial_filter_config = load_config("initial_filter")
