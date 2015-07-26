__author__ = 'a5'
from urllib2 import Request, urlopen
import json
from pprint import pprint


authheader = {'Authorization': 'Basic MThkNmEwMDI4YzkzNDFkY2FjMGFjMzI1NzYwNjZmZGY6OTgxM2VkY2MyYTU3NGQ1NGE3N2QzZjBiNGVkNGI0OTk='}
url_awaitingshipment = 'orders?orderStatus=awaiting_shipment'
base = "https://ssapi.shipstation.com/"

def getSSResponse(path):
    request = Request('https://ssapi.shipstation.com/' + path, headers=authheader)
    response_body = urlopen(request).read()
    return json.loads(response_body)

class Order:
    def __init__(self, orderID):
        self.orderID = orderID
        request = Request("https://ssapi.shipstation.com/orders/" + self.orderID, headers=authheader)
        response_body = urlopen(request).read()
        allinfo = json.loads(response_body)
        self.city = allinfo['shipTo']['city']
        self.name = allinfo['shipTo']['name']
        self.postalcode = allinfo['shipTo']['postalCode']
        self.street1 = allinfo['shipTo']['street1']
        self.street2 = allinfo['shipTo']['street2']
        self.country = allinfo['shipTo']['country']

    def getStreet(self):
        Streets = self.street1 +"\n"+ self.street2
        return Streets
    def getAddress(self):
        Address = self.name + '\n' + self.street1 +"\n"+ self.street2+"\n"+ self.city + "\n" + self.postalcode
        return Address

OID = "119686380"
O = Order(OID)
print(O.country)
print(O.getAddress())

