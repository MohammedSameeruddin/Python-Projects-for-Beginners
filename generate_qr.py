import pyqrcode
from pyqrcode import QRCode

myurl="https://github.com/MohammedSameeruddin/Python-Projects-for-Beginners/tree/main";
url=pyqrcode.create(myurl)
url.png("sameer_github.png",scale=8)
url.show()
