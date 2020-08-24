from datetime import datetime
from typing import Optional

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

        self.biological_sex: str = data.get(BIOLOGICAL_SEX)
        self.blood_type: str = data.get(BLOOD_TYPE)
        self.skin_type: str = data.get(SKIN_TYPE)
        self.wheelchair_use: bool = data.get(WHEELCHAIR_USE)

    @property
    def age(self) -> Optional[int]:
        if not self.date_of_birth:
            return None

        return (datetime.now() - self.date_of_birth).days // 365

    def __repr__(self):
        return f"{self.biological_sex}, {self.age} years old"
