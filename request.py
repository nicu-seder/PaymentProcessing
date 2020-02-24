from request_details import *


class Request:
    """
    Request object containing all details regarding a payment
    """

    def __init__(self, credit_card_number: CreditCardNumber, card_holder: CardHolder, expiration_date: ExpirationDate,
                 amount: Amount, security_code: SecurityCode = "000"):
        """
        Request constructor
        :param credit_card_number: CreditCardNumber object
        :param card_holder: CardHolder object
        :param expiration_date: ExpirationDate object
        :param amount: Amount object
        :param security_code: SecurityCode abject
        """
        self._credit_card_number = credit_card_number
        self._card_holder = card_holder
        self._expiration_date = expiration_date
        self._amount = amount
        self._security_code = security_code

    def get_amount(self) -> float:
        return self._amount.get_amount()
