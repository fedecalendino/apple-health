from apple_health.classes.base import Sample
from apple_health.util import parse_float, parse_time
from typing import List

UNIT = "@unit"
VALUE = "@value"
BPM = "@bpm"
TIME = "@time"


class HeartRateVariability:
    def __init__(self, **data):
        self.bpm = parse_float(data.get(BPM, 0.0))
        self.timestamp = parse_time(data.get(TIME))

    def __repr__(self) -> str:
        return f"{self.bpm:0.2f} bpm"


class Record(Sample):
    def __init__(self, **data):
        super().__init__(**data)

        self.unit: str = data.get(UNIT)
        self.value: float = parse_float(data.get(VALUE))
        self.heart_rate: List[HeartRateVariability] = []

    def __repr__(self):
        return f"{self.name}: {self.value:0.2f} {self.unit} {self.created_at}"
