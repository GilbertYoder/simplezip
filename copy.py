import json

with open("./src/US.txt", "r") as f:
    for line in f:
        raw = line.rstrip("\n").split("\t")
        data = {
            "countryCode": raw[0],
            "postalCode": raw[1],
            "city": raw[2],
            "state": raw[3],
            "stateCode": raw[4],
            "county": raw[5],
            "countyCode": raw[6],
            "community": raw[7],
            "communityCode": raw[8],
            "latitude": float(raw[9]) if raw[9] else None,
            "longitude": float(raw[10]) if raw[10] else None,
            "accuracy": int(raw[11]) if raw[11] else None,
        }
        postal = data["postalCode"]
        with open(f"./us/{postal}.json", "w") as f:
            json.dump(data, f, indent=2)
