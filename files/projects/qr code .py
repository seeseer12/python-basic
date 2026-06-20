# program to generate QR code
import qrcode
# data to be encoded
data = "https://www.example.com"
# create qr code instance
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)
# add data to the qr code
qr.add_data(data)   
qr.make(fit=True)
# create an image from the qr code instance
img = qr.make_image(fill='black', back_color='white')
# save the image
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")
