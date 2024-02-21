from . import *
from police_org.enums.charge_status import ChargeStatus


class CrimeCharges(Base):
    __tablename__ = 'crime_charges'

    id = Column('crime_charge_id', Integer, primary_key=True)
    crime_id = Column('crime_id', ForeignKey('crimes.crime_id'), nullable=False)
    crime_code_id = Column('crime_code', ForeignKey('crime_codes.code_id'), nullable=False)
    charge_status = Column('charge_status', Enum(ChargeStatus), nullable=False)
    fine_amount = Column('fine_amount', NUMERIC, default=0.0)
    court_fee = Column('court_fee', NUMERIC, default=0.0)
    pay_due_date = Column('payment_due_date', Date, nullable=True)
    amount_paid = Column('amount_paid', NUMERIC, default=0.0)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, crime_id: int, crime_code_id: int, charge_status: ChargeStatus,
                 fine_amount: float, court_fee: float, pay_due_date: date, amount_paid: float):
        self.crime_id = crime_id
        self.crime_code_id = crime_code_id
        self.charge_status = charge_status
        self.fine_amount = fine_amount
        self.court_fee = court_fee
        self.pay_due_date = pay_due_date
        self.amount_paid = amount_paid
