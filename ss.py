__author__ = 'dimi'


from urllib2 import Request, urlopen
import json
from pprint import pprint
headers = {
 'Authorization': 'Basic MThkNmEwMDI4YzkzNDFkY2FjMGFjMzI1NzYwNjZmZGY6OTgxM2VkY2MyYTU3NGQ1NGE3N2QzZjBiNGVkNGI0OTk='
}

request = Request('https://ssapi.shipstation.com/accounts/listtags', headers=headers)

response_body = urlopen(request).read()
print response_body

request = Request('https://ssapi.shipstation.com/orders?orderStatus=awaiting_shipment', headers=headers)


response_body = urlopen(request).read()

pprint(response_body)
orderqueue = json.loads(response_body)

orderqueue


pprint(orderqueue)
print response_body