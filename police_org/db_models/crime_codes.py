from . import *


class CrimeCodes(Base):
    __tablename__ = "crime_codes"

    id = Column("code_id", Integer, primary_key=True)
    crime_code = Column("crime_code", String(10), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, crime_code: str):
        self.crime_code = crime_code
