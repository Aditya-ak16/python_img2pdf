import os
import img2pdf
with open("ImageContainingBook.pdf", "wb") as file:
    file.write(img2pdf.convert([i for i in os.listdir("C:\\Users\\Aditya\\OneDrive\\Desktop\\img2pdf") if i.endswith(".jpg")])) # Change the file directory accordingly
