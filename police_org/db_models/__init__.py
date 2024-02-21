from datetime import datetime, timedelta, date

from sqlalchemy import UniqueConstraint, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BOOLEAN, CHAR, Column, Date, DateTime, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import ARRAY, NUMERIC, TIME

from .db_connect import session, engine


Base = declarative_base()


from .crimes import Crimes
from .address import Addresses
from .appeals import Appeals
from .crime_charges import CrimeCharges
from .crime_officers_mapping import CrimeOfficers
from .crime_codes import CrimeCodes
from .criminals import Criminals
from .criminals import CriminalAliases
from .police_officers import PoliceOfficers
from .probation_officers import ProbationOfficers
from .sentences import Sentences

Base.metadata.create_all(bind=engine)
