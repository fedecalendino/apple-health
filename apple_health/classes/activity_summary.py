from apple_health.util import parse_date, parse_float


class ActivitySummary:
    # a.k.a. The Rings

    def __init__(self, **data):
        self.date = parse_date(data.get("@dateComponents"))

        # Red
        self.active_energy_burned: float = parse_float(data.get("@activeEnergyBurned"))
        self.active_energy_burned_goal: float = parse_float(data.get("@activeEnergyBurnedGoal"))
        self.active_energy_burned_unit: str = data.get("@activeEnergyBurnedUnit", "kcal")

        # Green
        self.exercise_time: float = parse_float(data.get("@appleExerciseTime"))
        self.exercise_time_goal: float = parse_float(data.get("@appleExerciseTimeGoal"))

        # Blue
        self.stand_hours: float = parse_float(data.get("@appleStandHours"))
        self.stand_hours_goal: float = parse_float(data.get("@appleStandHoursGoal"))

    @property
    def active_energy_percent(self) -> float:
        if not self.active_energy_burned_goal:
            return 0.0

        return self.active_energy_burned/self.active_energy_burned_goal

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
