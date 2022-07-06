# apple-health

[![Version](https://img.shields.io/pypi/v/apple-health?logo=pypi)](https://pypi.org/project/apple-health)
[![Quality Gate Status](https://img.shields.io/sonar/alert_status/fedecalendino_apple-health?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_apple-health)
[![CodeCoverage](https://img.shields.io/sonar/coverage/fedecalendino_apple-health?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_apple-health)

---

```python
from health import HealthData

FILE = "./export/export.xml"
data = HealthData.read(FILE)

print(f"{len(data.activity_summaries)} activity records")
print(f"{len(data.correlations)} correlations")
print(f"{len(data.records)} records")
print(f"{len(data.workouts)} workouts")
```

```text
>> 322 activity records
>> 0 correlations
>> 650919 records
>> 129 workouts
```
