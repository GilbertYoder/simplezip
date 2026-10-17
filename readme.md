https://simplezip.dev/

A simple API for retreiving zip information.

Data from: https://download.geonames.org/export/zip/US.zip<br>
Licensed under CC BY 4.0<br>
Data converted to JSON and field names modified.<br>

**Usage**

```bash
(base) ➜  ~ curl https://simplezip.dev/us/24554.json
{
  "countryCode": "US",
  "postalCode": "24554",
  "city": "Gladys",
  "state": "Virginia",
  "stateCode": "VA",
  "county": "Campbell",
  "countyCode": "031",
  "community": "",
  "communityCode": "",
  "latitude": 37.1386,
  "longitude": -79.1048,
  "accuracy": 4
}
```
