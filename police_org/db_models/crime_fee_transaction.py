from . import *
from ..enums.transaction_type import TransactionType


class CrimeFeeTransactions(Base):
    __tablename__ = 'crime_fee_transactions'

    id = Column('crime_fee_transaction_id', Integer, primary_key=True)
    transaction_id = Column("transaction_id", String(20))
    crime_id = Column("crime_id", Integer, ForeignKey('crimes.crime_id'))
    transaction_type = Column("transaction_type", Enum(TransactionType), nullable=False)
    description = Column("Description", String(50), nullable=True)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, transaction_id: str, transaction_type: TransactionType, description: str):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.description = description
