from . import *
from police_org.enums.crime_classification import CrimeClassification
from police_org.enums.appeal_status import AppealStatus
from .crime_officers_mapping import CrimeOfficers
from .criminals import Criminals


class Crimes(Base):
    __tablename__ = 'crimes'

    id = Column('crime_id', Integer, primary_key=True)
    criminal_id = Column('criminal_id', ForeignKey('criminals.criminal_id'), nullable=False)
    classification = Column('crime_classification', Enum(CrimeClassification), nullable=False)
    date_charged = Column('date_charged', Date, nullable=False)
    appeal_status = Column('appeal_status', Enum(AppealStatus), nullable=False)
    hearing_date = Column('hearing_date', Date, nullable=False)
    appeal_cut_date = Column('appeal_cut_date', Date, nullable=False)
    officers = relationship('police_officers', secondary=CrimeOfficers)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), default=datetime.now())

    def __init__(self, criminal_id: int, classification: CrimeClassification, date_charged: date,
                 appeal_status: AppealStatus, hearing_date: date, appeal_cut_date: date):
        self.criminal_id = criminal_id
        self.classification = classification
        self.date_charged = date_charged
        self.appeal_status = appeal_status
        self.hearing_date = hearing_date
        self.appeal_cut_date = appeal_cut_date
