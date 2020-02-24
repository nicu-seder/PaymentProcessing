import datetime

import numpy as np
import pandas as pd


class Estimator:
    def __init__(self):
        self._dataset = None
        self._prediction_dataset = None

    def fit(self, dataset: pd.DataFrame):
        self._dataset = dataset.copy()

    def predict(self, stock_name: str, year: str, month: str, day: str):
        date = datetime.date(int(year), int(month), int(day))
        if self._stock_name_exists(stock_name) and any(self._dataset["date"].dt.month == date.month):
            self._prediction_dataset = self._dataset.loc[
                (self._dataset["stock"] == stock_name) & (self._dataset["date"].dt.month == date.month)]
            estimated_price = np.mean(self._prediction_dataset["mid_range_price"])
            print(f'Estimated price for stock {stock_name} is: {estimated_price}')
        else:
            print("Wrong data")

    def _stock_name_exists(self, stock_name: str):
        return any(self._dataset["stock"] == stock_name)
