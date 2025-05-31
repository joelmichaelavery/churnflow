#Entry point for scripts

from src.load_data import load_dataset #load the load_dataset function
import pandas as pd #import pandas for working my dataset into a dataframe
import seaborn as sns #import seaborn for visualization
import matplotlib.pyplot as plt #import matplotlib to show the visualization

if __name__ == "__main__": #main driver of my program
    df = load_dataset("data/data.csv") #loading the data set from data/data.csv via load dataset()
   # print(df.head()) was to show the first 5 rows, but just for testing

    #df.info() getting valuable insight on information in the dataset
    #df.isnull().sum() Shows me how many Columns have null values and how many. 
    #print(df["Dependents"].unique()) #A yes or no should be a 1 or 0
    #print(df["TotalCharges"].sample(10))

    #print(df[df["TotalCharges"].str.strip() == ""]) #Look for Non-Numeric Strings in Total Charges

    # Drop 11 rows where TotalCharges is an empty string so it can be safely converted to float
    df = df[df["TotalCharges"].str.strip()!= ""]
    #Converting Total Charges to float
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    print(df["TotalCharges"].dtype) #Should show float64
    print(df.info()) #Confirm its no longer object

    #visualization tools to comare Contract to churn
    sns.countplot(data=df, x='Contract', hue="Churn")
    plt.show()

    #boxplot to show churn versus monthly charges
    sns.boxplot(data=df, x="Churn", y="MonthlyCharges")
    plt.show()