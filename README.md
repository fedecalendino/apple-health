# apple-health

[![Version](https://img.shields.io/pypi/v/apple-health?logo=pypi)](https://pypi.org/project/apple-health)
[![Quality Gate Status](https://img.shields.io/sonar/alert_status/fedecalendino_apple-health?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_apple-health)
[![CodeCoverage](https://img.shields.io/sonar/coverage/fedecalendino_apple-health?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_apple-health)


Library to extract information from Apple Health exports.

---

## Setup

To use this library, is required to provide an export file from the iOS Apple Health app. 

### How to get the export

1. Open the Apple Health app on your iOS device.
2. Tap on your profile picture on the top-right corner.
3. Scroll down until you see a button that reads "Export All Health Data".
4. After pressing the button, a dialog will appear while the export process is ongoing (it might take a while).
5. Once the process is finished, a file called `apple_health_export.zip` will be generated.
6. Finally, from that zip file you'll need only the file named `export.xml`.
 

## Usage

```python
from health import HealthData

FILE = "./export/export.xml"
data = HealthData.read(
    FILE,
    include_me=True,
    include_activity_summaries=True,
    include_correlations=False,
    include_records=False,
    include_workouts=True,
)

print(data.me.biological_sex)
print(f"{len(data.activity_summaries)} activity records")
print(f"{len(data.correlations)} correlations")
print(f"{len(data.records)} records")
print(f"{len(data.workouts)} workouts")
```

```text
>> HKBiologicalSexMale
>> 322 activity records
>> 0 correlations
>> 0 records
>> 129 workouts
```

> note: use the flags on the `HealthData.read` to include only what you need to speed up the reading process.