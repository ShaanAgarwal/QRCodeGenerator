# importing the qrcode module
import qrcode as qr 

# generating the image with the help of make() function
image = qr.make("www.youtube.com")

# saving the image of the qr code with the help of Save() function and renaming it with the name we want
image.save("youtube_link.png")