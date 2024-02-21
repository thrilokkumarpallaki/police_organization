from . import *
from police_org.enums.charge_appeal_status import ChargeAppealStatus


class Appeals(Base):
    __tablename__ = 'appeals'

    id = Column("appeal_id", Integer, primary_key=True)
    crime_id = Column("crime_id", Integer, ForeignKey('crimes.crime_id'))
    filing_date = Column("filing_date", Date, nullable=False)
    hearing_date = Column("hearing_date", Date, nullable=False)
    status = Column("appeal_status", Enum(ChargeAppealStatus), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, crime_id: int, filing_date: date, hearing_date: date, status: ChargeAppealStatus):
        self.crime_id = crime_id
        self.filing_date = filing_date
        self.hearing_date = hearing_date
        self.status = status
