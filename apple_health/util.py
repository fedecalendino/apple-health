from datetime import datetime, time
from typing import Optional

from dateutil import parser

from apple_health.constants import record

CONSTANTS = {
    record.HK_RECORD_NOT_APPLICABLE: 0,
    record.HK_RECORD_APPLE_STAND_HOUR_STOOD: 0,
    record.HK_RECORD_APPLE_STAND_HOUR_IDLE: 1,
    record.HK_RECORD_AUDIO_EXPOSURE_EVENT_LOUD_ENVIRONMENT: 1,
    record.HK_RECORD_CERVICAL_MUCUS_QUALITY_DRY: 1,
    record.HK_RECORD_CERVICAL_MUCUS_QUALITY_STICKY: 2,
    record.HK_RECORD_CERVICAL_MUCUS_QUALITY_CREAMY: 3,
    record.HK_RECORD_CERVICAL_MUCUS_QUALITY_WATERY: 4,
    record.HK_RECORD_CERVICAL_MUCUS_QUALITY_EGG_WHITE: 5,
    record.HK_RECORD_OVULATION_TEST_RESULT_NEGATIVE: 1,
    record.HK_RECORD_OVULATION_TEST_RESULT_LUTEINIZING_HORMONE_SURGE: 2,
    record.HK_RECORD_OVULATION_TEST_RESULT_INDETERMINATE: 3,
    record.HK_RECORD_OVULATION_TEST_RESULT_ESTROGEN_SURGE: 4,
    record.HK_RECORD_SLEEP_ANALYSIS_IN_BED: 0,
    record.HK_RECORD_SLEEP_ANALYSIS_ASLEEP: 1,
    record.HK_RECORD_SLEEP_ANALYSIS_AWAKE: 2,
}


def parse_date(value: str) -> Optional[datetime]:
    if value is None:
        return None

    return parser.parse(value)


def parse_time(value: str) -> Optional[time]:
    if value is None:
        return None

    return parser.parse(value).time()


def parse_float(value: str, default: float = 0.0) -> float:
    if value is None:
        return default

    if value in CONSTANTS:
        return CONSTANTS[value]

    try:
        return float(value)
    except (ValueError, TypeError):
        return default



