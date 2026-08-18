import pandas as pd
from src.config import DATASET_FILE

def load_raw_data() -> pd.DataFrame:
    """
    Loads the raw dataset from the pickle file.
    
    Returns:
        pd.DataFrame: The loaded raw dataset.
    """
    # Assuming the data is stored as a pandas DataFrame in the pickle file
    return pd.read_pickle(DATASET_FILE)
