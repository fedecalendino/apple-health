import xmltodict

from apple_health.classes import (
    Me,
    ActivitySummary,
    Correlation,
    Record,
    Workout,
)


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
