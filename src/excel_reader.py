from openpyxl import load_workbook
from datetime import datetime
import os

# Path to the Excel file
EXCEL_PATH = os.path.join("data", "timetable.xlsx")


def get_today_schedule():
    """
    Returns:
        {
            "date": "2026-07-13",
            "status": "Working",
            "timetable": "Monday",
            "subjects": [...]
        }
    """

    wb = load_workbook(EXCEL_PATH, data_only=True)

    calendar = wb["Academic_Calendar"]
    weekly = wb["Weekly_Timetable"]

    today = datetime.now().strftime("%Y-%m-%d")

    status = None
    timetable_day = None

    # Find today's entry in Academic_Calendar
    for row in calendar.iter_rows(min_row=2, values_only=True):
        if str(row[0]) == today:
            status = row[2]
            timetable_day = row[3]
            break

    # Holiday
    if status == "Holiday":
        return {
            "date": today,
            "status": "Holiday",
            "subjects": []
        }

    # Read subjects from Weekly_Timetable
    subjects = []

    for row in weekly.iter_rows(min_row=2, values_only=True):
        if row[0] == timetable_day:
            subjects = list(row[1:])
            break

    return {
        "date": today,
        "status": "Working",
        "timetable": timetable_day,
        "subjects": subjects
    }