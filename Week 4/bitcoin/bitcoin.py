import sys
import requests
import json

#Parsing
if (len(sys.argv) == 1):
    print("Missing command-line argument")
    sys.exit(1)
if (len(sys.argv) == 2):
    try:
        nb = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)

#Get Bitcoin price
try:
    res1 = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    res2 = res1.json()
    taux = res2["bpi"]["USD"]["rate_float"]
    total = taux * nb
    #Thousands separator = ,
    print(f"${total:,.4f}")
except requests.RequestException:
    print("Request Exception")
    sys.exit(1)