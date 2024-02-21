from . import *
from police_org.enums.sentence_type import SentenceType


class Sentences(Base):
    __tablename__ = 'sentences'

    id = Column("sentence_id", Integer, primary_key=True)
    crime_id = Column("crime_id", Integer, ForeignKey('crimes.crime_id'), nullable=False)
    start_date = Column("start_date", Date, nullable=False)
    end_date = Column("end_date", Date, nullable=False)
    sentence_type = Column("sentence_type", Enum(SentenceType), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, crime_id: int, start_date: date, end_date: date, sentence_type: SentenceType):
        self.crime_id = crime_id
        self.start_date = start_date
        self.end_date = end_date
        self.sentence_type = sentence_type
