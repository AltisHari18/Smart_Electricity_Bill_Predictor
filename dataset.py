import pandas as pd
import random

random.seed(42)

rows = []

for _ in range(5000):

    lights = random.randint(2, 12)
    light_hours = random.randint(3, 10)

    fans = random.randint(1, 8)
    fan_hours = random.randint(5, 18)

    ac = random.randint(0, 4)
    ac_hours = random.randint(0, 12) if ac > 0 else 0

    fridge = random.randint(1, 3)

    tv = random.randint(0, 3)
    tv_hours = random.randint(1, 10)

    washing_machine = random.randint(0, 2)
    washing_hours = random.randint(0, 3)

    inverter = random.randint(0, 1)

    geyser = random.randint(0, 2)
    geyser_hours = random.randint(0, 3)

    season = random.choice([0, 1])

    # Approx units calculation
    units = (
        lights * light_hours * 0.08 +
        fans * fan_hours * 0.12 +
        ac * max(ac_hours, 1) * 1.7 +
        fridge * 1.5 +
        tv * tv_hours * 0.1 +
        washing_machine * washing_hours * 0.5 +
        inverter * 0.3 +
        geyser * geyser_hours * 1.2
    ) * 30

    units = int(units + random.randint(20, 100))

    # Indian slab-like billing
    if units <= 100:
        bill = units * 2

    elif units <= 300:
        bill = units * 4.5

    elif units <= 500:
        bill = units * 6.5

    else:
        bill = units * 8

    # Summer extra usage
    if season == 1:
        bill += random.randint(200, 1200)

    bill += random.randint(-200, 300)

    bill = int(max(bill, 100))

    rows.append([
        units,
        lights,
        light_hours,
        fans,
        fan_hours,
        ac,
        ac_hours,
        fridge,
        tv,
        tv_hours,
        washing_machine,
        washing_hours,
        inverter,
        geyser,
        geyser_hours,
        season,
        bill
    ])

columns = [
    "units",
    "lights",
    "light_hours",
    "fans",
    "fan_hours",
    "ac",
    "ac_hours",
    "fridge",
    "tv",
    "tv_hours",
    "washing_machine",
    "washing_hours",
    "inverter",
    "geyser",
    "geyser_hours",
    "season",
    "bill_per_month"
]

df = pd.DataFrame(rows, columns=columns)

df.to_excel(
    "electricity_bill_dataset_5000.xlsx",
    index=False
)

print("5000-row dataset created successfully!")
