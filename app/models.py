from app import db

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    invoice_no = db.Column(db.String(50), nullable=False, unique=True)
    amount = db.Column(db.Float, nullable=False)
    currency = db.Column(db.String(10), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    payment_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Bill {self.invoice_no}>'
