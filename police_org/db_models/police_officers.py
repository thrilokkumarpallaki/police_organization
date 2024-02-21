from . import *
from police_org.enums.officer_status import OfficerStatus


class PoliceOfficers(Base):
    __tablename__ = 'police_officers'

    id = Column("officer_id", Integer, primary_key=True)
    last_name = Column("last_name", String(10), nullable=False)
    first_name = Column("first_name", String(15), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.address_id'), nullable=False)
    precinct = Column(String(10), nullable=False)
    badge = Column(String(6), unique=True, nullable=False)
    phone = Column(String(10), nullable=False)
    status = Column("officer_status", Enum(OfficerStatus))
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, last_name: str, first_name: str, precinct: str, badge: str, phone: str, status: OfficerStatus):
        self.last_name = last_name
        self.first_name = first_name
        self.precinct = precinct
        self.badge = badge
        self.phone = phone
        self.status = status
