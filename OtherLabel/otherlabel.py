__author__ = 'Steven'
from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from elaphe import barcode
from reportlab.graphics import renderPDF
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, SimpleDocTemplate, Spacer
import json
from urllib2 import Request, urlopen
import json
import base64
from pprint import pprint
import elaphe
import zlib

import os
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics import renderPDF
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import registerFontFamily,  EmbeddedType1Face
from elaphe import barcode
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping
from PIL import Image, ImageFont, ImageDraw

from PIL import Image
VERSION = "bxcc0.11"
WAYBILL_FILENAME = 'bxwaybill.pdf' #required for canvas objest
SC = 1*mm
WAYBILL_H = 31.75*2 * SC
WAYBILL_W = 57.15*2 * SC

styles = getSampleStyleSheet()

#get info from shipstation and make data.png
headers = {
 'Authorization': 'Basic MThkNmEwMDI4YzkzNDFkY2FjMGFjMzI1NzYwNjZmZGY6OTgxM2VkY2MyYTU3NGQ1NGE3N2QzZjBiNGVkNGI0OTk='
}
request = Request('https://ssapi.shipstation.com/orders?orderStatus=awaiting_shipment', headers=headers)
response_body = urlopen(request).read()
orderqueue = json.loads(response_body)
for order in orderqueue['orders']:
    useful = ''
    useful+=(str(order['orderId']))
    useful+=(str(order['shipTo']))
    useful+=(str(order['billTo']))


print useful
data = elaphe.barcode('aztec', zlib.compress(useful,9), options=dict(columns=8, rows=4))
print type(data)
data.save("data.png", "PNG")
data.show()


########################################################################
class Test(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = (WAYBILL_W, WAYBILL_H)
        self.styles = getSampleStyleSheet()

    #----------------------------------------------------------------------
    def coord(self, x, y, unit=1):
        """
        http://stackoverflow.com/questions/4726011/wrap-text-in-a-table-reportlab
        Helper class to help position flowables in Canvas objects
        """
        x, y = x * unit, self.height -  y * unit
        return x, y

    #----------------------------------------------------------------------
    def run(self):
        """
        Run the report
        """
        self.doc = SimpleDocTemplate("test.pdf", pagesize = (WAYBILL_W, WAYBILL_H))
        self.story = [Spacer(0, 0*inch)]

        self.doc.build(self.story, onFirstPage=self.createDocument)
        print "finished!"

    #----------------------------------------------------------------------
    def createDocument(self, canvas, doc):
        """
        Create the document
        """
        self.c = canvas
        normal = self.styles["Heading1"]
        ptext = "<b>Type: </b> 5C LCD Ori <br/> <b>Color: </b> Black <br/><b>Qty: </b> 1 pc"
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, 30, 30)
        #the logo



    	self.c.drawImage('thermal.png', 10*SC, 40*SC, 1082*0.25, 164*0.25)
        #barcode
        self.c.drawImage('data.png', SC*75,SC*2, 205*0.50, 96*0.5) # test


    #----------------------------------------------------------------------
if __name__ == "__main__":
    t = Test()
    t.run()
