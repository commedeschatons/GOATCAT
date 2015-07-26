__author__ = 'a5'
from urllib2 import Request, urlopen
import json
from pprint import pprint


authheader = {'Authorization': 'Basic MThkNmEwMDI4YzkzNDFkY2FjMGFjMzI1NzYwNjZmZGY6OTgxM2VkY2MyYTU3NGQ1NGE3N2QzZjBiNGVkNGI0OTk='}
url_awaitingshipment = 'orders?orderStatus=awaiting_shipment'

def getSSResponse(path):
    request = Request('https://ssapi.shipstation.com/' + path, headers=authheader)
    response_body = urlopen(request).read()
    return json.loads(response_body)

class Order:
    def __init__(self, orderID):
        self.orderID = orderID
        allinfo = getSSResponse('orders/' + self.orderID)
        self.city = allinfo['shipTo']['city']
        self.name = allinfo['shipTo']['name']
        self.postalcode = allinfo['shipTo']['postalCode']
        self.street1 = allinfo['shipTo']['street1']
        self.street2 = allinfo['shipTo']['street2']
        self.country = allinfo['shipTo']['country']
        self.state = allinfo['shipTo']['state']

    def getStreet(self):
        Streets = self.street1 +"\n"+ self.street2
        return Streets

    def getAddress(self):
        if self.street2 != "":
            Streets = self.street1 +"\n"+ self.street2
        else:
            Streets = self.street1
        if self.state != "":
            state = ", " + self.state
        else:
            state = ""
        Address = self.name + '\n' + Streets +"\n"+ self.city + state + "\n" + self.postalcode + "\n"
        return Address

def getAwaitingOrders():
    everything = getSSResponse(url_awaitingshipment)
    orderIds = list()
    for i in range(0, len(everything['orders'])):
        orderIds.append(everything['orders'][i]['orderId'])
    return orderIds


myorderIds = getAwaitingOrders()

for orderID in myorderIds:
    O = Order(str(orderID))
    print(O.getAddress())



