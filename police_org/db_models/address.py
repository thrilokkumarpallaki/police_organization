from . import *


class Addresses(Base):
    __tablename__ = 'addresses'

    id = Column('address_id', Integer, primary_key=True)
    address_1 = Column('address1', String(20), nullable=False)
    address_2 = Column('address2', String(15))
    street = Column('street', String(20), nullable=False)
    city = Column('city', String(15), nullable=False)
    zipcode = Column('zipcode', String(10), nullable=False)
    state = Column('state', CHAR(2), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, address_1: str, address_2: str, street: str, city: str, zipcode: str, state: str):
        self.address_1 = address_1
        self.address_2 = address_2
        self.street = street
        self.city = city
        self.zipcode = zipcode
        self.state = state
