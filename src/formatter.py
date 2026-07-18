def format_message(schedule):

    if schedule["status"] == "Holiday":
        return f"🎉 Today ({schedule['date']}) is a Holiday!"

    message = f"📅 {schedule['date']}\n"
    message += f"📚 {schedule['timetable']} Timetable\n\n"

    for i, subject in enumerate(schedule["subjects"], start=1):
        if subject:
            message += f"{i}. {subject}\n"

    return message