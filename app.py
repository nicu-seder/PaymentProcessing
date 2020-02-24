from estimator import Estimator
from payment_gateway import *
from reader import Reader
from request import *
import numpy as np


class App:
    def __init__(self):
        self._payment_gateway = None

    def process_payment(self, request_to_process: Request):
        amount_value = request_to_process.get_amount()
        if amount_value < 20:
            self._payment_gateway = CheapPaymentGateway(amount_value, 200)
        elif amount_value > 20 and amount_value < 501:
            self._payment_gateway = ExpensivePaymentGateway(True, amount_value, 400)
        else:
            self._payment_gateway = PremiumPaymentGateway(amount_value, 500)
        self._payment_gateway.initialize_payment()

    def estimate_price(self, stock_name: str, year: str, month: str, day: str) -> float:
        """
        Estimates price of the stock sent as parameter. Based on the date which is sent as parameter, it takes the
        month from the date and filters all the stock_name stocks which have a date in the specified month and does
        the average of the mid range price (average between high and low price)
        :param stock_name: stock name for which we try to predict
        :param year:
        :param month:
        :param day:
        :return: returns the prediction
        """
        reader = Reader()
        self._dateset = reader.load_data("./dow_jones_index.csv")
        self._dateset = reader.clean_data(self._dateset)

        estimator = Estimator()
        estimator.fit(self._dateset)
        stock_prediction = estimator.predict(stock_name, year, month, day)
        return stock_prediction
