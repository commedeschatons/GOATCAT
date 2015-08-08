__author__ = 'Steven'

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
from urllib2 import Request, urlopen
import json
import elaphe
import zlib


VERSION = "bxcc0.11"
WAYBILL_FILENAME = 'bxwaybill.pdf' #required for canvas objest
SC = 1*mm
WAYBILL_H = 31.75*2 * SC
WAYBILL_W = 57.15*2 * SC

styles = getSampleStyleSheet()

def stylesheet():
    styles= {
        'default': ParagraphStyle(
            'default',
            fontName='Helvetica',
            fontSize=18,
            leading=22,
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


print useful
data = elaphe.barcode('aztec', zlib.compress(useful,9), options=dict(columns=8, rows=4))
print type(data)
data.save("data1.png", "PNG")

########################################################################
class Test(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.width, self.height = (WAYBILL_W, WAYBILL_H)
        self.styles = stylesheet()

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
        normal = self.styles["default"]
        ptext = "<b>Type: </b> 5C LCD Ori <br/> <b>Color: </b> Black <br/><b>Qty: </b> 1 pc"
        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, 30, 30)

        #the logo
    	self.c.drawImage('thermal.png', 10*SC, 45*SC, 1082*0.25, 164*0.25)
        #barcode
        self.c.drawImage('data1.png', SC*75, SC*5, 122*0.75, 122*0.75) # test


    #----------------------------------------------------------------------
if __name__ == "__main__":
    t = Test()
    t.run()

