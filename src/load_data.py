#Loads data from the datadset and converts into a dataframe using pandas
import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)
    return df