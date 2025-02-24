import qrcode

data = input('Enter the text/URL: ').strip() # The '.strip()' method helps to remove any whitespaces around our 
                                             # link, such that the link is still valid regardless.

# Now for the getting of the filename,
filename = input('Enter the filename: ').strip() # Meaning stripping any whitespaces as well, around the filename

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')