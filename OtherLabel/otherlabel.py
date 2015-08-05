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

from PIL import Image
VERSION = "bxcc0.11"
WAYBILL_FILENAME = 'bxwaybill.pdf' #required for canvas objest
SC = 1*mm
WAYBILL_H = 31.75*2 * SC
WAYBILL_W = 57.15*2 * SC

styles = getSampleStyleSheet()

def createBlankWayBill():
	wb = canvas.Canvas(WAYBILL_FILENAME, pagesize=(WAYBILL_W, WAYBILL_H))

	#drawline


	add = """Dimitri James3336 Hamilton\n71\nWest Lafayette\nIN\n47906 US"""
	wb.drawString(2.5*SC, 90*SC, add)

	#bifi logo
	wb.drawImage('thermal.png', 80*SC, 2.5*SC, 1082*0.175, 164*0.175)


	wb.setLineWidth(0.5)

	wb.line(0*SC, SC*40, 77.5*SC,SC*40 )
	wb.line(77.5*SC, SC*40, 77.5*SC , SC*0)
	wb.line(77.5*SC, 15.5*SC, 150*SC, 15.5*SC)
	print wb.getAvailableFonts()
	#draw address

	 #country

	#random strings
	wb.setFont('Courier', 7.5)
	canvas.Canvas.drawString(wb, SC*135, SC*0, VERSION)
	wb.setFont('Helvetica-Bold', 20)
	#draw pdf417
	wb.drawImage('data.png', SC*2.5,SC*2.5) # test
	# draw linecode

	#draw logo

	#draw carrier logo
	return wb


#test
createBlankWayBill().save()

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
        normal = self.styles["Normal"]

        header_text = "<b>This is a test header</b>"
        p = Paragraph(header_text, normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, *self.coord(1, 12, mm))

        ptext = "<b>Type: </b> 5C LCD Ori <br/> <b>Color: </b> Black <br/><b>Qty: </b> 1 pc"

        p = Paragraph(ptext, style=normal)
        p.wrapOn(self.c, self.width, self.height)
        p.drawOn(self.c, 30, 30)
        #the logo
    	self.c.drawImage('thermal.png', 20*SC, 50*SC, 1082*0.175, 164*0.175)
        #barcode
        self.c.drawImage('data.png', SC*75,SC*2, 205*0.50, 96*0.5) # test


    #----------------------------------------------------------------------
if __name__ == "__main__":
    t = Test()
    t.run()