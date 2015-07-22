__author__ = 'a5'

from reportlab.graphics.barcode import code39, code128, code93
from reportlab.graphics.barcode import eanbc, qr, usps
from reportlab.graphics.shapes import Drawing
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.graphics import renderPDF
from reportlab.lib.utils import ImageReader
from elaphe import barcode
from PIL import Image


#----------------------------------------------------------------------
def createBarCodes():
 """
 Create barcode examples and embed in a PDF
 """
 c = canvas.Canvas("barcodes.pdf", pagesize=(432,288))
 canvas.Canvas.drawString(c,10*mm, 70*mm, "Now we just have to read the Jason and we have a label basically")
 barcode_value = "1234567890"

 barcode128 = code128.Code128(barcode_value)
 # the multiwidth barcode appears to be broken
 barcode128Multi = code128.MultiWidthBarcode(barcode_value)


#create

 typestr = 'SK: 5c lcd b ori RC: 7/20/15 IV: L17 CR: dhl 3484191793'
 azres = barcode('aztec', typestr)
 azres.save('az.eps')
 #azres.show()
 x = 1 * mm
 y = 10 * mm
 x1 = 6.4 * mm

 c.drawImage('az.eps', 20 * mm, 20 * mm)

 barcode128.drawOn(c, x, y)
 c.showPage()

 c.save()

if __name__ == "__main__":
 createBarCodes()