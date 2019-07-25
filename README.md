# PyEmailParsers
Email parsers written in Python to extract useful information.
Requires email id and password. 
Note: If 2-Factor Authentication is enabled, you might require a separate "App Password" for Gmail or something similar for other email providers.

## Swiggy Email Parser

Extracts the grand total amount spent in the given date range.

## Uber Email Parser

Extracts the grand total amount spent in the given date range.

Note: This will not count rides that you received a receipt at a later date for if it's not in the given date range.

For example, if you took a ride on May 30th and received the receipt in your email inbox on June 1, if you then give the date range as May 1 - May 30, it will not count the trip as it was received outside this range.

To avoid this, you can pay the ride amount immediately after completing the trip so you receive the receipt in your email on time (mainly applies to places where Uber doesn't auto-charge your card).

## Amazon.in Email Parser

Extracts the grand total amount spent in the given date range.

Note: This does not (yet) take into consideration any orders that were refunded. It only reads the emails for the receipts generated when an order is placed.
