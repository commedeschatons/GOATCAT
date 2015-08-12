__author__ = 'Steven'

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from urllib2 import Request, urlopen
import json
import elaphe
import zlib

import string
import random

<<<<<<< HEAD
encode = "15G10L19"
=======
import datecode as dc

serial = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(7))

#argument for getEncoded is the invoice_number
encode = dc.getEncoded(18)
>>>>>>> 2b9ea0b44fcb0f01e6d2d10141d5dfd0e62ffe83
#VERSION = "bxcc0.11"
#WAYBILL_FILENAME = 'bxwaybill.pdf' #required for canvas objest
DATA = "SK: 5c lcd ori RC: 8/10/15 IV: 19 CR: dhl/3260516910 "
SC = 1*mm
WAYBILL_H = 31.75*2 * SC
WAYBILL_W = 57.15*2 * SC

styles = getSampleStyleSheet()
serial = "a"
color = raw_input("Enter the screen color ")
labels = input("Enter number of labels")
#color = "White"

def stylesheet():
    styles= {
        'default': ParagraphStyle(
            'default',
            fontName='Helvetica',
            fontSize=22,
            leading=25,
            leftIndent=0,
            rightIndent=0,
            firstLineIndent=0,
            spaceBefore=5,
            spaceAfter=5,
            bulletFontName='Times-Roman',
            bulletFontSize=10,
            bulletIndent=0,
            backColor=None,
            wordWrap=None,
            borderWidth= 0,
            borderPadding= 0,
            borderColor= None,
            borderRadius= None,
            allowWidows= 1,
            allowOrphans= 0,
            textTransform=None,  # 'uppercase' | 'lowercase' | None
            endDots=None,
            splitLongWords=1,
        ),
    }
    styles['small'] = ParagraphStyle(
        'small',
        parent=styles['default'],
        leading=16,
        fontName = 'Helvetica',
        fontSize = 12,
        borderWidth=1,
        borderPadding=5,
        borderRadius=2,
        spaceBefore=10,
        spaceAfter=10,
    )
    return styles

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




########################################################################
class Test(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = (WAYBILL_W, WAYBILL_H)
        self.styles = stylesheet()
        data = elaphe.barcode('aztec', zlib.compress(str(DATA + 'sn: ' + serial),1), options=dict(columns=8, rows=4))
        data.save("data1.png", "PNG")
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
        self.doc = SimpleDocTemplate('generated/' + serial + ".pdf", pagesize = (WAYBILL_W, WAYBILL_H))
        self.story = [Spacer(0, 0*inch)]

        self.doc.build(self.story, onFirstPage=self.createDocument)
        print "finished!"

    #----------------------------------------------------------------------
    def createDocument(self, canvas, doc):
        """
        Create the document
        """

        self.c = canvas
        if color == "White":
             self.c.rect(30*SC, 24.5*SC, 20*SC, 8 *SC, fill=1)
        normal = self.styles["default"]
        small = self.styles["small"]
        ptext = "<b>Type: </b> 5C LCD Ori <br/> <b>Color: </b><a color=%s> %s</a> <br/><b>Qty: </b> 1 pc" %(color, color)
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, 15, 45)
        p = Paragraph(encode, style=small)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, 15, 7)
        p = Paragraph(serial, style=small)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, 233, 7)



        #the logo
    	self.c.drawImage('thermal.png', 10*SC, 47*SC, 1082*0.25, 164*0.25)
        #barcode
        self.c.drawImage('data1.png', SC*78, SC*8, 122*0.75, 122*0.75) # test


    #----------------------------------------------------------------------
if __name__ == "__main__":

    for xk in range(0, labels):
        serial = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(7))
        serial = 'BX' + serial
        t = Test()
        t.run()

