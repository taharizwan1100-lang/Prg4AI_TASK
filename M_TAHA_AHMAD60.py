list1 = [47, 56, 52, 54]
list2 = [29, 27, 25, 28]
list3 = [22, 25, 28, 29]
list4 = [91, 58, 74, 88]

LIMITS = {
    "FUEL_PRESS": (40, 55),
    "BATTERY_VOLT": (26, 32),
    "CABIN_TEMP": (18, 27),
    "SIGNAL": (60, 100)
}

READINGS = {
    "FUEL_PRESS": list1,
    "BATTERY_VOLT": list2,
    "CABIN_TEMP": list3,
    "SIGNAL": list4
}

SUBSYSTEM = {
    "FUEL_PRESS": "PROPULSION",
    "BATTERY_VOLT": "POWER",
    "CABIN_TEMP": "THERMAL",
    "SIGNAL": "COMMS"
}

TIMES = ["T-60", "T-40", "T-20", "T-10"]


def check_reading(sensor, value):
    """Check the given sensor name and reading.
    Return NORMAL if within its limits, otherwise ANOMALY.
    """
    low, high = LIMITS[sensor]

    if low <= value <= high:
        return "NORMAL"
    else:
        return "ANOMALY"


def sensor_summary(values):
    """Take a non-empty list of readings.
    Return its minimum, maximum and average using a loop.
    """
    lowest = values[0]
    highest = values[0]
    total = 0
    count = 0

    for value in values:
        if value < lowest:
            lowest = value

        if value > highest:
            highest = value

        total = total + value
        count = count + 1

    average = total / count
    return lowest, highest, average


def subsystem_status(anomaly_count):
    """Take the number of anomalies in a subsystem.
    Return NO-GO for two or more anomalies, otherwise GO.
    """
    if anomaly_count >= 2:
        return "NO-GO"
    else:
        return "GO"


def save_report(filename, report_text):
    """Take a filename and the report text.
    Save the text in write mode and return None.
    """
    with open(filename, "w") as f:
        f.write(report_text)


total_readings = 0
total_anomalies = 0
anomalies = {}

for system in SUBSYSTEM.values():
    anomalies[system] = 0

report = "READINGS\n"
summary = "\nSENSOR SUMMARY\n"

for sensor, values in READINGS.items():

    for i in range(len(values)):
        value = values[i]
        status = check_reading(sensor, value)

        total_readings = total_readings + 1

        if status == "ANOMALY":
            total_anomalies = total_anomalies + 1

            system = SUBSYSTEM[sensor]
            anomalies[system] = anomalies[system] + 1

        report += f"{TIMES[i]} {sensor} {value} {status}\n"

    low, high, average = sensor_summary(values)

    summary += f"{sensor} Min: {low} Max: {high} "
    summary += f"Avg: {average:.2f}\n"

report += summary
report += "\nSUBSYSTEM STATUS\n"

no_go = []

for system, count in anomalies.items():
    status = subsystem_status(count)

    report += f"{system} Anomalies: {count} {status}\n"

    if status == "NO-GO":
        no_go.append(system)

if len(no_go) == 0:
    decision = "GO"
else:
    decision = "NO-GO - " + ", ".join(no_go)

report += f"\nTOTAL READINGS: {total_readings}\n"
report += f"TOTAL ANOMALIES: {total_anomalies}\n"
report += f"LAUNCH DECISION: {decision}\n"

print(report)

name = input("Enter your name: ")
roll = input("Enter roll number: ")

full_report = "NASA LAUNCH CONTROL - GO/NO-GO REPORT\n"
full_report += f"Name: {name}\n"
full_report += f"Roll No: {roll}\n\n"
full_report += report

save_report("mission_report.txt", full_report)

with open("mission_report.txt", "r") as f:
    saved_report = f.read()

if saved_report == full_report:
    print("Report saved and verified.")
else:
    print("Saved report does not match.")


# Task 4 - Question 1:
# check_reading() avoids repeating the same checking code.
# If the checking rule changes, we can update it in one place.

# Task 4 - Question 2:
# Opening an existing file in "w" mode removes its old contents.
# The new report replaces the previous report.