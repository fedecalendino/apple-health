from datetime import datetime
from typing import Optional

from dateutil import parser

CONSTANTS = {
    "HKCategoryValueNotApplicable": 0,
    "HKCategoryValueAppleStandHourStood": 0,
    "HKCategoryValueAppleStandHourIdle": 1,
    "HKCategoryValueAudioExposureEventLoudEnvironment": 1,
    "HKCategoryValueCervicalMucusQualityDry": 1,
    "HKCategoryValueCervicalMucusQualitySticky": 2,
    "HKCategoryValueCervicalMucusQualityCreamy": 3,
    "HKCategoryValueCervicalMucusQualityWatery": 4,
    "HKCategoryValueCervicalMucusQualityEggWhite": 5,
    "HKCategoryValueOvulationTestResultNegative": 1,
    "HKCategoryValueOvulationTestResultLuteinizingHormoneSurge": 2,
    "HKCategoryValueOvulationTestResultIndeterminate": 3,
    "HKCategoryValueOvulationTestResultEstrogenSurge": 4,
    "HKCategoryValueSleepAnalysisInBed": 0,
    "HKCategoryValueSleepAnalysisAsleep": 1,
    "HKCategoryValueSleepAnalysisAwake": 2,
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



