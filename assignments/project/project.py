import pandas as pd
import time

def train_model(data):
    # Train a model to predict fake news
    y = data["fraudulent"]
    return clf

if __name__ == "__main__":
    # Load data
    data = pd.read_csv("../data/job_train.csv")
    # Replace missing values with empty strings
    data = data.fillna("")
    # Train model
    clf = train_model(data)



    
    

