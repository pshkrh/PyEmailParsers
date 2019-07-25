from imbox import Imbox
import datetime
from bs4 import BeautifulSoup
from decimal import *

def read_email(start_date, end_date,email,pwd):
    with Imbox('imap.gmail.com',
        username=email,
        password=pwd,
        ssl=True,
        ssl_context=None,
        starttls=False) as imbox:

            parsed_start_date = parse_date(start_date)
            parsed_end_date = parse_date(end_date)

            GRAND_TOTAL = 0
            subtotals = []

            swiggy_emails = imbox.messages(sent_from='uber.india@uber.com', subject='trip with Uber',date__gt=parsed_start_date, date__lt=parsed_end_date)
            for uid, message in swiggy_emails:
                mailbody = str(message.body)
                
                soup = BeautifulSoup(mailbody, 'html.parser')
                parsed_txt = soup.find('span', attrs={'class':'Uber18_text_p2'}).text
                
                # Parsed text looks like this - ' ₹99'
                amount = Decimal(parsed_txt[2:])
                subtotals.append(amount)
                GRAND_TOTAL+= amount

            print(subtotals)
            print(GRAND_TOTAL)

def parse_date(date):
    datelist = date.split('-')
    parsed_date = datetime.date(int(datelist[2]),int(datelist[1]),int(datelist[0]))
    return parsed_date

if __name__ == '__main__':
    email = input("Enter your email id: ")
    pwd = input("Enter your password: ") # If you have 2 Factor enabled, you will need an app password for GMail.
    start_date = input("Enter the start date (DD-MM-YYYY): ")
    end_date = input("Enter the end date (DD-MM-YYYY): ")
    read_email(start_date,end_date,email,pwd)