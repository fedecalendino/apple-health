from datetime import datetime
from typing import Optional

from apple_health.constants import (
    BIOLOGICAL_SEXES,
    BLOOD_TYPES,
    SKIN_TYPES,
    WHEELCHAIR_USES,
)

DATE_OF_BIRTH = "@HKCharacteristicTypeIdentifierDateOfBirth"
BIOLOGICAL_SEX = "@HKCharacteristicTypeIdentifierBiologicalSex"
BLOOD_TYPE = "@HKCharacteristicTypeIdentifierBloodType"
SKIN_TYPE = "@HKCharacteristicTypeIdentifierFitzpatrickSkinType"
WHEELCHAIR_USE = "@HKCharacteristicTypeIdentifierWheelchairUse"


class Me:
    def __init__(self, **data):
        try:
            self.date_of_birth: datetime = datetime.strptime(
                data.get(DATE_OF_BIRTH),
                "%Y-%m-%d"
            )
        except (ValueError, TypeError):
            self.date_of_birth = None

        self.biological_sex: str = BIOLOGICAL_SEXES.get(
            data.get(BIOLOGICAL_SEX)
        )
        self.blood_type: str = BLOOD_TYPES.get(
            data.get(BLOOD_TYPE)
        )
        self.skin_type: str = SKIN_TYPES.get(
            data.get(SKIN_TYPE)
        )
        self.wheelchair_use: bool = WHEELCHAIR_USES.get(
            data.get(WHEELCHAIR_USE)
        )

    @property
    def age(self) -> Optional[int]:
        if not self.date_of_birth:
            return None

        return (datetime.now() - self.date_of_birth).days // 365

    def __repr__(self):
        return f"{self.biological_sex}, {self.age} years old"
