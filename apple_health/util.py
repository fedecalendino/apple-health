from datetime import datetime
from typing import Optional

from dateutil import parser

CONSTANTS = {
    "HKCategoryValueAppleStandHourIdle": 0,
    "HKCategoryValueAppleStandHourStood": 1,
    "HKCategoryValueSleepAnalysisAwake": 0,
    "HKCategoryValueSleepAnalysisInBed": 1,
    "HKCategoryValueSleepAnalysisAsleep": 2,
}


def parse_date(value: str) -> Optional[datetime]:
    if value is None:
        return None

    return parser.parse(value)


def parse_float(value: str, default: float = 0.0) -> float:
    if value is None:
        return default

    if value in CONSTANTS:
        return CONSTANTS[value]

    try:
        return float(value)
    except (ValueError, TypeError):
        return default



