import datetime


class CreditCardNumber:
    """
    It asks for card number as input and checks if the input is a valid card number
    """

    def __init__(self):
        while True:
            card_number = input("Insert credit card number\n")
            if self._check_card_number_validity(card_number):
                self._card_number = card_number
                break
            else:
                print("Invalid card number")

    def _check_card_number_validity(self, card_number_to_check: str) -> bool:
        """
        Checks if the card number is valid, which means if it contains only numbers as characters
        and the total number of character is equal to 16.

        :param card_number_to_check:
        :return:
        """
        card_number_to_check = ''.join(card_number_to_check.split())
        if (self._check_card_number_length(card_number_to_check) and self._check_card_number_integrity(
                card_number_to_check)):
            return True
        else:
            return False

    def _check_card_number_integrity(self, card_number_to_check: str) -> bool:
        """
        Checks if all characteres are numbers and not letters or symbols
        :param card_number_to_check:
        :return:
        """
        return card_number_to_check.isdecimal()

    def _check_card_number_length(self, card_number_to_check: str) -> bool:
        """
        Checks the length of  the card number
        :param card_number_to_check:
        :return:
        """
        return len(card_number_to_check) == 16


class CardHolder:
    """
    Asks for first name and last name as input. Then it checks if the names are valid names - they contain only letters
    """

    def __init__(self):
        while True:
            first_name = input("Insert first name\n")
            last_name = input("Insert last name\n")
            if self._check_if_only_letters(first_name) and self._check_if_only_letters(last_name):
                self._name = first_name.lower().capitalize() + ", " + last_name.lower().capitalize()
                break
            else:
                print("Invalid first name or last name")

    def _check_if_only_letters(self, text: str) -> bool:
        return text.isalpha()


class ExpirationDate:
    """
    Asks for month and year as card expiry details. It checks if the year and month are valid and if the expiry date
    is in the past
    """

    def __init__(self):
        self._current_date = datetime.date.today()
        while True:
            year = input("Insert year of card expiry\n")
            month = input("Insert month of card expiry\n")
            if self._check_date_validity(year, month) and self._current_date < datetime.date(int(year), int(month), 1):
                self._expiration_date = datetime.date(int(year), int(month), 1)
                break
            else:
                print("Expiry date is not valid")

    def _check_month_validity(self, month: str):
        return month.isdecimal() and int(month) in range(1, 13) and len(month) in range(1, 3)

    def _check_year_validity(self, year: str):
        return year.isdecimal() and int(year) in range(1900, 10000)

    def _check_date_validity(self, year, month):
        return self._check_year_validity(year) and self._check_month_validity(month)


class SecurityCode:
    """
    Asks for security code which is not mandatory. By default is "000". If entered it is checked if it's a valid one
    """

    def __init__(self):
        while True:
            security_code = input("Insert security code\n")
            if security_code == "":
                self._security_code = "000"
                break
            elif security_code.isdecimal() and len(security_code) == 3:
                self._security_code = security_code
                break
            else:
                print("Invalid security code")


class Amount:
    """
    Asks for amount which will be processed by the application. The amount is checked if is a numeric value so it can be
    used in further computation
    """

    def __init__(self):
        while True:
            amount = input("Insert amount to be processed\n")
            try:
                self._amount = float(amount)
                break
            except ValueError:
                print("Invalid amount")

    def get_amount(self):
        return self._amount
