import qrcode
from PIL import Image

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return img

if __name__ == '__main__':
    bill_data = {
        'company': 'XYZ Corp',
        'invoice_no': '12345',
        'amount': '150.00',
        'currency': 'USD',
        'due_date': '2024-08-01',
        'payment_url': 'https://paymentgateway.com/pay?invoice=12345&amount=150.00'
    }

    qr_data = f"""
    Company: {bill_data['company']}
    Invoice No: {bill_data['invoice_no']}
    Amount: {bill_data['amount']} {bill_data['currency']}
    Due Date: {bill_data['due_date']}
    Pay Here: {bill_data['payment_url']}
    """

    qr_image = generate_qr_code(qr_data, 'bill_qr_code.png')
    qr_image.show()
