# PyEmailParsers
Email parsers written in Python to extract useful information.
Requires email id and password. 
Note: If 2-Factor Authentication is enabled, you might require a separate "App Password" for Gmail or something similar for other email providers.

## Swiggy Email Parser

Extracts the grand total amount spent in the given date range.

## Uber Email Parser

Extracts the grand total amount spent in the given date range.
Note: This will not count rides that you received a receipt at a later date for if it's not in the given date range.
For example - 
You took a ride on May 30th, 2019. Received the receipt in your email inbox on June 1, 2019. 
If you give the date range as May 1 - May 30, it will not count the trip as it was received outside the specified date range.
To avoid this, you can pay the ride amount immediately after completing the trip so you receive the receipt in your email on time.



