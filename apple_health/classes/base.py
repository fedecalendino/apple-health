from datetime import datetime

from apple_health.util import parse_date


TYPE = "@type"
SOURCE_NAME = "@sourceName"
CREATION_DATE = "@creationDate"
START_DATE = "@startDate"
END_DATE = "@endDate"

KEY = "@key"
VALUE = "@value"


class MetaData:
    def __init__(self, **data):
        self.key = data.get(KEY)
        self.value = data.get(VALUE)

    def __repr__(self) -> str:
        return f"{self.key}: {self.value}"


class Sample:
    NAME_KEY = TYPE

    def __init__(self, **data):
        self.name: str = data[self.NAME_KEY]

        self.source: str = data.get(SOURCE_NAME)

        self.created_at: datetime = parse_date(data.get(CREATION_DATE))
        self.start: datetime = parse_date(data.get(START_DATE))
        self.end: datetime = parse_date(data.get(END_DATE))

        metadata = data.get("MetadataEntry")

        if metadata is None:
            self.metadata = []
        elif isinstance(metadata, dict):
            self.metadata = [MetaData(**metadata)]
        elif isinstance(metadata, list):
            self.metadata = list(map(
                lambda m: MetaData(**m),
                metadata
            ))

    @property
    def seconds(self) -> int:
        return (self.end - self.start).seconds
