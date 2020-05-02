HK_BIOLOGICAL_SEX_NOT_SET = "HKBiologicalSexNotSet"
HK_BIOLOGICAL_SEX_FEMALE = "HKBiologicalSexFemale"
HK_BIOLOGICAL_SEX_MALE = "HKBiologicalSexMale"
HK_BIOLOGICAL_SEX_OTHER = "HKBiologicalSexOther"
HK_BLOOD_TYPE_NOT_SET = "HKBloodTypeNotSet"
HK_BLOOD_TYPE_O_POSITIVE = "HKBloodTypeOPositive"
HK_BLOOD_TYPE_O_NEGATIVE = "HKBloodTypeONegative"
HK_BLOOD_TYPE_A_POSITIVE = "HKBloodTypeAPositive"
HK_BLOOD_TYPE_A_NEGATIVE = "HKBloodTypeANegative"
HK_BLOOD_TYPE_B_POSITIVE = "HKBloodTypeBPositive"
HK_BLOOD_TYPE_B_NEGATIVE = "HKBloodTypeBNegative"
HK_BLOOD_TYPE_A_B_POSITIVE = "HKBloodTypeABPositive"
HK_BLOOD_TYPE_A_B_NEGATIVE = "HKBloodTypeABNegative"
HK_FITZPATRICK_SKIN_TYPE_NOT_SET = "HKFitzpatrickSkinTypeNotSet"
HK_FITZPATRICK_SKIN_TYPE_I = "HKFitzpatrickSkinTypeI"
HK_FITZPATRICK_SKIN_TYPE_I_I = "HKFitzpatrickSkinTypeII"
HK_FITZPATRICK_SKIN_TYPE_I_I_I = "HKFitzpatrickSkinTypeIII"
HK_FITZPATRICK_SKIN_TYPE_I_V = "HKFitzpatrickSkinTypeIV"
HK_FITZPATRICK_SKIN_TYPE_V = "HKFitzpatrickSkinTypeV"
HK_FITZPATRICK_SKIN_TYPE_V_I = "HKFitzpatrickSkinTypeVI"
HK_WHEELCHAIR_USE_NOT_SET = "HKWheelchairUseNotSet"
HK_WHEELCHAIR_USE_NO = "HKWheelchairUseNo"
HK_WHEELCHAIR_USE_YES = "HKWheelchairUseYes"

BIOLOGICAL_SEX_FEMALE = "Female"
BIOLOGICAL_SEX_MALE = "Male"
BIOLOGICAL_SEX_OTHER = "Other"

BLOOD_TYPE_A_NEGATIVE = "A–"
BLOOD_TYPE_A_POSITIVE = "A+"
BLOOD_TYPE_AB_NEGATIVE = "AB–"
BLOOD_TYPE_AB_POSITIVE = "AB+"
BLOOD_TYPE_B_NEGATIVE = "B–"
BLOOD_TYPE_B_POSITIVE = "B+"
BLOOD_TYPE_O_NEGATIVE = "O–"
BLOOD_TYPE_O_POSITIVE = "O+"

SKIN_TYPE_I = "Type I"
SKIN_TYPE_II = "Type II"
SKIN_TYPE_III = "Type III"
SKIN_TYPE_IV = "Type IV"
SKIN_TYPE_V = "Type V"
SKIN_TYPE_VI = "Type VI"

BIOLOGICAL_SEXES = {
    HK_BIOLOGICAL_SEX_NOT_SET: None,
    HK_BIOLOGICAL_SEX_FEMALE: BIOLOGICAL_SEX_FEMALE,
    HK_BIOLOGICAL_SEX_MALE: BIOLOGICAL_SEX_MALE,
    HK_BIOLOGICAL_SEX_OTHER: BIOLOGICAL_SEX_OTHER,
}

BLOOD_TYPES = {
    HK_BLOOD_TYPE_NOT_SET: None,
    HK_BLOOD_TYPE_O_POSITIVE: BLOOD_TYPE_O_POSITIVE,
    HK_BLOOD_TYPE_O_NEGATIVE: BLOOD_TYPE_O_NEGATIVE,
    HK_BLOOD_TYPE_A_POSITIVE: BLOOD_TYPE_A_POSITIVE,
    HK_BLOOD_TYPE_A_NEGATIVE: BLOOD_TYPE_A_NEGATIVE,
    HK_BLOOD_TYPE_B_POSITIVE: BLOOD_TYPE_B_POSITIVE,
    HK_BLOOD_TYPE_B_NEGATIVE: BLOOD_TYPE_B_NEGATIVE,
    HK_BLOOD_TYPE_A_B_POSITIVE: BLOOD_TYPE_AB_POSITIVE,
    HK_BLOOD_TYPE_A_B_NEGATIVE: BLOOD_TYPE_AB_NEGATIVE,
}

SKIN_TYPES = {
    HK_FITZPATRICK_SKIN_TYPE_NOT_SET: None,
    HK_FITZPATRICK_SKIN_TYPE_I: SKIN_TYPE_I,
    HK_FITZPATRICK_SKIN_TYPE_I_I: SKIN_TYPE_II,
    HK_FITZPATRICK_SKIN_TYPE_I_I_I: SKIN_TYPE_III,
    HK_FITZPATRICK_SKIN_TYPE_I_V: SKIN_TYPE_IV,
    HK_FITZPATRICK_SKIN_TYPE_V: SKIN_TYPE_V,
    HK_FITZPATRICK_SKIN_TYPE_V_I: SKIN_TYPE_VI,
}

WHEELCHAIR_USES = {
    HK_WHEELCHAIR_USE_NOT_SET: None,
    HK_WHEELCHAIR_USE_NO: False,
    HK_WHEELCHAIR_USE_YES: True,
}