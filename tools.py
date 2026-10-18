CITY_CODES = {
    "paris": "PAR",
    "tokyo": "TYO",
    "nairobi": "NBO",
}


def multiply(a, b):
    return int(a) * int(b)


def lookup_city(name):
    key = str(name).strip().lower()
    if key not in CITY_CODES:
        raise KeyError(key)
    return CITY_CODES[key]
