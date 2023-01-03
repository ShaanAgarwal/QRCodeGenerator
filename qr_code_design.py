# importing the qrcode module
import qrcode

# importing Image library from PIL module
from PIL import Image

# making variable qr to handle the changing features to the qrcode
# defining the version, error_correction, highlevel_correction, size of the qrcode and the border size of the code
qr = qrcode.QRCode(version = 1, 
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)

# generating adding the data for the qrcode
qr.add_data("www.youtube.com")

qr.make(fit = True)

# generating the qrcode by defining the main color and the background color
img = qr.make_image(fill_color = "green", back_color = "yellow")

# saving the image of the qrcode for use
img.save("youtube_link_address.png")