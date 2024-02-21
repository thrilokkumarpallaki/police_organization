from . import *

from police_org.enums.officer_status import OfficerStatus


class ProbationOfficers(Base):
    __tablename__ = 'probation_officers'

    id = Column("prob_id", Integer, primary_key=True)
    last_name = Column("last_name", String(10), nullable=False)
    first_name = Column("first_name", String(15), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.address_id'), nullable=False)
    phone = Column("phone", String(10), nullable=False)
    email = Column("email", String(20), nullable=False)
    status = Column("prob_status", Enum(OfficerStatus), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, last_name: str, first_name: str, address_id: int, phone: str, email: str, status: OfficerStatus):
        self.last_name = last_name
        self.first_name = first_name
        self.address_id = address_id
        self.phone = phone
        self.email = email
        self.status = status
