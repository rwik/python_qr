import qrcode
import datetime
from pyzbar.pyzbar import decode
from PIL import Image


#from qrcode.image.styledpil import StyledPilImage
#from qrcode.image.styles.colormasks import RadialGradiantColorMask
#from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

def encode(key):
    qr = qrcode.QRCode(version=1,box_size=12,border=6)
    qr.add_data(key)
    qr.make(fit=True)
    img = qr.make_image()
    fileName = f'qr_{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}.png'
    img.save(fileName)
    print("QR image is saved successfully in current path ")


def decode_qr(key):
    img = Image.open(key)
    text = decode(img)
    print(f"result={text}")
    pass


def main():
    choice = int(input("Hello there, Do you want to create a qr(1) or read a qr(2) ? "))
    if choice == 1:
        key = input("Please provide the text for encoding: ")
        encode(key)
    elif choice == 2:
        key = input("Please provide path to qr image: ")
        decode_qr(key)
    else:
        print("Please provide valid input")


if __name__ == "__main__":
    main()
