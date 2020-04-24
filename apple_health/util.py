from dateutil import parser


def parse_date(value):
    if value is None:
        return None

    return parser.parse(value)


def parse_value(value):
    if value is None:
        return None

    try:
        if "." in value:
            return float(value)
    except:
        pass

    try:
        return int(value)
    except:
        pass

    return value\
        .replace("HKCategoryValueAppleStandHour", "")\
        .replace("HKCategoryValueSleepAnalysis", "")
