import pyqrcode

from pyqrcode import QRCode

Email = "kshitijsangar@gmail.com\n"
Mobile = "\n 8669042081\n"

obj = pyqrcode.create(Email + Mobile)
obj.svg("QR_kshitij.svg",scale = 7)