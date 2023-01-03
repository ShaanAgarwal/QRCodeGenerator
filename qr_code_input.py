# importing the qrcode module
import qrcode as qr

# taking the input of the data to be stored in the qrcode
data = input("Enter the data or the link to be executed by the qrcode: ")

# generating the qrcode using make() function
image = qr.make(data)

# entering the name of the file to be stored as the qrcode
name = input("Enter the name using which you would like to save the qrcode as an image: ")

# concatenating the name of the file with the image extension
final_name_of_file = name + ".png"

# saving the generated qrcode as an image
image.save(final_name_of_file)