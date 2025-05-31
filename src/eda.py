from src.load_data import load_dataset

def show_churn_distribution(df):
    print(df["Churn"].value_counts())
    print(df["Churn"].value_counts(normalize=True))
    