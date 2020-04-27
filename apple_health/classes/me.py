from datetime import datetime
from typing import Optional, Union

DATE_OF_BIRTH = "@HKCharacteristicTypeIdentifierDateOfBirth"
BIOLOGICAL_SEX = "@HKCharacteristicTypeIdentifierBiologicalSex"
BLOOD_TYPE = "@HKCharacteristicTypeIdentifierBloodType"
SKIN_TYPE = "@HKCharacteristicTypeIdentifierFitzpatrickSkinType"
WHEELCHAIR_USE = "@HKCharacteristicTypeIdentifierWheelchairUse"

CONSTANTS = {
    BIOLOGICAL_SEX: {
        "HKBiologicalSexNotSet": None,
        "HKBiologicalSexFemale": "Female",
        "HKBiologicalSexMale": "Male",
        "HKBiologicalSexOther": "Other",
    },
    BLOOD_TYPE: {
        "HKBloodTypeNotSet": None,
        "HKBloodTypeOPositive": "O+",
        "HKBloodTypeONegative": "O–",
        "HKBloodTypeAPositive": "A+",
        "HKBloodTypeANegative": "A–",
        "HKBloodTypeBPositive": "B+",
        "HKBloodTypeBNegative": "B–",
        "HKBloodTypeABPositive": "AB+",
        "HKBloodTypeABNegative": "AB–",
    },
    SKIN_TYPE: {
        "HKFitzpatrickSkinTypeNotSet": None,
        "HKFitzpatrickSkinTypeI": "Type I",
        "HKFitzpatrickSkinTypeII": "Type II",
        "HKFitzpatrickSkinTypeIII": "Type III",
        "HKFitzpatrickSkinTypeIV": "Type IV",
        "HKFitzpatrickSkinTypeV": "Type V",
        "HKFitzpatrickSkinTypeVI": "Type VI",
    },
    WHEELCHAIR_USE: {
        "HKWheelchairUseNotSet": None,
        "HKWheelchairUseNo": False,
        "HKWheelchairUseYes": True,
    },
}


def _get_date_of_birth(data) -> Optional[datetime]:
    try:
        return datetime.strptime(data.get(DATE_OF_BIRTH), "%Y-%m-%d")
    except ValueError:
        return None


def _get_constant(data, name: str) -> Union[str, bool]:
    return CONSTANTS[name].get(data.get(name), None)


class Me:
    def __init__(self, **data):
        self.date_of_birth = _get_date_of_birth(data)
        self.biological_sex = _get_constant(data, BIOLOGICAL_SEX)
        self.blood_type = _get_constant(data, BLOOD_TYPE)
        self.skin_type = _get_constant(data, SKIN_TYPE)
        self.wheelchair_use = _get_constant(data, WHEELCHAIR_USE)

    @property
    def age(self) -> Optional[int]:
        if not self.date_of_birth:
            return None

        return (datetime.now() - self.date_of_birth).days // 365

    def __repr__(self):
        return f"{self.biological_sex}, {self.age} years old"
