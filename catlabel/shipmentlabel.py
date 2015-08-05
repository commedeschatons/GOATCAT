from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from elaphe import barcode
from reportlab.graphics import renderPDF
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet

from PIL import Image
VERSION = "bxcc0.11"
WAYBILL_FILENAME = 'bxwaybill.pdf' #required for canvas objest
SC = 1*mm
WAYBILL_H = 100 * SC
WAYBILL_W = 150 * SC

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