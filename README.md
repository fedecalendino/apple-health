# apple-health

[![Version](https://img.shields.io/pypi/v/apple-health?logo=pypi)](https://pypi.org/project/apple-health)
[![Build Status](https://img.shields.io/travis/fedecalendino/apple-health/master?logo=travis)](https://travis-ci.com/fedecalendino/apple-health)
[![Quality Gate Status](https://img.shields.io/sonar/alert_status/fedecalendino_apple-health?logo=sonarcloud&server=https://sonarcloud.io)](https://sonarcloud.io/dashboard?id=fedecalendino_apple-health)
[![CodeCoverage](https://img.shields.io/codecov/c/gh/fedecalendino/apple-health?logo=codecov)](https://codecov.io/gh/fedecalendino/apple-health)

---

```python
from apple_health import HealthData

FILE = "./export/export.xml"
health_data = HealthData.read(FILE)

print(f"{len(health_data.activity_summaries)} activity records")
print(f"{len(health_data.correlations)} correlations")
print(f"{len(health_data.records)} records")
print(f"{len(health_data.workouts)} workouts")
```

```text
>> 25 activity records
>> 37 correlations
>> 47013 records
>> 17 workouts
```