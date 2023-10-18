import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_with_qr(full_name, email,phone_number):
    #create QR Code

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f"Full Name: {full_name}\nEmail: {email}\nphone Number: {phone_number}")
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save("static/qr.png")

    # create pdf file

    pdf_filename = "qr_code.pdf"
    c = canvas.Canvas(pdf_filename, pagesize=letter)
   
    c.drawImage("static/qr.png", 100, 600, width=200, height=200)
    c.save()
    
    return pdf_filename

if __name__ == "__main__":
    generate_pdf_with_qr("please enter your name", "and email", "and your phone")



