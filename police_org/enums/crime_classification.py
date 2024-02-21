from . import *


class CrimeClassification(enum.Enum):
    UNDEFINED = 0
    FELONY = 1
    MISDEMEANOR = 2
    OTHER = 3
