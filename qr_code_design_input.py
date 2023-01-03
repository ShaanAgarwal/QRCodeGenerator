# importing qrcode module
import qrcode

# importing the Image library from PIL module
from PIL import Image

# taking input of the version for the qrcode from the user
version_number = int(input("Enter the version of the qrcode: "))

# taking the input of the box size of the qrcode from the user
box_size_number = int(input("Enter the box size for the qrcode: "))

# taking the input of the border size of the qrcode from the user
border_size = int(input("Enter the border size of the qrcode: "))

# making the variable qr for managing the features of the qrcode entered by the user
qr = qrcode.QRCode(version = version_number,
                    error_correction = qrcode.constants.ERROR_CORRECT_H, 
                    box_size = box_size_number, border = border_size)

# taking the input of the data for the qrcode from the user
data = input("Enter the data for the qrcode: ")

# fitting the features into the qrcode entered by the user
qr.make(fit = True)

# taking the input for the color of the qrcode from the user
qr_color = input("Enter the color for the qrcode: ")

# taking the input for the background color of the qrcode from the user
qr_background_color = input("Enter the background color for the qrcode: ")

# creating the qrcode, fitting all the features and the color 
img = qr.make_image(fill_color = qr_color, back_color = qr_background_color)

# taking the name of the image from the user using which you would like to save the qrcode
image_name = input("Enter the name of the image as you would like to save the qrcode image: ")

# concatenating the name of the image with image extension ".png"
final_image_name = image_name + ".png"

# saving the qrcode as an image
img.save(final_image_name)