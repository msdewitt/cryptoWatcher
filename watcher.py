# This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

import emailSender

cryptoCurrencies = ['BTC', 'LINK', 'THETA']

symbol=''
isNotFirst = False
for crypto in cryptoCurrencies:
    if isNotFirst:
        symbol +=','
    symbol+= crypto
    isNotFirst = True;

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {
    'symbol': symbol,
    # 'start': '1',
    # 'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'fa87d364-1417-43bd-96d5-0738dba66927',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    print(data)
    message = ""
    simpleMessage=""
    for crypto in cryptoCurrencies:
        print('Name: ' + data['data'][crypto]['name'])
        message = message + '<p><b>Name:</b> ' + data['data'][crypto]['name'] + '<br>'
        simpleMessage += data['data'][crypto]['name'] + ": $" + str(round(data['data'][crypto]['quote']['USD']['price'], 3)) + "\n || "
        print('Market Price: $' + str(data['data'][crypto]['quote']['USD']['price']))
        message = message + '<b>Market Price:</b> $' + str(data['data'][crypto]['quote']['USD']['price']) + '<br>'
        print('Market Cap: $' + str(data['data'][crypto]['quote']['USD']['market_cap']))
        message = message + '<b>Market Cap:</b> $' + str(data['data'][crypto]['quote']['USD']['market_cap']) + '<br>'
        print('Last Updated: ' + str(data['data'][crypto]['quote']['USD']['last_updated']))
        message = message + '<b>Last Updated:</b> ' + str(data['data'][crypto]['quote']['USD']['last_updated']) + '<br>'
        print('Percent Change In Last 7d: ' + str(data['data'][crypto]['quote']['USD']['percent_change_7d']))
        message = message + '<b>Percent Change In Last 7d:</b> <i>' + str(data['data'][crypto]['quote']['USD']['percent_change_7d']) + '%</i><br>'
        print('Percent Change In Last 24h: ' + str(data['data'][crypto]['quote']['USD']['percent_change_24h']))
        message = message + '<b>Percent Change In Last 24h:</b> <i>' + str(data['data'][crypto]['quote']['USD']['percent_change_24h']) + '%</i><br>'
        print('Percent Change In Last 1h: ' + str(data['data'][crypto]['quote']['USD']['percent_change_1h']))
        message = message + '<b>Percent Change In Last 1h:</b> <i>' + str(data['data'][crypto]['quote']['USD']['percent_change_1h']) + '%</i><br>'
        print('\n')
        message += '\n</p><br>'
    emailSender.sendEmail(message, simpleMessage)
except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)