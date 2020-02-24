class PaymentGateway:
    """
    PaymentGateway parent class from which different type of PaymentGateways are derived
    """

    # check if amount to be paid comes as string and should be transformed to float
    def __init__(self, amount_to_be_paid, payment_success_code):
        self._amount_to_be_paid = amount_to_be_paid
        self._payment_success_code = payment_success_code

    def initialize_payment(self):
        """
        Response when the payment is initialized
        :return:
        """
        if self._payment_success_code == 200:
            print("200 OK")
        elif self._payment_success_code == 400:
            print("400 bad request")
        else:
            print("500 internal server error")


class CheapPaymentGateway(PaymentGateway):
    pass


class ExpensivePaymentGateway(PaymentGateway):
    def __init__(self, available: bool, amount_to_be_paid, payment_success_code):
        """
        Overrided the parent __init__ method as it involes if this PaymentGateway is available
        :param available:
        :param amount_to_be_paid:
        :param payment_success_code:
        """
        super().__init__(amount_to_be_paid, payment_success_code)
        self._available = available

    def initialize_payment(self):
        if self._available:
            print("Payment processed through Expensive Payment Gateway")
        else:
            CheapPaymentGateway(self._amount_to_be_paid, self._payment_success_code).initialize_payment()


class PremiumPaymentGateway(PaymentGateway):
    pass
