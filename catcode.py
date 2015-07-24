__author__ = 'a5'
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
import reportlab.rl_config
reportlab.rl_config.warnOnMissingFontGlyphs = 0



#----------------------------------------------------------------------
def createBarCodes():
 """
 Create barcode examples and embed in a PDF
 """
 print os.sep

 c = canvas.Canvas("barcodes.pdf", pagesize=(5.715 * cm,3.175 * cm))
 canvas.Canvas.drawString(c,10*mm, 70*mm, "Now we just have to read the Jason and we have a label basically")
 barcode_value = "1234567890"

 #barcode128 = code128.Code128(barcode_value)
 # the multiwidth barcode appears to be broken
 barcode128Multi = code128.MultiWidthBarcode(barcode_value)
 print c.getAvailableFonts()

#register font
 #justface= EmbeddedType1Face('/Users/dimi/PycharmProjects/BX-goat-cat/ocra.afm', '/Users/dimi/PycharmProjects/BX-goat-cat/OCRA.pfb')
 #faceName = "OCRA"
 #registerFontFamily(TTFont('OCRA', '/Users/dimi/PycharmProjects/BX-goat-cat/OCRA.ttf'))
 #canvas.setFont('OCRA', 12)
 #canvas.drawString(1,1, 'BreakitFixit')


 image = Image.open('/Users/dimi/Desktop/b.eps', 'r')
 draw = ImageDraw.Draw('/Users/dimi/Desktop/b.eps')


#create

 typestr = 'SK: 5c lcd b ori RC: 7/20/15 IV: L17 CR: dhl 3484191793'
 azres = barcode('aztec', typestr)
 azres.save('az.eps')
 #azres.show()


 x = 1 * mm
 y = 2 * mm
 x1 = 6.4 * mm

 c.drawImage('az.eps', 20 * mm, 20 * mm)

 barcode128.drawOn(c, x, y)
 c.showPage()

 c.save()