from . import *



class CrimeOfficers(Base):
    __tablename__ = 'crime_officers_mapping'

    crime_officers_id = Column('crime_officers_id', Integer, primary_key=True)
    crime_id = Column('crime_id', Integer, ForeignKey('crimes.crime_id'), nullable=False)
    officer_id = Column('officer_id', Integer, ForeignKey('police_officers.officer_id'), nullable=False)
