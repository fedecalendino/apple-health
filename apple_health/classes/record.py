from apple_health.classes.base import Sample
from apple_health.constants import RECORDS
from apple_health.util import parse_float

UNIT = "@unit"
VALUE = "@value"


class Record(Sample):
    TYPES = RECORDS

    def __init__(self, **data):
        super().__init__(**data)

        self.unit: str = data.get(UNIT)
        self.value: float = parse_float(data.get(VALUE))

    def __repr__(self):
        return f"{self.name}: {self.value} {self.unit} {self.created_at}"
