from apple_health.classes.base import Sample
from apple_health.util import parse_float

WORKOUT_ACTIVITY_TYPE = "@workoutActivityType"
DURATION = "@duration"
DURATION_UNIT = "@durationUnit"
TOTAL_DISTANCE = "@totalDistance"
TOTAL_DISTANCE_UNIT = "@totalDistanceUnit"
TOTAL_ENERGY_BURNED = "@totalEnergyBurned"
TOTAL_ENERGY_BURNED_UNIT = "@totalEnergyBurnedUnit"
TOTAL_FLIGHTS_CLIMBED = "@totalFlightsClimbed"
TOTAL_SWIMMING_STROKE_COUNT = "@totalSwimmingStrokeCount"


class Workout(Sample):
    NAME_KEY = WORKOUT_ACTIVITY_TYPE

    def __init__(self, **data):
        super().__init__(**data)

        self.duration: float = parse_float(data.get(DURATION))
        self.duration_unit: str = data.get(DURATION_UNIT)

        self.distance: float = parse_float(data.get(TOTAL_DISTANCE))
        self.distance_unit: str = data.get(TOTAL_DISTANCE_UNIT)

        self.energy_burned: float = parse_float(data.get(TOTAL_ENERGY_BURNED))
        self.energy_burned_unit: str = data.get(TOTAL_ENERGY_BURNED_UNIT)

        self.flights_climbed: float = parse_float(
            data.get(TOTAL_FLIGHTS_CLIMBED)
        )
        self.swimming_strokes: float = parse_float(
            data.get(TOTAL_SWIMMING_STROKE_COUNT)
        )

    def __repr__(self) -> str:
        return f"{self.name}: {self.duration:0.2f} {self.duration_unit}"
