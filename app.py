from flask import Flask, render_template, request, send_file
from generate_pdf import generate_pdf_with_qr

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("form.html")

@app.route("/generate_pdf", methods=["POST"])
def generate_pdf():
    full_name = request.form.get("full_name")
    email = request.form.get("email")
    phone_number = request.form.get("phone_number")
    
    # Generate the PDF with the QR code
    pdf_filename = generate_pdf_with_qr(full_name, email, phone_number)
    
    # Return the PDF to the user
    return send_file(pdf_filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)

