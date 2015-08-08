__author__ = 'dimi'
from urllib2 import Request, urlopen
import json
import base64
from pprint import pprint
import elaphe
import zlib

import os
from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics import renderPDF
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import registerFontFamily,  EmbeddedType1Face
from elaphe import barcode
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from PIL import Image, ImageFont, ImageDraw






headers = {
 'Authorization': 'Basic MThkNmEwMDI4YzkzNDFkY2FjMGFjMzI1NzYwNjZmZGY6OTgxM2VkY2MyYTU3NGQ1NGE3N2QzZjBiNGVkNGI0OTk='
}

request = Request('https://ssapi.shipstation.com/accounts/listtags', headers=headers)

response_body = urlopen(request).read()

request = Request('https://ssapi.shipstation.com/orders?orderStatus=awaiting_shipment', headers=headers)


response_body = urlopen(request).read()

orderqueue = json.loads(response_body)




#pprint(orderqueue)
print 'Number of pending orders ' + str(len(orderqueue['orders'])) + '\n'
pprint(orderqueue['orders'][2])
print '========================='
for order in orderqueue['orders']:
 useful = ''
 useful+=(str(order['orderId']))
 useful+=(str(order['shipTo']))
 useful+=(str(order['billTo']))
 #useful+=(str(order['items']))





 print useful
 data = elaphe.barcode('aztec', zlib.compress(useful,9), options=dict(columns=8, rows=4))
 print type(data)
 data.save("data.png", "PNG")
 data.show()


<<<<<<< Updated upstream



#print response_body
=======
#print response_body
>>>>>>> Stashed changes
