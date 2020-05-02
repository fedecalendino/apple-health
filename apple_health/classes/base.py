from datetime import datetime

from apple_health.constants import METADATA
from apple_health.util import parse_date


TYPE = "@type"
SOURCE_NAME = "@sourceName"
CREATION_DATE = "@creationDate"
START_DATE = "@startDate"
END_DATE = "@endDate"

KEY = "@key"
VALUE = "@value"


class Metadata:
    def __init__(self, **data):
        self.key = METADATA.get(data.get(KEY))
        self.value = data.get(VALUE)

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"


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

        self.metadata = list(map(
            lambda m: Metadata(**m),
            filter(
                lambda m: isinstance(m, dict) and m[KEY] in METADATA,
                data.get("MetadataEntry", [])
            )
        ))

    @property
    def seconds(self) -> int:
        return (self.end - self.start).seconds
