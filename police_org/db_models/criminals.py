from . import *


class Criminals(Base):
    __tablename__ = 'criminals'

    id = Column('criminal_id', Integer, primary_key=True)
    first_name = Column('first_name', String(10), nullable=False)
    last_name = Column('last_name', String(10), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.address_id'), nullable=False)
    phone_number = Column('phone_number', String(10), nullable=False)
    violent_status = Column('v_status', BOOLEAN, nullable=False, default=False)
    probation_status = Column('p_status', BOOLEAN, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), onupdate=datetime.now())

    def __init__(self, first_name: str, last_name: str, address_id: int, phone_number: str,
                 v_status: bool, p_status: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.address_id = address_id
        self.phone_number = phone_number
        self.violent_status = v_status
        self.probation_status = p_status


class CriminalAliases(Base):
    __tablename__ = 'criminal_alias'

    id = Column('criminal_alias_id', Integer, primary_key=True)
    criminal_id = Column('criminal_id', ForeignKey('criminals.criminal_id'), nullable=False)
    alias = Column(String(10), nullable=False)
    criminal = relationship('Criminals', back_populates='aliases')
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    modified_at = Column(DateTime(timezone=True), default=datetime.now())

    def __init__(self, criminal_id: int, alias: str):
        self.criminal_id = criminal_id
        self.alias = alias
