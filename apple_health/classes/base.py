from datetime import datetime

from apple_health.util import parse_date

TYPE = "@type"
SOURCE_NAME = "@sourceName"
CREATION_DATE = "@creationDate"
START_DATE = "@startDate"
END_DATE = "@endDate"


class Sample:
    NAME_KEY = TYPE
    TYPES = {}

    def __init__(self, **data):
        self.key: str = data[self.NAME_KEY]
        self.name: str = self.TYPES[self.key]

        self.source: str = data.get(SOURCE_NAME)

        self.created_at: datetime = parse_date(data.get(CREATION_DATE))
        self.start: datetime = parse_date(data.get(START_DATE))
        self.end: datetime = parse_date(data.get(END_DATE))

    @property
    def seconds(self) -> int:
        return (self.end - self.start).seconds
