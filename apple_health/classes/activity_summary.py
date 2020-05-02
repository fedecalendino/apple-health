from apple_health.util import parse_date, parse_float

DATE_COMPONENTS = "@dateComponents"
ACTIVE_ENERGY_BURNED = "@activeEnergyBurned"
ACTIVE_ENERGY_BURNED_GOAL = "@activeEnergyBurnedGoal"
ACTIVE_ENERGY_BURNED_UNIT = "@activeEnergyBurnedUnit"
APPLE_EXERCISE_TIME = "@appleExerciseTime"
APPLE_EXERCISE_TIME_GOAL = "@appleExerciseTimeGoal"
APPLE_STAND_HOURS = "@appleStandHours"
APPLE_STAND_HOURS_GOAL = "@appleStandHoursGoal"


class ActivitySummary:
    # a.k.a. The Rings

    def __init__(self, **data):
        self.date = parse_date(data.get(DATE_COMPONENTS))

        # Red
        self.active_energy_burned: float = parse_float(
            data.get(ACTIVE_ENERGY_BURNED)
        )
        self.active_energy_burned_goal: float = parse_float(
            data.get(ACTIVE_ENERGY_BURNED_GOAL)
        )
        self.active_energy_burned_unit: str = data.get(
            ACTIVE_ENERGY_BURNED_UNIT, "kcal"
        )

        # Green
        self.exercise_time: float = parse_float(
            data.get(APPLE_EXERCISE_TIME)
        )
        self.exercise_time_goal: float = parse_float(
            data.get(APPLE_EXERCISE_TIME_GOAL)
        )

        # Blue
        self.stand_hours: float = parse_float(
            data.get(APPLE_STAND_HOURS)
        )
        self.stand_hours_goal: float = parse_float(
            data.get(APPLE_STAND_HOURS_GOAL)
        )

    @property
    def active_energy_percent(self) -> float:
        if not self.active_energy_burned_goal:
            return 0.0

        return self.active_energy_burned / self.active_energy_burned_goal

    @property
    def exercise_time_percent(self) -> float:
        if not self.exercise_time_goal:
            return 0.0

        return self.exercise_time / self.exercise_time_goal

    @property
    def stand_hours_percent(self) -> float:
        if not self.stand_hours_goal:
            return 0.0

        return self.stand_hours / self.stand_hours_goal

    def __repr__(self) -> str:
        aep = int(100 * self.active_energy_percent)
        etp = int(100 * self.exercise_time_percent)
        shp = int(100 * self.stand_hours_percent)

        return f"{aep}% / {etp}% / {shp}%"
