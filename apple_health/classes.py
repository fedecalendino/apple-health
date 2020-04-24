from datetime import datetime

import xmltodict

from apple_health.constants import CORRELATION_TYPES, RECORD_TYPES, WORKOUT_TYPES
from apple_health.util import parse_date, parse_value


class DateOfBirth:
    name = "@HKCharacteristicTypeIdentifierDateOfBirth"

    @staticmethod
    def parse(value):
        return datetime.strptime(value, "%Y-%m-%d")


class BiologicalSex:
    name = "@HKCharacteristicTypeIdentifierBiologicalSex"

    _values_ = {
        "HKBiologicalSexMale": "Male",
        "HKBiologicalSexFemale": "Female"
    }

    @staticmethod
    def parse(value):
        return BiologicalSex._values_[value]


class BloodType:
    name = "@HKCharacteristicTypeIdentifierBloodType"

    _values_ = {
        "HKBloodTypeAPositive": "A+",
    }

    @staticmethod
    def parse(value):
        return BloodType._values_[value]


class SkinType:
    name = "@HKCharacteristicTypeIdentifierFitzpatrickSkinType"

    _values_ = {
        "HKFitzpatrickSkinTypeII": "Type II",
    }

    @staticmethod
    def parse(value):
        return SkinType._values_[value]


class Me:
    def __init__(self, **data):
        self.birth_date = DateOfBirth.parse(data[DateOfBirth.name])
        self.biological_sex = BiologicalSex.parse(data[BiologicalSex.name])
        self.blood_type = BloodType.parse(data[BloodType.name])
        self.skin_type = SkinType.parse(data[SkinType.name])

    @property
    def age(self) -> int:
        if not self.birth_date:
            return None

        return (datetime.now() - self.birth_date).days // 365

    def __repr__(self):
        return f"{self.biological_sex}, {self.age} years old ({self.blood_type}/{self.skin_type})"


class ActivitySummary:
    # a.k.a. The Rings

    def __init__(self, **data):
        self.date = parse_date(data.get("@dateComponents"))

        self.active_energy_burned = parse_value(
            data.get("@activeEnergyBurned", 0)
        )
        self.active_energy_burned_goal = parse_value(
            data.get("@activeEnergyBurnedGoal", 0)
        )
        self.active_energy_burned_unit = parse_value(
            data.get("@activeEnergyBurnedUnit")
        )

        self.exercise_time = parse_value(
            data.get("@appleExerciseTime", 0)
        )
        self.exercise_time_goal = parse_value(
            data.get("@appleExerciseTimeGoal", 0)
        )

        self.stand_hours = parse_value(
            data.get("@appleStandHours", 0)
        )
        self.stand_hours_goal = parse_value(
            data.get("@appleStandHoursGoal", 0)
        )

    @property
    def active_energy_percent(self) -> float:
        if self.active_energy_burned_goal == 0:
            return 0

        return self.active_energy_burned/self.active_energy_burned_goal

    @property
    def exercise_time_percent(self) -> float:
        if self.exercise_time_goal == 0:
            return 0

        return self.exercise_time / self.exercise_time_goal

    @property
    def stand_hours_percent(self) -> float:
        if self.stand_hours_goal == 0:
            return 0

        return self.stand_hours / self.stand_hours_goal

    def __repr__(self):
        aep = int(100 * self.active_energy_percent)
        et = int(100 * self.exercise_time_percent)
        sh = int(100 * self.stand_hours_percent)

        return f"{aep}% / {et}% / {sh}%"


class Record:
    def __init__(self, **data):
        self.name = data["@type"]
        self.alias = RECORD_TYPES[self.name]

        self.unit = data.get("@unit")
        self.value = parse_value(data.get("@value"))

        self.source = data.get("@sourceName")

        self.created_at = parse_date(data["@creationDate"])
        self.start = parse_date(data.get("@startDate"))
        self.end = parse_date(data.get("@endDate"))

    @property
    def lenght(self):
        return (self.end - self.start).seconds

    def __repr__(self):
        return f"{self.alias}: {self.value} {self.created_at}"


class Correlation:
    def __init__(self, **data):
        self.name = data["@type"]
        self.alias = CORRELATION_TYPES[self.name]

        self.unit = data.get("@unit")
        self.value = parse_value(data.get("@value"))

        self.source = data.get("@sourceName")

        self.created_at = parse_date(data["@creationDate"])
        self.start = parse_date(data.get("@startDate"))
        self.end = parse_date(data.get("@endDate"))

        self.records = list(map(
            lambda record_data: Record(**record_data),
            data.get("Record", [])
        ))

    @property
    def lenght(self):
        return (self.end - self.start).seconds

    def __repr__(self):
        return f"{self.alias}: {len(self.records)} records"


class Workout:
    def __init__(self, **data):
        self.name = data["@workoutActivityType"]
        self.alias = WORKOUT_TYPES[self.name]

        self.source = data.get("@sourceName")

        self.duration = parse_value(data.get("@duration", 0))
        self.duration_unit = data.get("@durationUnit")

        self.total_distance = parse_value(data.get("@totalDistance", 0))
        self.total_distance_unit = data.get("@totalDistanceUnit")

        self.total_energy_burned = parse_value(data.get("@@totalEnergyBurned", 0))
        self.total_energy_burned_unit = data.get("@@totalEnergyBurnedUnit")

        self.created_at = parse_date(data["@creationDate"])
        self.start = parse_date(data.get("@startDate"))
        self.end = parse_date(data.get("@endDate"))

    @property
    def lenght(self):
        return (self.end - self.start).seconds

    def __repr__(self):
        return f"{self.alias}: {self.duration} {self.duration_unit}"


class HealthData:

    def __init__(self):
        self.me = None
        self.activity_summaries = []
        self.correlations = []
        self.records = []
        self.workouts = []

    @staticmethod
    def read(
            file_name: str,
            include_me: bool = True,
            include_activity_summaries: bool = True,
            include_correlations: bool = True,
            include_records: bool = True,
            include_workouts: bool = True,
    ) -> "HealthData":
        with open(file_name) as file:
            xml = xmltodict.parse(file.read())
            data = xml["HealthData"]

        health_data = HealthData()

        if include_me:
            print("Reading: Me...")
            health_data.me = Me(**data["Me"])

        if include_activity_summaries:
            print("Reading: ActivitySummary...")
            health_data.activity_summaries = list(map(
                lambda a: ActivitySummary(**a),
                data.get("ActivitySummary", [])
            ))

        if include_correlations:
            print("Reading: Correlation...")
            health_data.correlations = list(map(
                lambda c: Correlation(**c),
                data.get("Correlation", [])
            ))

        if include_records:
            print("Reading: Record...")
            health_data.records = list(map(
                lambda r: Record(**r),
                data.get("Record", [])
            ))

        if include_workouts:
            print("Reading: Workout...")
            health_data.workouts = list(map(
                lambda w: Workout(**w),
                data.get("Workout", [])
            ))

        return health_data
