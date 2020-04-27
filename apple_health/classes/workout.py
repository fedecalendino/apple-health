from apple_health.classes.base import HKRecord

from apple_health.util import parse_float


class Workout(HKRecord):
    NAME_KEY = "@workoutActivityType"
    TYPES = {
        "HKWorkoutActivityTypeAmericanFootball": "American Football",
        "HKWorkoutActivityTypeArchery": "Archery",
        "HKWorkoutActivityTypeAustralianFootball": "Australian Football",
        "HKWorkoutActivityTypeBadminton": "Badminton",
        "HKWorkoutActivityTypeBaseball": "Baseball",
        "HKWorkoutActivityTypeBasketball": "Basketball",
        "HKWorkoutActivityTypeBowling": "Bowling",
        "HKWorkoutActivityTypeBoxing": "Boxing",
        "HKWorkoutActivityTypeClimbing": "Climbing",
        "HKWorkoutActivityTypeCricket": "Cricket",
        "HKWorkoutActivityTypeCrossTraining": "Cross Training",
        "HKWorkoutActivityTypeCurling": "Curling",
        "HKWorkoutActivityTypeCycling": "Cycling",
        "HKWorkoutActivityTypeDance": "Dance",
        "HKWorkoutActivityTypeDanceInspiredTraining": "Dance Inspired Training",
        "HKWorkoutActivityTypeElliptical": "Elliptical",
        "HKWorkoutActivityTypeEquestrianSports": "Equestrian Sports",
        "HKWorkoutActivityTypeFencing": "Fencing",
        "HKWorkoutActivityTypeFishing": "Fishing",
        "HKWorkoutActivityTypeFunctionalStrengthTraining": "Functional Strength Training",
        "HKWorkoutActivityTypeGolf": "Golf",
        "HKWorkoutActivityTypeGymnastics": "Gymnastics",
        "HKWorkoutActivityTypeHandball": "Handball",
        "HKWorkoutActivityTypeHighIntensityIntervalTraining": "High Intensity Interval Training",
        "HKWorkoutActivityTypeHiking": "Hiking",
        "HKWorkoutActivityTypeHockey": "Hockey",
        "HKWorkoutActivityTypeHunting": "Hunting",
        "HKWorkoutActivityTypeLacrosse": "Lacrosse",
        "HKWorkoutActivityTypeMartialArts": "Martial Arts",
        "HKWorkoutActivityTypeMindAndBody": "Mind And Body",
        "HKWorkoutActivityTypeMixedMetabolicCardioTraining": "Mixed Metabolic Cardio Training",
        "HKWorkoutActivityTypeOther": "Other",
        "HKWorkoutActivityTypePaddleSports": "Paddle Sports",
        "HKWorkoutActivityTypePlay": "Play",
        "HKWorkoutActivityTypePreparationAndRecovery": "Preparation And Recovery",
        "HKWorkoutActivityTypeRacquetball": "Racquetball",
        "HKWorkoutActivityTypeRowing": "Rowing",
        "HKWorkoutActivityTypeRugby": "Rugby",
        "HKWorkoutActivityTypeRunning": "Running",
        "HKWorkoutActivityTypeSailing": "Sailing",
        "HKWorkoutActivityTypeSkatingSports": "Skating Sports",
        "HKWorkoutActivityTypeSnowSports": "Snow Sports",
        "HKWorkoutActivityTypeSoccer": "Soccer",
        "HKWorkoutActivityTypeSoftball": "Softball",
        "HKWorkoutActivityTypeSquash": "Squash",
        "HKWorkoutActivityTypeStairClimbing": "Stair Climbing",
        "HKWorkoutActivityTypeSurfingSports": "Surfing Sports",
        "HKWorkoutActivityTypeSwimming": "Swimming",
        "HKWorkoutActivityTypeTableTennis": "Table Tennis",
        "HKWorkoutActivityTypeTennis": "Tennis",
        "HKWorkoutActivityTypeTrackAndField": "Track And Field",
        "HKWorkoutActivityTypeTraditionalStrengthTraining": "Traditional Strength Training",
        "HKWorkoutActivityTypeVolleyball": "Volleyball",
        "HKWorkoutActivityTypeWalking": "Walking",
        "HKWorkoutActivityTypeWaterFitness": "Water Fitness",
        "HKWorkoutActivityTypeWaterPolo": "Water Polo",
        "HKWorkoutActivityTypeWaterSports": "Water Sports",
        "HKWorkoutActivityTypeWrestling": "Wrestling",
        "HKWorkoutActivityTypeYoga": "Yoga",
    }

    def __init__(self, **data):
        super().__init__(**data)

        self.duration: float = parse_float(data.get("@duration"))
        self.duration_unit: str = data.get("@durationUnit")

        self.distance: float = parse_float(data.get("@totalDistance"))
        self.distance_unit: str = data.get("@totalDistanceUnit")

        self.flights_climbed: float = parse_float(data.get("@totalFlightsClimbed"))
        self.swimming_strokes: float = parse_float(data.get("@totalSwimmingStrokeCount"))

        self.energy_burned: float = parse_float(data.get("@totalEnergyBurned"))
        self.energy_burned_unit: str = data.get("@totalEnergyBurnedUnit")

    def __repr__(self) -> str:
        return f"{self.alias}: {self.duration} {self.duration_unit}"
