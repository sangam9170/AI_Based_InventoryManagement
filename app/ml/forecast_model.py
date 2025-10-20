import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

MODEL_PATH = os.path.join("models", "linear_regression_model.pkl")

class DemandForecaster:
    def __init__(self):
        self.model = LinearRegression()
    
    def train(self, sales_df: pd.DataFrame):
        X = sales_df[['week_number']]
        y = sales_df['quantity_sold']
        self.model.fit(X, y)
        with open(MODEL_PATH, "wb") as f:
            pickle.dump(self.model, f)
    
    def predict(self, last_week: int):
        return int(self.model.predict([[last_week + 1]])[0])
