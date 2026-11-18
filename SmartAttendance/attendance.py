import csv
import os
from datetime import datetime

FILE_NAME = "attendance.csv"


def mark_attendance(name):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Date", "Time"])

        now = datetime.now()

        writer.writerow([
            name,
            now.strftime("%Y-%m-%d"),
            now.strftime("%H:%M:%S")
        ])

    print("Attendance marked:", name)


mark_attendance("Sunzidul")