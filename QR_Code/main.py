import qrcode

data = "https://www.linkedin.com/in/rajat-singh-aa7990316/"

qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color = "purple")

location="G:/My Drive/Coding/Python/Projects/Learning-Projects/QR_Code/qr_codes"

img.save(f"{location}/Linkedin_profile.png")