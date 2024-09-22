from app import app, db
from app.models import Bill
from flask import request, jsonify
import qrcode
from PIL import Image
import io

@app.route('/bill/<int:id>', methods=['GET'])
def get_bill(id):
    bill = Bill.query.get_or_404(id)
    return jsonify({
        'company': bill.company,
        'invoice_no': bill.invoice_no,
        'amount': bill.amount,
        'currency': bill.currency,
        'due_date': bill.due_date,
        'payment_url': bill.payment_url
    })

@app.route('/bill/<int:id>/qr', methods=['GET'])
def get_bill_qr(id):
    bill = Bill.query.get_or_404(id)
    qr_data = f"""
    Company: {bill.company}
    Invoice No: {bill.invoice_no}
    Amount: {bill.amount} {bill.currency}
    Due Date: {bill.due_date}
    Pay Here: {bill.payment_url}
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    
    return img_byte_arr.getvalue(), 200, {'Content-Type': 'image/png'}
