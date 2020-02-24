from app import App
from request import Request
from request_details import *

# Request object to be processed by the application
request = Request(CreditCardNumber(),
                  CardHolder(),
                  ExpirationDate(),
                  Amount(),
                  SecurityCode())

# Initialization of app object
app = App()

app.process_payment(request)
app.estimate_price("AA", "2011", "3", "14")
