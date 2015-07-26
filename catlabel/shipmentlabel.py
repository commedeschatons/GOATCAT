from reportlab.lib.units import mm, cm
from reportlab.pdfgen import canvas
from elaphe import barcode
from reportlab.graphics import renderPDF
from reportlab.lib.utils import ImageReader

VERSION = "bxcc0.11"
WAYBILL_FILENAME = 'bxwaybill.pdf' #required for canvas objest
SC = 1*mm
WAYBILL_H = 100 * SC
WAYBILL_W = 150 * SC


def createBlankWayBill():
	wb = canvas.Canvas(WAYBILL_FILENAME, pagesize=(WAYBILL_W, WAYBILL_H))

	#drawline
	wb.line(0, SC*40, 77.5*SC,SC*40 )
	wb.line(77.5*SC, SC*40, 77.5*SC , 0)

	print wb.getAvailableFonts()
	#draw address

	 #country

	#random strings
	wb.setFont('Courier', 10)
	canvas.Canvas.drawString(wb, SC*130, SC*2.5, VERSION)
	#draw pdf417
	wb.drawImage('data.png', SC*2.5,SC*2.5) # test
	# draw linecode

	#draw logo

	#draw carrier logo

	return wb


#test
createBlankWayBill().save()