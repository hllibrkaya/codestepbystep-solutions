def rarest_age(d):
    if d is None or len(d) == 0:
        return 0
    ages = {}
    for name, age in d.items():
        if age not in ages:
            ages[age] = 0
        ages[age] += 1
    min_count = min(ages.values())
    min_age = -1
    for age, count in ages.items():
        if count == min_count and (min_age == -1 or age < min_age):
            min_age = age
    return min_age