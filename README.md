# Payment Processing

The purpose of this project is to process user payments, which we call as requests. 

Each request element has its own class: CreditCardNumber, CardHolder, ExpirationDate, SecurityCode, Amount so they are decoupled. All of the represent a request. All the testing is done inside them - ex: Inside ExpirationDate we have "private" methods which test if the expiration_date is a valid date and if the expiration_date is in the future.

For each request element we wait for user input in order to try to replicate a web app where the user fill in forms with the required information.

Regarding PaymentGateway, i used OOP concept such as inheritance and polymorphism where PaymentGateway is the top parent and the specialized payment gateways are children of PaymentGateway and depending of the case one of them is used. All children payment gateways inherit attributes from the parent but some children classes oiverride some methods.

For the optional task, i didn't get it very well but it tried to create a simple prediction logic. The method estimate_price it asks for a stock_name(ex:"AA") and a date as "year", "month" and "day". Based on the stock_name sent as parameter we loop through the database(the csv file dow_jones_index.csv) and filter it by only stocks that are equal with the paramter. Then we create the mean of the mid_range_price of all remaining stocks but only those who are in the same month as the sent as parameter.

mid_range is computed previously for each observation as the mean of highest_price and lowest_price.

The program starts in main module where a request object and an app object are created. Then, the app object represent the application which processes requests and tries to estimate a price - basically it has only 2 methods.
