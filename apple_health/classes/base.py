from datetime import datetime

from apple_health.util import parse_date


class HKRecord:
    NAME_KEY = "@type"
    TYPES = {}

    def __init__(self, **data):
        self.name: str = data[self.NAME_KEY]
        self.alias: str = self.TYPES[self.name]

        self.source: str = data.get("@sourceName")

        self.created_at: datetime = parse_date(data["@creationDate"])
        self.start: datetime = parse_date(data.get("@startDate"))
        self.end: datetime = parse_date(data.get("@endDate"))

    @property
    def seconds(self) -> int:
        return (self.end - self.start).seconds
