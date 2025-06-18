import qrcode  
# generating a QR code using the make() function  
qr_img = qrcode.make("Dear Students Course Completed-Best of Luck")  
# saving the image file  
qr_img.save("student.jpg")  
print("QR Code generated--verify")