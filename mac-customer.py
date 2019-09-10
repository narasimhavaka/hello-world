#!/usr/local/bin/python

import requests
import json
import sys

def find_customer(*args, **kwargs):
    try:
        if args:
            mac = args[0][1]
        else:
            print('ERROR: MAC address is a mandatory parameter.')
    except:
            print('ERROR: Exception wile extracting MAC. Its a mandatory parameter.')

    url = 'https://api.macaddress.io/v1?apiKey=at_5Vi6TP5Re8N9Jgqq7FzEMZcyszs1i&output=json&search=' + mac

    try:
        res = requests.get(url=url)
    except:
        print('ERROR: MAC address is a mandatory parameter.')

    dic = json.loads(res.text)
    return dic.get('vendorDetails', {}).get('companyName', None)

if __name__ == '__main__':
    cus = find_customer(sys.argv)
    print(cus)
