from typing import List

from apple_health.classes.base import Sample
from apple_health.classes.record import Record
from apple_health.util import parse_float

UNIT = "@unit"
VALUE = "@value"


class Correlation(Sample):
    def __init__(self, **data):
        super().__init__(**data)

        self.unit: str = data.get(UNIT)
        self.value: float = parse_float(data.get(VALUE))

        self.records: List[Record] = list(map(
            lambda record_data: Record(**record_data),
            data.get("Record", [])
        ))

    def __repr__(self) -> str:
        return f"{self.name}: {len(self.records)} records"
